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
float grouptime = 10;
int groupnum = (int)(grouptime*1.0 / timeII);

int main()
{
	cout << groupnum << endl;
	char filepath[1024];
	char readfilename1[1024];
	char readfilename2[1024];
	char readfilename3[1024];
	char savefilename[1024];
	char tmp[1024];

	strcpy(filepath, "D:/result/res1/");
	strcpy(readfilename1, filepath);
	strcat(readfilename1, "center_CMean_stable_Jonny_20161118_203114_1000GyrosX_1.txt"); //Gyros
	strcpy(readfilename2, filepath);
	strcat(readfilename2, "stable_Jonny_20161118_203114_timeInterval.csv");//*/
	
	strcpy(savefilename, "CDelta_center_CMean_stable_Jonny_20161118_203114_1000GyrosX");
	fstream fin1(readfilename1, ios::in);
	fstream fin2(readfilename2, ios::in);
	//fstream fin3(readfilename3, ios::in);

	vector<double> oridata;
	vector<double> timeInv;
	//TotaltimeInv
	vector<double> Totaltime;
	double dataline;
	double timeline;
	double totaltimeline;
	double timesum = 0;
	double timetmp;
	while (fin1 >> dataline && fin2 >> timeline)
	{
		//cout << dataline << timeline << endl;
		fin1 >> dataline;
		timesum += timeline;
		oridata.push_back(dataline);
		timeInv.push_back(timeline);
		Totaltime.push_back(timesum);
	}
	if (oridata.size() == 0 || timeInv.size() == 0)
	{
		cout << "no file" << endl;
		system("pause");
		return 0;
	}
	int T = 1;
	//cout << "times£º";
	//cin >> T;
	int countt = 0;
	if (oridata.size() < groupnum)
	{
		cout << "window is too large" << endl;
		system("pause");
		return 0;
	}
	while (T--)
	{
		countt++;
		char savefilename1[1024];
		char plt[1024];
		strcpy(savefilename1, filepath);
		strcat(savefilename1, savefilename);
		sprintf(plt, "%s_%d.plt", savefilename1, countt);
		sprintf(savefilename1, "%s_%d.txt", savefilename1, countt);
		fstream fout(savefilename1, ios::out);
		fstream fpltout(plt, ios::out);
		fpltout << "set xlabel \"Time\"" << endl;
		fpltout << "set ylabel \"mean\"" << endl;
		fpltout << "plot \"" << savefilename << "_" << countt << ".txt\"with lines title \"" << savefilename << "\"" << endl;
		fpltout << "pause 3600" << endl;
		double sumdata = 0;// oridata[0] * timeInv[0];
		double sumtime = 0;// timeInv[0];
		vector<double> meandata(oridata.size());

		fout << Totaltime[0] << " " << 0 << endl;
		for (int i = 1; i < oridata.size(); i++)
		{
			fout << Totaltime[i] << " " << oridata[i]-oridata[i-1] << endl; 
		}

	}
	system("pause");
	return 0;
}