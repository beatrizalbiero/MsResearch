# The Corpus

|          | Whole Corpus | Corpus without non-family Verbs | Total Regular Verbs | Total Irregular Verbs |
|:--------:|:------------:|:----------------------------------:|:-------------------:|:---------------------:|
| Absolute |      423     |                 403                |         214         |          209          |
|     %    |       -      |                 100                |      50.59           |         49.40          |

## Classes of Irregularities


| iar: eiu | o_ar: O_u | o_ir: u_o | izer: igu | fazer: fasu | ler, crer: eiu | entir: intu | edir: Esu |
|:----------:|-------------|-------------|-------------|---------------|------------------|---------------|-------------|
|      9     | 30          | 7           | 7           | 15            | 5                | 8             | 7           |

| or: oniu | e_ir: i_u | ter: teniu | e_ar: E_u  | ver: veju | vir: veniu |
|:----------:|-------------|--------------|--------------|-------------|--------------|
|     27     | 27          | 10           | 20           | 6           | 11           |

# Phonetic Keys for Transcription

![Table](https://github.com/beatrizalbiero/MsResearch/blob/master/WickelfeaturesProject/img/Screen%20Shot%202019-06-28%20at%2012.28.44.png)

## Non-Family Verbs - Total: 20

requerer -> requero
<br/>
entrequerer -> entrequero
<br/>
querer -> quero
<br/>
saber -> sei
<br/>
equivaler -> equivalho
<br/>
prover -> provenho
<br/>
trazer -> trago
<br/>
poder -> posso
<br/>
desdar -> desdo
<br/>
idear -> ideio
<br/>
estrear -> estreio
<br/>
dar -> dou
<br/>
sobrestar -> sobrestou
<br/>
estar -> estou
<br/>
caber -> caibo
<br/>
saber -> sei
<br/>
ouvir -> ouco
<br/>
entreouvir -> ouco
<br/>
reouvir -> reouco
<br/>
parir -> pairo
<br/>
perder -> perco

---

# Files

## treated_corpus.csv - Total: 403

This is the file containing all verbs except those considered "non-family" verbs.

--------
## Test and Train Corpora

The table below exhibits the verbs that form the test and train corpora according to the number/proportion of regular and irregular verbs.

|       | Regulars | Irregulars | Total | %     |
|-------|----------|------------|-------|-------|
| Test  | 42       | 36         | 78    | 19.35 |
| Train | 172      | 153        | 325   | 80.65 |
| Total | 214      | 189        | 403   | 100   |

## train_corpus.csv - Total: 325

| iar: eiu | o_ar: O_u | o_ir: u_o | izer: igu | fazer: fasu | ler, crer: eiu | entir: intu | edir: Esu |
|:----------:|-------------|-------------|-------------|---------------|------------------|---------------|-------------|
|      7     |  24         |     6      |  6         |      12       |        4        |   6           |       6     | |

| or: oniu | e_ir: i_u | ter: teniu | e_ar: E_u  | ver: veju | vir: veniu | regulars|
|:----------:|-------------|--------------|--------------|-------------|--------------|---|
|     22     |      22     |   8         |       16    |        5    |      8     | 172 |

## test_corpus.csv - Total: 78

| iar: eiu | o_ar: O_u | o_ir: u_o | izer: igu | fazer: fasu | ler, crer: eiu | entir: intu | edir: Esu |
|:----------:|-------------|-------------|-------------|---------------|------------------|---------------|-------------|
|      2     |      6       |   1        |   1        |         3    |       1         |   2           |       1     | |

| or: oniu | e_ir: i_u | ter: teniu | e_ar: E_u  | ver: veju | vir: veniu | regulars|
|:----------:|-------------|--------------|--------------|-------------|--------------|---|
|    5      |     5      |  2          |     4      |       1     |     2      | 42 |

---

# Folders

## corpus_separated_by_classes.csv

This folder contains multiple .csv files. Each file concerns a family of verbs and contains all the verbs that belong to such family.

## corpus_different_proportions.csv

This folder contains multiple different datasets (.csv). The regular-irregular verb ratio varies per dataset.
