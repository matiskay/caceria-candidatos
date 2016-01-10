# Instalación
* crear virtualenvironment. Usar Python 3.
* instalar requisitos: `pip install -r requirements.txt`
* instalar elasticsearch
* agregar datos a elasticsearch:
    * `python add_redam_to_index.py`
    * `python add_indultados_to_index.py`
    * `python add_candidates_2014_to_index.py`
    * `python add_deudores_to_index.py "data/BASE_DE_DATOS_REGISTRO_DE_DEUDORES_POR_DELITO_AGRAVIO_ESTADO_Enero_2016.TSV"`
    * `python add_deudores_to_index.py "data/BASE_DE_DATOS_REGISTRO_DE_DEUDORES_POR_DELITO_AGRAVIO_ESTADO.CSV"`
* todos los datos de deudores, indultados, etc están en el folder `data`.
* buscar si nombres de una lista aparecen en la relación de deudores,
  indultados, etc:
    * `python search_from_list_of_names.py -i lista_de_nombres.txt`
* profit.
