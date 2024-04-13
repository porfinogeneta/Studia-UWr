#include <stdio.h>
// #include <fstream>
#include <vector> 
#include <cmath>
#include <limits>
#include <algorithm>
using namespace std;

class Triangle {
    public:
        pair<int, int> a;
        pair<int, int> b;
        pair<int, int> c;
        double peri;

        Triangle(pair<int, int> p1, pair<int, int> p2, pair<int, int> p3){
            a = p1;
            b = p2;
            c = p3;
            peri = numeric_limits<double>::max();
        }
};

// odległość między punktami
double twoPointsDist(const pair<int, int> &a, const pair<int, int> &b){
    return sqrt(pow(a.first - b.first, 2) + pow(a.second - b.second, 2));
}

// obliczanie najkrotszego obwodu na końcu rekursji
// Triangle bruteForceTriangle(pair<int, int> points[], int n){
Triangle bruteForceTriangle(vector<pair<int, int> >& points, int n){
    if (n < 3){
        return Triangle(points[0], points[0], points[0]);
    }

    double perimeter = numeric_limits<double>::max();
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
                if (candidate < perimeter){
                    perimeter = candidate;
                    res = Triangle(points[i], points[j], points[k]);
                    res.peri = perimeter;
                }
            }
        }
    }

    return res;
}

// obliczanie najkrotszego obwodu w otoczeniu prostej
// Triangle stripTriangle(pair<int, int> ypoints[], int size){
Triangle stripTriangle(vector<pair<int, int> >& ypoints, int size){
    if (size < 3){
        return Triangle(ypoints[0], ypoints[0], ypoints[0]);
    }

    double perimeter = numeric_limits<double>::max();
    Triangle res(make_pair(0, 0), make_pair(0, 0), make_pair(0, 0));
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
                if (candidate < perimeter){
                    perimeter = candidate;
                    res = Triangle(ypoints[i], ypoints[j], ypoints[k]);
                    res.peri = perimeter;
                }
            }
        }
    }
    return res;
}

Triangle minTriangle(Triangle t1, Triangle t2){
    if (t1.peri < t2.peri){
        return t1;
    }else {
        return t2;
    }
}

// algorytm na obliczanie najkrotszego obwodu 
// Xpoints, posortowane po X, Ypoints analogicznie
// Triangle periMinTriangle(pair<int, int> Xpoints[], pair<int, int> Ypoints[], int n){
Triangle periMinTriangle(vector<pair<int, int> >& Xpoints, vector<pair<int, int> >& Ypoints){
    int n = (int)Xpoints.size();
    // przypadek bazowy
    if (n <= 3){
        return bruteForceTriangle(Xpoints, n);
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

    // pair<int, int> *YpointsCopy = new pair<int, int>[n];
    // for (int i = 0; i < n; i++) {
    //     YpointsCopy[i] = Ypoints[i];
    // }
    // // wskaźnik lewy i prawy
    // int l = 0, r = mid;
    // while (l < mid) {
    //     // szukamy elementu, ktory nie powinien być w Yl
    //     while (Ypoints[l].first <= midPoint.first && l < mid){
    //         l++;
    //     }
    //     // szukamy elementu, ktory nie powinien byc w Yr
    //     while (Ypoints[r].first >= midPoint.first && r < n){
    //         r++;
    //     }
    //     // znaleźliśmy elementy do zamiany
    //     if (l < mid){
    //         pair<int, int> temp = Ypoints[r];
    //         // wszystko na lewo od r trzeba przesunąć o 1 w prawo
    //         for (int i = r; i > mid; i--){
    //             Ypoints[i] = Ypoints[i-1];
    //         }
    //         // na początek wrzucamy element z l (na początek zeby było zachowane sortowanie po y)
    //         Ypoints[mid] = Ypoints[l];
    //         // wszystko na prawo od l trzeba przesunąć o 1 w lewo
    //         for (int i = l + 1; i < mid; i++){
    //             Ypoints[i-1] = Ypoints[i];
    //         }
    //         // na koniec wrzucamy element z r, zeby zachować sortowanie
    //         Ypoints[mid -1] = temp;
    //         l++;
    //         r++;

    //     }else {
    //         break;
    //     }
    // }

    // Triangle pL = periMinTriangle(Xpoints.begin(), Xpoints.begin() + mid, YpointsL);
    // Triangle pR = periMinTriangle(Xpoints.begin() + mid, Xpoints.end()          , YpointsR);
    
    Triangle pL = periMinTriangle(XpointsL, YpointsL);
    Triangle pR = periMinTriangle(XpointsR, YpointsR);



    // mniejszy trojkąt w partycjach
    Triangle pTriangle = minTriangle(pL, pR);

    // oblicznie otoczenia prostej
    // pair<int, int> strip[n];
    vector<pair<int, int> > strip;
    strip.reserve((int)Ypoints.size());
    for (int i = 0; i < (int)Ypoints.size(); i++){
        if (abs(Ypoints[i].first - midPoint.first) <= pTriangle.peri/2){
            strip.push_back(Ypoints[i]);
        }
    }
    // int j = 0;
    // for (int i = 0; i < n; i++){
    //     if (abs(YpointsCopy[i].first - midPoint.first) <= pTriangle.peri){
    //         strip[j] = YpointsCopy[i];
    //         j++;

    //     }
    // }

    // delete[] YpointsCopy;

    // najmnijszy trojkąt w otoczeniu prostej
    Triangle sTriangle = stripTriangle(strip, (int)strip.size());
    // Triangle sTriangle = stripTriangle(strip, j + 1);

    // porownanie obu trojkątow z partycji i otoczenia
    return minTriangle(pTriangle, sTriangle);


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

    // for (int i = 0; i < n; i++){
    //     cout << points[i].first << points[i].second << endl;
    // }
    vector<pair<int , int> > pointsY(points);
    // sortujemy po x i po y
    sort(points.begin(), points.end(), &comparePairX);
    sort(pointsY.begin(), pointsY.end(), &comparePairY);
    // Triangle res = bruteForceTriangle(points, n);
    // lista posortowane względem X
    
    // pair<int, int> Xpoints [n];
    // sort(points, points + n, &comparePairX);
    // copy(points, points + n, Xpoints);
    // sort(points, points + n, &comparePairY);
    
    Triangle res = periMinTriangle(points, pointsY);

    printf("%d %d\n", res.a.first, res.a.second);
    printf("%d %d\n", res.b.first, res.b.second);
    printf("%d %d\n", res.c.first, res.c.second);
    

    return 0;
}