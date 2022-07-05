*** Settings ***
Suite Setup    Open Browser    https://www.google.com.br/    Chrome
Library    Enviar Gmail.py
Library    SeleniumLibrary



*** Test Cases ***  
Teste configuração para envio de email
    Teste envio email
*** Keywords ***
Teste envio email
    Sleep    2
    TRY
        Wait Until Page Contains    Texto inexistente para simular erro
        Log To Console     Teste Ok
    EXCEPT  
        Log To Console    Teste Não Ok    
        enviar_email    Reporte de Erros - [${TEST_NAME}]
        Fail   
    END
