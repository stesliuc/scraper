import argparse
import src.scrape_utils as scrp
import os


def main(args):
    scraper = scrp.Scraper()
    output_graph = scraper.scrape_url(args.url, args.depth, args.html_element)
    file_path = os.path.join(args.out_dir, "graph")
    with open(file_path, "w") as f:
        f.write(str(output_graph))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape content from websites")

    parser.add_argument("--url", required=True, help="Url to start scraping from")
    parser.add_argument("--depth", type=int, default=2, help="Depth of links")
    parser.add_argument(
        "--html_element",
        required=False,
        default="p",
        help="HTML element to scrape (ex: 'p')",
    )
    parser.add_argument(
        "--out_dir",
        required=False,
        default="results/",
        help="Output directory for scraped graph",
    )

    args = parser.parse_args()
    main(args)
