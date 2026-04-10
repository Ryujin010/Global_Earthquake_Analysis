from src.data_loader import load_data
from src.cleaning import clean_data
from src.analysis import (
    plot_earthquakes_per_year,
    plot_earthquakes_per_5_years,
    plot_geographical_distribution,
    plot_outliers_distribution,
    plot_outliers_magnitude,
    plot_magnitude_distribution,
    plot_earthquakes_per_month,
    plot_years_most_earthquakes,
    plot_magnitude_vs_depth_relationship
)


def main():
    df_geh = load_data("data/raw/earthquakes_1900_2026.csv")
    df_geh = clean_data(df_geh)

    plot_earthquakes_per_year(df_geh)
    plot_earthquakes_per_month(df_geh)
    plot_earthquakes_per_5_years(df_geh)
    plot_geographical_distribution(df_geh)
    plot_outliers_distribution(df_geh)
    plot_magnitude_vs_depth_relationship(df_geh)
    plot_outliers_magnitude(df_geh)
    plot_magnitude_distribution(df_geh)
    plot_years_most_earthquakes(df_geh)

if __name__ == "__main__":
    main()