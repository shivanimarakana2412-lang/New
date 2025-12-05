

"""
Data Analysis & Visualization Program (uses sample_data_for_cleaning.csv)

How to run:
- In Jupyter: paste cells or run `%run your_script.py`
- In terminal: `python your_script.py`
- Make sure pandas, numpy, matplotlib, seaborn are installed:
    pip install pandas numpy matplotlib seaborn
"""

import sys
import os
from typing import Optional
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Default CSV path (change if needed)
DEFAULT_CSV_PATH = "/mnt/data/sample_data_for_cleaning.csv"

class SalesDataAnalyzer:
    def __init__(self, file_path: Optional[str] = None):
        self.file_path = file_path or DEFAULT_CSV_PATH
        self.data: Optional[pd.DataFrame] = None

    def load_data(self, file_path: Optional[str] = None):
        path = file_path or self.file_path
        try:
            self.data = pd.read_csv(path)
            # attempt to parse dates if a column looks like a date
            for col in self.data.columns:
                if self.data[col].dtype == object:
                    try:
                        parsed = pd.to_datetime(self.data[col], errors="coerce")
                        # if many values parsed (not all NaT), keep new dtype
                        if parsed.notna().sum() > 0:
                            self.data[col] = parsed
                    except Exception:
                        pass
            print(f"Dataset loaded: {path} (rows: {len(self.data)})")
        except FileNotFoundError:
            print(f"File not found: {path}")
            self.data = None
        except Exception as e:
            print("Error loading file:", e)
            self.data = None

    def explore_data(self, show_n=5):
        if self.data is None:
            print("No data loaded.")
            return
        print("\n== head ==")
        display = getattr(self.data, "head")
        print(self.data.head(show_n).to_string(index=False))
        print("\n== tail ==")
        print(self.data.tail(show_n).to_string(index=False))
        print("\n== info ==")
        print(self.data.info())
        print("\n== describe (numeric) ==")
        print(self.data.describe(include=[np.number]).to_string())
        print("\n== columns ==")
        print(list(self.data.columns))

    def clean_data(self, drop_thresh=0.5, fill_strategy=None, fill_value=None):
        """
        drop_thresh: fraction of non-NA required to keep column (e.g. 0.5 keeps columns with >=50% non-NA)
        fill_strategy: one of [None, 'mean', 'median', 'mode', 'ffill', 'bfill', 'value']
        fill_value: used if fill_strategy == 'value'
        """
        if self.data is None:
            print("Load data first.")
            return

        print("\n== Missing value summary (before) ==")
        print(self.data.isna().sum())

        # Drop columns with too many missing values
        keep_cols = [c for c in self.data.columns if self.data[c].dropna().shape[0] / len(self.data) >= drop_thresh]
        dropped = set(self.data.columns) - set(keep_cols)
        if dropped:
            print(f"Dropping columns with >{100*(1-drop_thresh):.0f}% missing: {dropped}")
            self.data = self.data[keep_cols]

        # Fill missing values according to strategy
        if fill_strategy is not None:
            for col in self.data.columns:
                if self.data[col].isna().sum() == 0:
                    continue
                if fill_strategy == "mean" and pd.api.types.is_numeric_dtype(self.data[col]):
                    self.data[col].fillna(self.data[col].mean(), inplace=True)
                elif fill_strategy == "median" and pd.api.types.is_numeric_dtype(self.data[col]):
                    self.data[col].fillna(self.data[col].median(), inplace=True)
                elif fill_strategy == "mode":
                    mode_val = self.data[col].mode(dropna=True)
                    if len(mode_val) > 0:
                        self.data[col].fillna(mode_val[0], inplace=True)
                elif fill_strategy == "ffill":
                    self.data[col].fillna(method="ffill", inplace=True)
                elif fill_strategy == "bfill":
                    self.data[col].fillna(method="bfill", inplace=True)
                elif fill_strategy == "value":
                    self.data[col].fillna(fill_value, inplace=True)
                else:
                    # no-op
                    pass

        print("\n== Missing value summary (after) ==")
        print(self.data.isna().sum())

    def mathematical_operations(self):
        """
        Demonstrates element-wise ops and adds some example derived columns if numeric columns exist.
        """
        if self.data is None:
            print("Load data first.")
            return
        numeric = self.data.select_dtypes(include=[np.number]).columns.tolist()
        if not numeric:
            print("No numeric columns to perform mathematical operations on.")
            return
        print("Numeric columns:", numeric)
        # Example: normalized version of first numeric column
        col = numeric[0]
        new_col = col + "_norm"
        arr = self.data[col].to_numpy()
        minv, maxv = np.nanmin(arr), np.nanmax(arr)
        if maxv - minv != 0:
            self.data[new_col] = (arr - minv) / (maxv - minv)
            print(f"Added normalized column: {new_col}")
        else:
            self.data[new_col] = np.nan
            print(f"Column {col} was constant; created {new_col} of NaNs")

        # Example: element-wise add of two numeric cols if available
        if len(numeric) >= 2:
            a, b = numeric[0], numeric[1]
            self.data[f"{a}_plus_{b}"] = self.data[a] + self.data[b]
            print(f"Added column: {a}_plus_{b}")

    def combine_data(self, other_df: pd.DataFrame, how="concat"):
        if self.data is None:
            print("Load data first.")
            return
        if how == "concat":
            combined = pd.concat([self.data, other_df], ignore_index=True, sort=False)
        elif how == "merge":
            # merge on intersection of columns if possible
            common = list(set(self.data.columns) & set(other_df.columns))
            if not common:
                print("No common columns to merge on; using concat instead.")
                combined = pd.concat([self.data, other_df], ignore_index=True, sort=False)
            else:
                combined = pd.merge(self.data, other_df, on=common, how="outer")
        else:
            raise ValueError("how must be 'concat' or 'merge'")
        print("Combined dataset rows:", len(combined))
        return combined

    def split_data(self, by: str):
        """
        Split by unique values of a column -> returns dict of dataframes
        """
        if self.data is None:
            print("Load data first.")
            return {}
        if by not in self.data.columns:
            print(f"Column {by} not in dataset.")
            return {}
        groups = {k: v.copy() for k, v in self.data.groupby(by)}
        print(f"Split into {len(groups)} groups based on {by}")
        return groups

    def search_sort_filter(self, search_col=None, search_val=None, sort_by=None, ascending=True, filter_expr=None):
        """
        - search_col & search_val: returns rows where search_col == search_val (or contains if str)
        - sort_by: column name to sort
        - filter_expr: a pandas-query style string, e.g. "Age > 16 and Score >= 80"
        """
        if self.data is None:
            print("Load data first.")
            return None
        df = self.data
        if filter_expr:
            try:
                df = df.query(filter_expr)
            except Exception as e:
                print("Filter query error:", e)
        if search_col and search_val is not None:
            if pd.api.types.is_string_dtype(df[search_col]):
                df = df[df[search_col].str.contains(str(search_val), na=False, case=False)]
            else:
                df = df[df[search_col] == search_val]
        if sort_by:
            df = df.sort_values(by=sort_by, ascending=ascending)
        return df

    def aggregate_functions(self, group_by_cols: list, agg_map: dict):
        """
        group_by_cols: list of columns to group by
        agg_map: dict of column -> aggregation e.g. {'Score': ['mean','sum'], 'Age':'count'}
        """
        if self.data is None:
            print("Load data first.")
            return None
        result = self.data.groupby(group_by_cols).agg(agg_map)
        return result

    def statistical_analysis(self):
        if self.data is None:
            print("Load data first.")
            return None
        stats = {
            "describe": self.data.describe(include="all"),
            "std": self.data.std(numeric_only=True),
            "var": self.data.var(numeric_only=True),
            "quantiles": self.data.quantile([0.25, 0.5, 0.75])
        }
        return stats

    def create_pivot_table(self, index_cols, columns_col, values_col, aggfunc="mean"):
        if self.data is None:
            print("Load data first.")
            return None
        pivot = pd.pivot_table(self.data, index=index_cols, columns=columns_col, values=values_col, aggfunc=aggfunc)
        return pivot

    def visualize_data(self, kind="bar", x=None, y=None, hue=None, save_path=None):
        """
        kind: bar, line, scatter, pie, hist, box, heatmap, stack
        """
        if self.data is None:
            print("Load data first.")
            return
        plt.figure(figsize=(8, 5))
        try:
            if kind == "bar":
                if x and y:
                    sns.barplot(data=self.data, x=x, y=y, hue=hue)
                else:
                    # bar of counts for first non-numeric column
                    cat = self.data.select_dtypes(include=["object", "category"]).columns[0]
                    sns.countplot(data=self.data, x=cat)
            elif kind == "line":
                if x and y:
                    sns.lineplot(data=self.data.sort_values(by=x), x=x, y=y, hue=hue)
                else:
                    print("line plot requires x and y.")
            elif kind == "scatter":
                if x and y:
                    sns.scatterplot(data=self.data, x=x, y=y, hue=hue)
                else:
                    print("scatter requires x and y.")
            elif kind == "pie":
                # pie for counts of top categories in first object column
                cat = self.data.select_dtypes(include=["object", "category"]).columns[0]
                counts = self.data[cat].value_counts()
                counts.plot.pie(autopct="%1.1f%%")
            elif kind == "hist":
                if x:
                    self.data[x].plot.hist()
                else:
                    self.data.select_dtypes(include=[np.number]).iloc[:, 0].plot.hist()
            elif kind == "box":
                if y:
                    sns.boxplot(data=self.data, y=y, x=x)
                else:
                    self.data.select_dtypes(include=[np.number]).plot.box()
            elif kind == "heatmap":
                corr = self.data.select_dtypes(include=[np.number]).corr()
                sns.heatmap(corr, annot=True)
            elif kind == "stack":
                # stack plot of numeric columns (first 3)
                nums = self.data.select_dtypes(include=[np.number]).columns[:3]
                if len(nums) >= 2:
                    self.data[nums].fillna(0).head(50).plot.area(stacked=True)
                else:
                    print("Not enough numeric columns for stack plot.")
            else:
                print("Unknown plot kind.")
            plt.title(f"{kind} plot")
            plt.tight_layout()
            if save_path:
                plt.savefig(save_path)
                print(f"Saved plot to {save_path}")
            plt.show()
        except Exception as e:
            print("Visualization error:", e)
            plt.close()

    # Extra helper: show numpy indexing/slicing examples
    def numpy_examples(self):
        if self.data is None:
            print("Load data first.")
            return
        print("\n== Numpy conversion and indexing examples ==")
        # convert numeric columns to numpy
        nums = self.data.select_dtypes(include=[np.number]).columns.tolist()
        if not nums:
            print("No numeric columns to demonstrate numpy arrays.")
            return
        arr = self.data[nums].to_numpy()
        print("Array shape:", arr.shape)
        # show first 3 rows
        print("First 3 rows (numpy):")
        print(arr[:3, :])
        # slice: first column, rows 1..3
        print("Slice rows 1..3 of first numeric column:")
        print(arr[1:4, 0])
        # elementwise operation example:
        print("Elementwise add first two numeric columns (if exist):")
        if arr.shape[1] >= 2:
            print(arr[:, 0] + arr[:, 1])

