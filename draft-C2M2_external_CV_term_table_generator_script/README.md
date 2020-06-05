# Building 'green' tables from core tables

(please someone add links and so on so that this is more understandable)

There are only green tables to be run for level 1, not for level 0.

The script is named `build_term_tables.py` and you can run it like so:

```
./build_term_tables.py
```

It takes in `biosample.tsv` and `file.tsv` (core-entity ETL instance
TSVs, aka two of the three gold tables) and produces `file_format`,
`data_type`, `assay_type`, and `anatomy` TSV files.

It will load OBO and ontology stuff from `--cvRefDir`, which is by default `external_CV_reference_files`.

It will load `file.tsv` and `biosample.tsv` from the `--draftDir`
which is by default
`../draft-C2M2_example_submission_data/HMP__sample_C2M2_Level_1_bdbag.contents`.

It will output four TSVs into `--outDir`, which by default is `./007_HMP-specific_CV_term_usage_TSVs`.

Run it with `-h` for command line help.

