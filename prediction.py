#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

import os
import csv

def estimated_price(mileage, theta0, theta1):
	return float(theta0 + (theta1 * mileage));

def get_thetas_in_csv():
	file = open("thetas.csv");
	line = file.readline();
	table = line.split(",");
	table[0] = float(table[0]);
	table[1] = float(table[1]); 
	return table;

def main():
	[theta0, theta1] = get_thetas_in_csv();
	mileage = 0;
	while (mileage <= 0):
		mileage = input("Saisissez un Kilomètrage pour estimer le prix de votre voiture : ")
		try:
			mileage = int(mileage);
		except:
			print("Vous n'avez pas saisi un kilmètrage valide. Merci de réessayer.");
			mileage = 0;
		if (mileage < 0):
			print("Ce Kilomètrage est inferieur à 0. Merci de réessayer.");
	price = estimated_price(mileage, theta0, theta1);
	print("L'estimation de votre voiture est de " + str(int(price)) + "$");

if __name__ == "__main__":
	main();