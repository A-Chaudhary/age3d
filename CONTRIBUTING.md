# Contributing to age3d
## Environment Setup
To get started with developing on zkpy, run the following steps:
1. Clone age3d from git
```
git clone https://github.com/A-Chaudhary/age3d.git
cd age3d
```
2. Create and load a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
3. Install dev dependencies
```
make develop
```

## Issues
In case you identify an issue, kindly verify if it has already been reported or not. If not, you can create a new issue to report it.

Moreover, you can browse through the current issues to identify any problems that require attention. If you want to address a specific issue, you are welcome to open a pull request to solve it.

## Pull Requests
Please feel encouraged to make pull requests for changes and new features! Before making a pull request, ensure the following works:
1. All tests pass
```
make test
```
2. Lint passes
```
make lint
```
If needed, run 
```
make fix
```
3. Ensure all checks pass on Github

## New Features
If there is a specific feature that you would like added, please feel free to open a issue with details about the feature.