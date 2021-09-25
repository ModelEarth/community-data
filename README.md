# Community Datasets

Pre-processed state, county and zipcode data for the [model.earth](https://model.earth) project.  

Most data currently resides in our [community-data/us/state](https://github.com/modelearth/community-data/tree/master/us/state) subfolders.  



We're using Github Actions. Here are our [Github&nbsp;Actions&nbsp;samples](https://model.earth/community/projects/#github-actions).




<br><br><br><br><br>

## Running the Pipeline Locally<br>(We're not currently using the following. Using GitHub Actions instead.)

We did not implement the following Python pipeline. The following orginated from the [Public Tree Map Pipeline](https://github.com/Public-Tree-Map/public-tree-map-data-pipeline). We're using GitHub Action instead.  


Prerequisites:
- `make`
- `node`

After a fresh clone, run `npm install` to install the necessary node modules.

To run the full pipeline, which will download the latest tree data and all
images, run:

```bash
make release
```

To skip lengthy network requests, you can run a smaller version of the pipeline
with:

```bash
make local-only
```

See the `Makefile` for other rules that are available.

### Viewing the Logs

The various scripts that makeup the pipeline rely on reading/writing to stdin 
and stdout, so the scripts can't log to stdout like you'd expect. Instead, they
write to a log file that's located at tmp/log.txt. If you'd like to watch logs
as they happen, simply run:

```bash
tail -f tmp/log.txt
```

### Command Documentation

#### find\_missing\_species.py
This covers how to run the find_missing_species.py script. Let's start with the command line options and what they do:
```
python find_missing_species.py -u <inventory url> -s <known species csv file> -o <output file>
```
`-u`: This is the url to download the tree inventory csv from santa monica. This data must also contain the column, `Species ID`, which is the species id. If not specified, it defaults to `https://data.smgov.net/resource/w8ue-6cnd.csv?$limit=50000`

`-s`: This specifies the csv file containing all known species ids. This script expects the species id in the column named `Species ID`. If not specified, it defaults to `data/species_attributes.csv`

`-o`: This specifies the name of the output csv file. If not specified it prints the csv file to stdout (aka the command line).


Here are some examples:

```
python find_missing_species.py -h # this shows you all the options (and explanations)

# this grabs data from the santa monica trees dataset and saves them to missing_trees.csv
python find_missing_species.py -o missing_trees.csv

# uses all the defaults and prints the output to the command line
python find_missing_species.py
```

### General Thoughts on the Pipeline

We don't want a server. To avoid this, we serve static data as JSON via a Google 
Cloud bucket. This has a number of benefits, namely cost and client simplicity.

The pipeline in general works like this:

- Start with tree data provided by FLOWSA, Federal Farmfresh data, etc.
- End with CSV and JSON files that can be used to render maps, and a series of 
  JSON files that represent the details of individual locations and zip codes.
- In between, we break down each augmentation/alteration of the data into a
  series of distinct processes, each of which reads from stdin and writes to
  stdout. Examples include doing the initial parse of the CSV and APIs.
- Each of these scripts are written and documented extensively.
- The Makefile composes these scripts into a set of routines.
- CircleCI will run the `make release` script nightly to update the data.

## Protocol for pull requests + code review

- Please review open issues and link your pull request to the relevant issue.
- Please create new branch!
- For all **new** changes, please submit your pull request to the ```test-circleci``` branch.
- In your pull request, please list and explain all proposed changes to the code base (additions, deletions). If you reuse code from elsewhere, please make sure you've attributed it.
- Please apply all relevant labels to your pull request.
- Please request a review (either from a specific person or from the appropriate [slack channel](https://model.earth/community/challenge/meetups/)).
- Reviewers: please review all proposed changes, write comments and questions in line notes. Please review all updates made at your request.
- Reviewer and requester: please confirm with each other that the PR is ready to merge. Please make sure that the PR branch name documents the new changes.

## Data Sources

EPA FLOWSA - [Display datasets from API](https://model.earth/localsite/info/data/)  
BEA - [Our prior script](process/python/bea/)
