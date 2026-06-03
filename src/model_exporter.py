import os
import joblib


def save_model(model, path):

    project_root = os.path.dirname(os.getcwd())

    os.makedirs(
        os.path.join(project_root, "models"),
        exist_ok=True
    )

    joblib.dump(model, path)

    print(f'Modelo Guardado en : {path}')