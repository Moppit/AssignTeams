# CapstoneTeamsProblem

Every year, the majority of senior students in CU Boulder's Computer Science department enroll in the software engineering capstone project. This tool uses linear programming to generate optimal student to project matchings.

See this video for a summary of the project, the math behind it, and a demo: https://drive.google.com/file/d/11iO3ZGFLaayVtsiGlMb_zrdxF7zLcntM/view?usp=sharing

## Getting Started
First, install `pulp`, the library behind the linear programming capabilities:
```
pip3 install PuLP
```

You may also have to install common data-parsing libraries like `pandas` if you don't have them already.

## Usage
To run the code, use the command:
```
python3 solve_LP.py
```

As it stands, the script is calculating results based on the given test data. This data was anonymized, and extraneous data has been removed. As it stands, you must modify your data's column headings to match the headings in the sample .csv files.

To tune the parameters (i.e. project team sizes, considering team skills distributions, etc), modify `parameters.py`. The `CONSIDER_` variables determine whether you want a parameter to affect team determinations, and the adjustable parameters determine exact threshold values. Don't be afraid to modify these parameters and iterate until you get an output you're satsified with!

If there's no optimal solution, the output will say `Status: Infeasible`.

If there's an optimal solution, the output will say `Status: Optimal`. Each project will be displayed with a list of students matched to the project.

## Future Features
- Automated data munging: Qualtrics results still need to be modified by hand to match the sample1.xlsx formats
- Better display showing the student's ranking of the project for their matching
- Code quality
    - Cleaning up some areas in the code, specifically `read_data.py`
    - Adding more comprehensive comments, specifically in `helpers.py`
    - Remove duplicated code, specifically in `dummy_data.py` (for testing)



