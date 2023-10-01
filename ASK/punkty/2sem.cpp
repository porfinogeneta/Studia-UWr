#include <iostream>
#include <map>

const std::map<double, double> progi_ask = {
	{3.0, 50},
	{3.5, 60},
	{4, 70},
	{4.5, 80},
	{5, 90}};

const std::map<double, double> progi_mp = {
	{3.0, 50},
	{3.5, 59},
	{4, 68},
	{4.5, 77},
	{5, 86}};

const std::map<double, double> progi_algebra = {
	{3.0, 40},
	{3.5, 55},
	{4, 65},
	{4.5, 75},
	{5, 85}};

int main()
{
	// ASK
	std::cout << "Architektury Systemów Kompterowych\n";
	double punkty_ask;
	std::cout << "Punktów razem: ";
	std::cin >> punkty_ask;
	for (const auto &el : progi_ask)
	{
		std::cout << "Do " << el.first << " brakuje " << std::max(0.0, 2 * el.second - punkty_ask) << " punktów\n";
	}

	std::cout << "\nMetody programowania\n";
	double punkty_mp_cwicz, punkty_mp_prac;
	std::cout << "Punktów za ćwiczenia: ";
	std::cin >> punkty_mp_cwicz;
	std::cout << "Punktów za pracownie: ";
	std::cin >> punkty_mp_prac;
	for (const auto &el : progi_mp)
	{
		std::cout << "Do " << el.first << " brakuje " << std::max(0.0, 28.0 / 25.0 * (3 * el.second - 5 * punkty_mp_prac) - punkty_mp_cwicz) << " punktów (z ćwiczeń)\n";
	}

	std::cout << "\nAlgebra\n";
	double punkty_algebra_cwicz, punkty_algebra_zdom;
	std::cout << "Punktów za ćwiczenia: ";
	std::cin >> punkty_algebra_cwicz;
	std::cout << "Punktów za zadania domowe: ";
	std::cin >> punkty_algebra_zdom;
	for (const auto &el : progi_algebra)
	{
		std::cout << "Do " << el.first << " brakuje " << std::max(0.0, 5.0 / 4.0 * el.second - punkty_algebra_cwicz - punkty_algebra_zdom / 8) << " punktów (z ćwiczeń)\n";
	}

	return 0;
}