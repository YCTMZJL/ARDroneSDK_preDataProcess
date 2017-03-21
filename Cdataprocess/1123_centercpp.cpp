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
	//char curname[1024];
	/*cout << "path: ";
	cin >> filepath;
	//strcpy(filepath, "/");
	cout << "datafile name: ";
	strcpy(readfilename1, filepath);
	cin >> tmp;
	//cout << readfilename1 << endl;
	//sprintf(readfilename1, "%s/%s", filepath, readfilename1);
	//cout << readfilename1 << endl;
	strcat(readfilename1, tmp);
	cout << "timeInvfile name: ";
	cin >> tmp;
	strcpy(readfilename2, filepath);
	strcat(readfilename2, tmp);//*/
	//sprintf(readfilename2, "%s/%s", filepath, readfilename2);

	strcpy(filepath, "D:/result/res1/");
	strcpy(readfilename1, filepath);
	strcat(readfilename1, "stable_Jonny_20161118_203114_accX.csv"); //Gyros
	strcpy(readfilename2, filepath);
	strcat(readfilename2, "stable_Jonny_20161118_203114_timeInterval.csv");//*/
	//strcpy(readfilename3, filepath);
	//strcat(readfilename3, "TotalTime_stable_Jonny_20161118_203114_timeInterval.csv");
	//strcpy(savefilename, filepath);
	//strcat(savefilename, "CMean_stable_Jonny_20161118_203114_accZ");//*/
	strcpy(savefilename, "center_CMean_stable_Jonny_20161118_203114_1000accX");
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
	while (fin1 >> dataline && fin2 >> timeline)
	{
		//cout << dataline << timeline << endl;
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
		
		double pre = oridata[0];
		for (int i = 0; i <= groupnum / 2; i++)
		{
			sumdata += oridata[i] * timeInv[i];
			sumtime += timeInv[i];
		}
		if (sumtime == 0) fout << Totaltime[0] << " " << oridata[0] << endl;
		else
		{
			pre = sumdata / sumtime;
			fout << Totaltime[0] << " " << pre << endl;
		}
		meandata[0] = pre;
		for (int i = 1; i < oridata.size(); i++)
		{
			if (i + groupnum /2 > groupnum)
			{
				sumdata -= oridata[i - groupnum/2] * timeInv[i - groupnum/2];
				sumtime -= timeInv[i - groupnum/2];
			}
			if (i + groupnum / 2 < oridata.size())
			{
				sumdata += oridata[i + groupnum / 2] * timeInv[i + groupnum / 2];
				sumtime += timeInv[i + groupnum / 2];
			}
			if (sumtime == 0)
			{
				fout << Totaltime[i] << " " << pre << endl; cout << "invalid" << endl;
			}
			else
			{
				pre = sumdata / sumtime;
				fout << Totaltime[i] << " " << pre << endl;
			}
			//cout << pre << endl;
			meandata[i] = pre;
		}

	}
	system("pause");
	return 0;
}