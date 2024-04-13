#include <iostream>
#include <utility>
#include <algorithm>
#include <stack>
// #include <fstream>

// funkcja do znajdowanie indexow obu dzieci danego wierzchołka, znajduje wierzchołek 'najbardziej na lewo'
int binSearch(std::pair<int, int> graph[], int v, int n){
    int l = 0;
    int r = n - 2;
    while (l <= r){
        int mid = (l + r) / 2;
        // dostajemy indeksy dzieci (albo dwoch, albo pojedynczych)
        if (graph[mid].first == v) {
            if (graph[mid - 1].first == v){
                r = mid - 1;
            }else {
                return mid;
            }
        }
        else if (graph[mid].first < v){
            l = mid + 1;
        }
        else {
            r = mid - 1;
        }
    }
    return -1;
}


void dfs(std::pair<int, int> times[], std::pair<int, int> graph[], int n){
    
    int time = 0;

    std::stack<int> stack;
    stack.push(1);

    while (!stack.empty()) {

        int s = stack.top(); 
 
        if (times[s-1].first == -1) {
            time++;
            times[s-1].first = time; // wejście do pierwszego elementu
            // szukamy indexu rodzica
            // std::cout <<"stos " << s << std::endl;
            int edgeIdx = binSearch(graph, s, n);
            // std::cout <<"binsearch res " <<  edgeIdx << std::endl;
            if (edgeIdx != -1){
                int r = edgeIdx;
                while (graph[r].first == s && r < n - 1){
                    stack.push(graph[r].second);
                    r++;
                }
            }
        }else {
            time++;
            times[s - 1].second = time;
            stack.pop();
        }
    }
    
}


bool compare_pair( const std::pair<int,int> &pair1, const std::pair<int,int> &pair2)
{
    int result = 0;
    if ( (pair2.first > pair1.first)){result = 1;} 
    return result;
}


int main() {
    // normal input
    int n;
    int q;
    std::cin >> n >> q;
    // infile >> n >> q;

    int* mothers = new int[n - 1];
    // int mothers[n - 1];

    // matek jest o jedną mniej niz podane 'n'
    for (int i = 0; i < n - 1; i++){
        int input;
        std::cin >> input;
        // infile >> input;
        mothers[i] = input;
    }


    // graf przetrzymujemy w postaci listy krawędzi
    // skoro jest to drzewo to mamy n-1 krawędzi
    std::pair<int, int> *graph = new std::pair<int, int>[n-1];
    // std::pair<int, int> graph[(n-1)];
    for (int i = 0; i < n-1; i++){
        graph[i] = std::make_pair(mothers[i], i + 2);
    }
    
    std::sort(graph, graph+(n-1), &compare_pair);



    std::pair<int, int> *times = new std::pair<int, int>[n];
    // std::pair<int, int> times[n];
    std::fill(times, times + n, std::make_pair(-1, -1));
    // for (int i = 0; i < n; ++i) {
    //     times[i] = std::make_pair(-1, -1);
    // }

    // for (int i = 0; i < n-1; ++i) {
    //     std::cout << "(" << graph[i].first << ", " << graph[i].second << ")" << std::endl;
    // }

    dfs(times, graph, n);

    // for (int i = 0; i < n; i++)
    // {
    //     std::cout << i+1 << " " << times[i].first << " " << times[i].second << std::endl;
    // }

    int i = 0;
    while (i < q){
        int a, b;
        std::cin >> a >> b;
        // infile >> a >> b;
        if (times[a - 1].first < times[b - 1].first && 
            times[a - 1].second > times[b - 1].second){
                std::cout << "TAK" << std::endl;
            }
        else {
        std::cout << "NIE" << std::endl;
    }
        i++;
    }


    // infile.close();

    return 0;
}