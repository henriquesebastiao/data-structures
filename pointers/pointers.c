#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void main() {
    int numero = 10;
    int *ponteiro = &numero;
    printf("%d\n", numero);
    printf("%d\n", &numero);
    printf("%d\n", ponteiro);
    printf("%d\n", &ponteiro);
    printf("%d\n", *ponteiro);

    // Output
    // 10 (valor da variavel numero)
    // -1692088420 (endereço de memória onde está a veriável número)
    // -1692088420 (o valor do ponterio é endereço de memória onde está o valor da variável cujo a qual ele referencia)
    // -1692088416 (endereço de memória do próprio ponteiro)
    // 10 (valor da variavel que o ponteiro está referenciando)
}