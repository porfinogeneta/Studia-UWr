#include <stdio.h>
// #include <fstream>
#include <vector> 
#include <cmath>
#include <limits>
#include <algorithm>
using namespace std;

// #define point pair<int, int>
// #define x first
// #define y second

class Triangle {
    public:
        pair<int, int> a;
        pair<int, int> b;
        pair<int, int> c;
        // double peri;

        Triangle(pair<int, int> p1, pair<int, int> p2, pair<int, int> p3){
            a = p1;
            b = p2;
            c = p3;
            // peri = numeric_limits<double>::max();
        }
};

double peri = numeric_limits<double>::max();
Triangle resTriangle(make_pair(0, 0), make_pair(0, 0), make_pair(0, 0));

// odległość między punktami
double twoPointsDist(const pair<int, int> &a, const pair<int, int> &b){
    return sqrt(pow(a.first - b.first, 2) + pow(a.second - b.second, 2));
}

// obliczanie najkrotszego obwodu na końcu rekursji
// Triangle bruteForceTriangle(pair<int, int> points[], int n){
void bruteForceTriangle(vector<pair<int, int> >& points, int n){
    if (n < 3){
        return;
    }

    // double perimeter = numeric_limits<double>::max();
    Triangle res(make_pair(0, 0), make_pair(0, 0), make_pair(0, 0));
    // generujemy wszystkie trojkąty i liczmy obwody
    for (int i = 0; i < n; i++){
        for (int j = i+1; j < n; j++){
            for (int k = j+1; k < n; k++){
                double candidate = 0;
                double side1 = twoPointsDist(points[i], points[j]);
                double side2 = twoPointsDist(points[i], points[k]);
                double side3 = twoPointsDist(points[j], points[k]);
                candidate = side1 + side2 + side3;
                // aktualizujemy obwod i wynikowy trojkąt
                if (candidate < peri){
                    peri = candidate;
                    // peri = candidate
                    resTriangle.a = points[i];
                    resTriangle.b = points[j];
                    resTriangle.c = points[k];
                    //  = Triangle(points[i], points[j], points[k]);
                    // res.peri = perimeter;
                }
            }
        }
    }

    return;
}

// obliczanie najkrotszego obwodu w otoczeniu prostej
// Triangle stripTriangle(pair<int, int> ypoints[], int size){
void stripTriangle(vector<pair<int, int> >& ypoints, int size){
    if (size < 3){
        return;
    }

    // double perimeter = numeric_limits<double>::max();
    // Triangle res(make_pair(0, 0), make_pair(0, 0), make_pair(0, 0));
    // maksymalnie 16 punktow dla kazdego punktu do sprawdzenia
    for (int i = 0; i < size; i++){
        for (int j = i+1; j < i + 16 && j < size; j++){
            for (int k = j+1; k < i + 16 && k < size; k++){
                double candidate = 0;
                double side1 = twoPointsDist(ypoints[i], ypoints[j]);
                double side2 = twoPointsDist(ypoints[i], ypoints[k]);
                double side3 = twoPointsDist(ypoints[j], ypoints[k]);
                candidate = side1 + side2 + side3;
                // aktualizujemy obwod i wynikowy trojkąt
                if (candidate < peri){
                    peri = candidate;
                    // res = Triangle(ypoints[i], ypoints[j], ypoints[k]);
                    resTriangle.a = ypoints[i];
                    resTriangle.b = ypoints[j];
                    resTriangle.c = ypoints[k];
                    // res.peri = perimeter;
                }
            }
        }
    }
    return;
}

// Triangle minTriangle(Triangle t1, Triangle t2){
//     if (t1.peri < t2.peri){
//         return t1;
//     }else {
//         return t2;
//     }
// }

// algorytm na obliczanie najkrotszego obwodu 
void periMinTriangle(vector<pair<int, int> >& Xpoints, vector<pair<int, int> >& Ypoints){
    int n = (int)Xpoints.size();
    // przypadek bazowy
    if (n <= 18){
        bruteForceTriangle(Xpoints, n);
        return;
    }

    // obliczanie lewej i prawej strony
    int mid = n/2;
    pair<int, int> midPoint = Xpoints[mid];
    // posortowane połowy X, ktore wrzucimy do wywołań rekurencyjnych
    vector<pair<int ,int> > XpointsL(Xpoints.begin(), Xpoints.begin() + mid);
    vector<pair<int, int> > XpointsR(Xpoints.begin() + mid, Xpoints.end());


    vector<pair<int, int> > YpointsL;
    vector<pair<int, int> > YpointsR;
    YpointsL.reserve((int)Ypoints.size());
    YpointsR.reserve((int)Ypoints.size());


    for (int i = 0; i < (int)Ypoints.size(); i++) {
        if (Ypoints[i].first <= midPoint.first) {
            YpointsL.push_back(Ypoints[i]);
        }
        else {
            YpointsR.push_back(Ypoints[i]);
        }
    }

    
    // Triangle PL = periMinTriangle(XpointsL, YpointsL);
    // Triangle PR = periMinTriangle(XpointsR, YpointsR);

    periMinTriangle(XpointsL, YpointsL);
    periMinTriangle(XpointsR, YpointsR);




    // mniejszy trojkąt w partycjach
    // double minPTriangle = minPTriangle(PL, PR);

    // oblicznie otoczenia prostej
    vector<pair<int, int> > strip;
    strip.reserve((int)Ypoints.size());
    for (int i = 0; i < (int)Ypoints.size(); i++){
        if (abs(Ypoints[i].first - midPoint.first) <= peri/2){
            strip.push_back(Ypoints[i]);
        }
    }

    // najmnijszy trojkąt w otoczeniu prostej
    // double sPeriTriangle = stripTriangle(strip, (int)strip.size());
    stripTriangle(strip, (int)strip.size());
    // Triangle sTriangle = stripTriangle(strip, j + 1);

    // porownanie obu trojkątow z partycji i otoczenia
    // return minTriangle(pTriangle, sTriangle);
    // return min(minPTriangle, sPeriTriangle);
    return;


}


bool comparePairX(pair<int, int> &p1, pair<int, int> &p2){
        if (p1.first < p2.first){return 1;}else {return 0;}
}

bool comparePairY(pair<int, int> &p1, pair<int, int> &p2){
        if (p1.second < p2.second) {return 1;} else {return 0;}
}



int main() {
    // ifstream infile;
    // infile.open("/Users/szymon/Documents/Studia-UWr/AiSD/coding/pracownie/pracB/test.txt");
    int n;
    // infile >> n;
    scanf("%d", &n);

    // pair<int, int> *points = new pair<int, int>[n];
    vector<pair<int , int> > points(n);
    points.reserve(n);
    for (int i = 0; i < n; i++){
        int x;
        int y;
        // infile >> x >> y;
        scanf("%d %d", &x, &y);
        points[i] = make_pair(x, y);
        // points[i] = make_pair(x, y);
    }

    vector<pair<int , int> > pointsY(points);
    // sortujemy po x i po y
    sort(points.begin(), points.end(), &comparePairX);
    sort(pointsY.begin(), pointsY.end(), &comparePairY);
    
    
    // double res = periMinTriangle(points, pointsY);
    periMinTriangle(points, pointsY);

    printf("%d %d\n", resTriangle.a.first, resTriangle.a.second);
    printf("%d %d\n", resTriangle.b.first, resTriangle.b.second);
    printf("%d %d\n", resTriangle.c.first, resTriangle.c.second);
    

    return 0;
}