# ---------------------------
# Menu-driven console UI
# ---------------------------
def print_menu():
    menu = """
========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations (math/convert)
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization (quick example)
8. Numpy Examples
9. Exit
==========================================================
"""
    print(menu)

def main():
    analyzer = SalesDataAnalyzer()
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            path = input(f"Enter path to CSV (default: {analyzer.file_path}): ").strip()
            if path == "":
                path = analyzer.file_path
            analyzer.load_data(path)
        elif choice == "2":
            analyzer.explore_data()
        elif choice == "3":
            print("1) Mathematical ops & derived columns\n2) Convert columns types\n3) Combine with another CSV")
            c = input("Choice: ").strip()
            if c == "1":
                analyzer.mathematical_operations()
            elif c == "2":
                print("Columns:", analyzer.data.columns.tolist() if analyzer.data is not None else [])
                col = input("Column to convert: ").strip()
                dtype = input("Target dtype (int,float,str,datetime): ").strip()
                if analyzer.data is not None and col in analyzer.data.columns:
                    try:
                        if dtype == "datetime":
                            analyzer.data[col] = pd.to_datetime(analyzer.data[col], errors="coerce")
                        else:
                            analyzer.data[col] = analyzer.data[col].astype(dtype)
                        print("Conversion successful.")
                    except Exception as e:
                        print("Conversion error:", e)
            elif c == "3":
                other_path = input("Enter path to another CSV to combine: ").strip()
                if os.path.exists(other_path):
                    other = pd.read_csv(other_path)
                    combined = analyzer.combine_data(other, how="concat")
                    if combined is not None:
                        print("Combined preview:")
                        print(combined.head().to_string(index=False))
                else:
                    print("Other file not found.")
        elif choice == "4":
            print("Missing data options:\n1. Show missing\n2. Drop columns by threshold\n3. Fill missing (mean/median/mode/ffill/bfill/value)")
            c = input("Choice: ").strip()
            if c == "1":
                print(analyzer.data.isna().sum() if analyzer.data is not None else "Load data first.")
            elif c == "2":
                thresh = input("Keep columns with at least what fraction of non-missing? (0-1) default 0.5: ").strip()
                thresh = float(thresh) if thresh else 0.5
                analyzer.clean_data(drop_thresh=thresh)
            elif c == "3":
                strat = input("Strategy (mean/median/mode/ffill/bfill/value): ").strip()
                val = None
                if strat == "value":
                    val = input("Value to use: ")
                analyzer.clean_data(drop_thresh=0.0, fill_strategy=strat, fill_value=val)
        elif choice == "5":
            stats = analyzer.statistical_analysis()
            if stats:
                print("Describe:")
                print(stats["describe"].to_string())
                print("\nStd:\n", stats["std"])
                print("\nVar:\n", stats["var"])
        elif choice == "6":
            print("Plot kinds: bar, line, scatter, pie, hist, box, heatmap, stack")
            kind = input("kind: ").strip()
            x = input("x column (or Enter): ").strip() or None
            y = input("y column (or Enter): ").strip() or None
            hue = input("hue (or Enter): ").strip() or None
            analyzer.visualize_data(kind=kind, x=x, y=y, hue=hue)
        elif choice == "7":
            # quick example: save a histogram of first numeric column
            nums = analyzer.data.select_dtypes(include=[np.number]).columns.tolist() if analyzer.data is not None else []
            if not nums:
                print("No numeric columns to save a plot.")
            else:
                save_path = input("Enter filename to save (e.g., myplot.png): ").strip()
                if save_path == "":
                    save_path = "saved_plot.png"
                analyzer.visualize_data(kind="hist", x=nums[0], save_path=save_path)
        elif choice == "8":
            analyzer.numpy_examples()
        elif choice == "9":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
