//
// Created by Яков Контарук on 06.02.2023.
//

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Введите количество элементов в массиве: ";
    cin >> n;
    int arr[100];
    cout << "Введите элементы массива: ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    cout << "Отсортированный массив: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}
