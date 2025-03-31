IDENTIFICATION DIVISION.
PROGRAM-ID. SomaNumeros.

ENVIRONMENT DIVISION.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 Num1       PIC 9(5).
01 Num2       PIC 9(5).
01 Soma       PIC 9(5).

PROCEDURE DIVISION.
    DISPLAY "Digite o primeiro número: ".
    ACCEPT Num1.

    DISPLAY "Digite o segundo número: ".
    ACCEPT Num2.

    COMPUTE Soma = Num1 + Num2.

    DISPLAY "A soma dos números é: " Soma.

    STOP RUN.
