import os

import wget

url_dict = {
    "train_pbmc": "https://drive.google.com/uc?export=download&id=1vXiEzN14M8tzSngPc8ufowOEv4sokVs9",
    "valid_pbmc": "https://drive.google.com/uc?export=download&id=1cd0NgirLuL81-igegduLGxEpHKSs2-C5",

    "train_hpoly": "https://drive.google.com/uc?export=download&id=1IZkQcIj1jz04cyLOW-IHtEc4jBNeBxVQ",
    "valid_hpoly": "https://drive.google.com/uc?export=download&id=1ZwN7BpUWfzV8-hYnjAq2FeGMec5phKxZ",

    "train_salmonella": "https://drive.google.com/uc?export=download&id=11lFjCiYwFIwm21QCCCeabTupiy6LqQjJ",
    "valid_salmonella": "https://drive.google.com/uc?export=download&id=1ytgIt2talgHPbX_CNu5O7bkMP8A1SGdJ",

    "train_species": "https://www.dropbox.com/s/vb5xm2y9eqwunmh/train_species.h5ad?dl=1",
    "valid_species": "https://drive.google.com/uc?export=download&id=1CNcESxSIsSZcqNIXjZpiiWmkOIMlr9h7",

    "train_study": "https://drive.google.com/uc?export=download&id=1dUZ_4f5EuU9YYu7APfrxl6mhbpSqairb",
    "valid_study": "https://drive.google.com/uc?export=download&id=1HAzqBAQnd8zUKD3FqoAyUEitgw7-BDyg",

    "train_zheng": "https://drive.google.com/uc?export=download&id=17E0Ew9vNqCigJn_1xDUgO4clBslinAMc",

    "pancreas": "https://www.dropbox.com/s/qj1jlm9w10wmt0u/pancreas.h5ad?dl=1",
    "bbknn": "https://www.dropbox.com/s/mkxzca2447x3hdu/bbknn.h5ad?dl=1",
    "cca": "https://www.dropbox.com/s/fjn3hc3z994kerg/cca.h5ad?dl=1",
    "mnn": "https://www.dropbox.com/s/n4vl10h7zw7m6tl/mnn.h5ad?dl=1",
    "scanorama": "https://www.dropbox.com/s/2ek1rfus06737ik/scanorama.h5ad?dl=1",

    "MouseAtlas.subset": "https://www.dropbox.com/s/zkss8ds1pi0384p/MouseAtlas.subset.h5ad?dl=1"

}


def download_data(data_name, key=None):
    data_path = "../data/"
    if key is None:
        train_path = os.path.join(data_path, f"train_{data_name}.h5ad")
        valid_path = os.path.join(data_path, f"valid_{data_name}.h5ad")

        train_url = url_dict[f"train_{data_name}"]
        valid_url = url_dict[f"valid_{data_name}"]

        if not os.path.exists(train_path):
            wget.download(train_url, train_path)
        if not os.path.exists(valid_path):
            wget.download(valid_url, valid_path)
    else:
        data_path = os.path.join(data_path, f"{key}.h5ad")
        data_url = url_dict[key]

        if not os.path.exists(data_path):
            wget.download(data_url, data_path)
    print(f"{data_name} data has been downloaded and saved in {data_path}")


def main():
    data_names = ["pbmc", "hpoly", "salmonella", "species", "study"]
    for data_name in data_names:
        download_data(data_name)
    keys = ["train_zheng", "pancreas", "bbknn", "cca", "mnn", "MouseAtlas.subset"]
    for key in keys:
        download_data(None, "key")


if __name__ == '__main__':
    main()
