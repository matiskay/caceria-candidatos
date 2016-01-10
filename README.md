# Instalación
* crear virtualenvironment. Usar Python 3.
* instalar requisitos: `pip install -r requirements.txt`
* instalar elasticsearch
* agregar datos a elasticsearch:
    * `python add_redam_to_index.py`
    * `python add_indultados_to_index.py`
    * así sucesivamente.
* todos los datos de deudores, indultados, etc están en el folder `data`.
* buscar si nombres de una lista aparecen en la relación de deudores,
  indultados, etc:
    * `python search_from_list_of_names.py -i lista_de_nombres.txt`
* profit.
