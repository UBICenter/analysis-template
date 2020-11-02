# UBI Center analysis template
Template for UBI Center analyses, including Jupyter-Book and GitHub Action files.

Instructions:
* Replace `reponame` in `.github/workflows/*` files with the name of the repo.
* Replace `reponame` in `jb/_config.yml` with the name of the repo.
* Add data generation `.py` script and data files to `jb/data` folder.
Store files in `.csv.gz` format and load them as local files in analysis notebooks.