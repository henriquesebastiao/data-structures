#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Definição da estrutura de um nó da lista ligada
struct Node {
    int value;             // Valor do nó
    struct Node *previous; // Ponteiro para o nó anterior
};

// Função para alocar e criar um novo nó
struct Node* createNode(int value, struct Node *previous) {
    // Alocação de memória para o novo nó
    struct Node *node = (struct Node*) malloc(sizeof(struct Node));
    // Atribuição do valor ao novo nó
    node -> value = value;
    // Se houver um nó anterior, preenche o campo previous para apontar para o nó que estivermos passando no argumento
    if (previous) {
        node -> previous = previous;
    }
    // Retorna o ponteiro para o novo nó criado
    return node;
}

// Função para inserir um nó no meio da lista
struct Node* insertNode(int value, struct Node *previous, struct Node *next) {
    struct Node *node = (struct Node*) malloc(sizeof(struct Node));
    node -> value = value;
    if (previous) {
        node -> previous = previous;
    }
    if (next) {
        next -> previous = node;
    }
}

void main() {
    struct Node *first = createNode(2020, NULL);
    struct Node *second = createNode(2021, first);
    struct Node *third = createNode(2022, second);
    struct Node *insert = insertNode(2050, second, third);

    // Inicialização do iterador como o último nó (terceiro nó)
    struct Node *iterator = third;
    // Loop para percorrer a lista a partir do último nó até o primeiro nó
    while (iterator)
    {
        // Imprime o valor do nó atual
        printf("%d, ", iterator-> value);
        // Move o iterador para o nó anterior
        iterator = iterator -> previous;
    }
    printf("\n");
}
