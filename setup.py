from argparse_prompt import PromptParser

if __name__ == "__main__":
    parser = PromptParser(description="A utility to setup scripting tools for this analysis repo.")
    parser.add_argument("repo-name", help="The title of the analysis (url-safe)")
    args = parser.parse_args()