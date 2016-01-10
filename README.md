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

## Ejemplo

```
python search_from_list_of_names.py -i lista_apra.txt 
2.2043698       deudores        Enrique Valderrama      Wilfredo Enrique Valderrama Zegarra http://pisaq.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=276
2.1855752       deudores        Enrique Valderrama      WILFREDO ENRIQUE VALDERRAMA ZEGARRA http://ot.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=8750
2.1371934       deudores        Enrique Valderrama      Wilfredo Enrique Valderrama Zegarra http://ot.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=276
2.2855947       narcoindultos   Victor de la Roca       DE LA ROCA ROJAS, VICTOR MANUEL, conmutarle de 04 años a 03 años 02 meses de pena
2.197633        narcoindultos   Victor de la Roca       DE LA ROCA ROJAS, VICTOR MANUEL, conmutarle de 04 años a 03 años 02 meses de pena
2.714491        candidato_2014  Carlos Arana    ARANA, ANYAIPOMA, CARLOS, 06001815, ABUSO DE AUTORIDAD
2.375986        deudores        Jorge del Castillo      JORGE AUGUSTO DEL CASTILLO RAMIREZ http://pisaq.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=6084
2.329935        deudores        Jorge del Castillo      JORGE AUGUSTO DEL CASTILLO RAMIREZ http://ot.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=6084
2.1775408       deudores        Fernando Arias  Fernando Morgan Arias http://ot.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=8135
2.1568613       deudores        Fernando Arias  FERNANDO ABEL ARIAS CARDENAS http://ot.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=1222
2.1568613       deudores        Fernando Arias  FERNANDO MORGAN ARIAS http://ot.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=6502
2.1568613       deudores        Fernando Arias  FERNANDO ABEL ARIAS CARDENAS http://pisaq.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=1222
2.1297197       deudores        Fernando Arias  FERNANDO MORGAN ARIAS http://pisaq.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=6502
2.4034545       narcoindultos   Luis Negreiros  5. NEGREIROS MONTERO, LUIS PEDRO, conmutarle de 06 años a 04 años 26 días de
2.3947446       narcoindultos   Luis Negreiros  5. NEGREIROS MONTERO, LUIS PEDRO, conmutarle de 06 años a 04 años 26 días de
```
