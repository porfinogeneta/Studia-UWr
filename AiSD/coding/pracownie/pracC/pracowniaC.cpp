#include <stdio.h>
#include <vector>
#include <utility>
#include <iostream>
#include <limits>
// #include <fstream>

using namespace std;

const int NEGATIVE_INFINITY = numeric_limits<int>::min();
const int POSITIVE_INFINITY = numeric_limits<int>::max();


// sprawdzamy czy mozemy skorzystać z monety (nie ma za duzej wagi)
// oraz sprawdzamy czy jak rozwiązemy problem za pomocą tej monety to sprowadzi się
// on to innego problemu, ktory juz korzystnie rozwiązaliśmy
void evaluateCoins(pair<int, int>* problems, int problemsSize, pair<int, int>* coins, int coinsAmount, bool Max) {
    // problemy mają pierwotnie wartość -inf
    for (int i = 0; i < problemsSize; ++i) {
        if (Max) {
            problems[i] = make_pair(NEGATIVE_INFINITY, NEGATIVE_INFINITY);
        }else {
            problems[i] = make_pair(POSITIVE_INFINITY, POSITIVE_INFINITY);
        }
        
    }
    // 0 problem mamy za darmo
    problems[0].first = 0;
    problems[0].second = 0;
    // probujemy rozwiązać kolejne problemy wagowe
    for (int p = 1; p < problemsSize; p++){
        // za pomocą kolejnych monet
        for (int c = 0; c < coinsAmount; c++){
            if (Max) {
                if (p - coins[c].second >= 0 && problems[p - coins[c].second].first != NEGATIVE_INFINITY) {
                    // sprawdzamy czy problem będzie korzystniej rozwiązany
                    if (problems[p - coins[c].second].first + coins[c].first > problems[p].first){
                        // jak tak podmieniamy monetę i nominał uzyskany
                        problems[p].first = problems[p - coins[c].second].first + coins[c].first;
                        problems[p].second = c; // wrzucamy na drugą pozycję indeks korzystniejszej monety
                    }
                }
            }else {
                if (p - coins[c].second >= 0 && problems[p - coins[c].second].first != POSITIVE_INFINITY) {
                    // sprawdzamy czy problem będzie korzystniej rozwiązany
                    if (problems[p - coins[c].second].first + coins[c].first < problems[p].first){
                        // jak tak podmieniamy monetę i nominał uzyskany
                        problems[p].first = problems[p - coins[c].second].first + coins[c].first;
                        problems[p].second = c; // wrzucamy na drugą pozycję indeks korzystniejszej monety
                    }
                }
            }
        }
    }
}

void countCoins(pair<int, int>* problems, int F, int* coinsCount, pair<int, int>* coins){
    int current = F;
    // przeglądamy monety i zwiększamy counter na danym indeksie
    while (current != 0) {
        int idx = problems[current].second; // indeks obecnej największej monety
        coinsCount[idx] += 1;
        current -= coins[idx].second; // odejmujemy wagę znalezionej monety, aby cofnąc się o jeden krok
    }
}

int main() {
    // ifstream infile;
    // infile.open("/Users/szymon/Documents/Studia-UWr/AiSD/coding/pracownie/pracC/test.txt");
    // waga ktorą chcemy dostać
    int F;
    // infile >> F;
    scanf("%d", &F);
    // monety na rynku
    int C;
    // infile >> C;
    scanf("%d", &C);

    pair<int, int>* coins = new pair<int, int>[C];

    for (int i = 0; i < C; i++){
        int p;
        int w;
        // infile >> p >> w;
        scanf("%d %d", &p, &w);
        coins[i] = make_pair(p, w);
    }

    // lista problemow do rozwiązania przez algorytm, szukanie odpowiednich monet dla dostępnych wag
    // problemy do rozwiązania są od 0 do F włącznie
    pair<int, int>* problems = new pair<int, int>[F + 1];

    int* coinsCount = new int[C];

    // rozwiązanie dla Min
    evaluateCoins(problems, F + 1, coins, C, false);

    // for (int i = 0; i <= F; ++i) {
    //     cout << "(" << problems[i].first << ", " << problems[i].second << ") ";
    // }

    // cout << "\n";
    if (problems[F].first == POSITIVE_INFINITY){
        printf("NIE\n");
        return 0;
    }else {
        printf("TAK\n");
        printf("%d\n", problems[F].first);
    }

    
    countCoins(problems, F, coinsCount, coins);
    
    // wypisanie wykorzystanych monet
    for (int i = 0; i < C; ++i) {
        printf("%d ", coinsCount[i]);
    }
    printf("\n");
    // rozwiązanie dla Max
     evaluateCoins(problems, F + 1, coins, C, true);
     printf("%d\n", problems[F].first);
    
    // reset coinsCount
    for (int i = 0; i < C; ++i){
        coinsCount[i] = 0;
    }

    countCoins(problems, F, coinsCount, coins);

    // wypisanie wykorzystanych monet
    for (int i = 0; i < C; ++i) {
        printf("%d ", coinsCount[i]);
    }

    delete[] coins;
    delete[] problems;
    delete[] coinsCount;

    return 0;
}