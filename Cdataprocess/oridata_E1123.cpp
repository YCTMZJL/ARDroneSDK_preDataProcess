#define  _CRT_SECURE_NO_WARNINGS 1
#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<fstream>
#include<sstream>
#include<string.h>
#include<string>
#define timeII  0.01
using namespace std;
int grouptime = 10;
int groupnum = grouptime / timeII;
int main()
{
	char filepath[1024];
	char readfilename1[1024];
	//char readfilename2[1024];
	char readfilename3[1024];
	char savefilename[1024];
	char tmp[1024];


	strcpy(filepath, "D:/result/res2/");
	strcpy(readfilename1, filepath);
	strcat(readfilename1, "fly_Jonny_mesures_20161118_204012_GyrosZ.csv"); //accX Gyros
	strcpy(readfilename3, filepath);
	strcat(readfilename3, "fly_Jonny_mesures_20161118_204012_timeInterval.csv");
	//strcpy(savefilename, filepath);
	//strcat(savefilename, "CMean_stable_Jonny_20161118_203114_accZ");//*/
	strcpy(savefilename, "newC_stable_Jonny_20161118_204012_GyrosZ");
	fstream fin1(readfilename1, ios::in);
	//fstream fin2(readfilename2, ios::in);
	fstream fin3(readfilename3, ios::in);

	vector<double> oridata;
	vector<double> timeInv;
	//TotaltimeInv
	vector<double> Totaltime;
	double dataline;
	//double timeline;
	double totaltimeline;
	float timeInvE = 0.001;//from 0.001
	float curtimeE = 0.001;//from 0.001
	double predataline;
	double totoltimesum = 0;
	//double pretotaltimeline;
	fin1 >> predataline;
	//fin3 >> totaltimeline;
	//totoltimesum = totaltimeline;
	while (fin1 >> dataline && fin3 >> totaltimeline)//(fin1 >> dataline && fin2 >> timeline && fin3 >> totaltimeline)
	{
		//cout << dataline <<" " <<totaltimeline << endl;
		//cout <<" totaltimeline "<< totaltimeline << endl;
		totaltimeline += totoltimesum;
		//cout << " totoltimesum " << totaltimeline << endl;
		while (totaltimeline > curtimeE)
		{
			oridata.push_back(predataline);
			timeInv.push_back(timeInvE);
			Totaltime.push_back(curtimeE);
			curtimeE = curtimeE + timeInvE;
		}
		totoltimesum = totaltimeline;
		predataline = dataline;
	}
	if (oridata.size() == 0 || timeInv.size() == 0)
	{
		cout << "no file" << endl;
		system("pause");
		return 0;
	}

		char savefilename1[1024];
		char plt[1024];
		strcpy(savefilename1, filepath);
		strcat(savefilename1, savefilename);
		sprintf(plt, "%s.plt", savefilename1);
		sprintf(savefilename1, "%s.txt", savefilename1);
		fstream fout(savefilename1, ios::out);
		fstream fpltout(plt, ios::out);
		fpltout << "set xlabel \"Time\"" << endl;
		fpltout << "set ylabel \"mean\"" << endl;
		fpltout << "plot \"" << savefilename << ".txt\"with lines title \"" << savefilename << "\"" << endl;
		fpltout << "pause 3600" << endl;
		for (int i = 0; i < Totaltime.size(); i++)
			fout << Totaltime[i] << " " << oridata[i] << endl;

	
	system("pause");
	return 0;
}