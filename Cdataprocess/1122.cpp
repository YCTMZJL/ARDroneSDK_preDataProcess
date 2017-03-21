#define  _CRT_SECURE_NO_WARNINGS 1
#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<fstream>
#include<sstream>
#include<string.h>
#include<string>
using namespace std;
int groupnum = 10;
int main()
{
	char filepath[1024];
	char readfilename1[1024];
	char readfilename2[1024];
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
	strcat(readfilename1,"Mean_stable_Jonny_20161118_203114_accX.csv");
	strcpy(readfilename2, filepath);
	strcat(readfilename2, "stable_Jonny_20161118_203114_timeInterval.csv");//*/
	//strcpy(savefilename, filepath);
	//strcat(savefilename, "CMean_stable_Jonny_20161118_203114_accZ");//*/
	strcpy(savefilename, "CMean_stable_Jonny_20161118_203114_accX");
	fstream fin1(readfilename1,ios::in);
	fstream fin2(readfilename2, ios::in);
	
	vector<double> oridata;
	vector<double> timeInv;
	double dataline;
	double timeline;
	while (fin1 >> dataline && fin2 >> timeline)
	{
		//cout << dataline << timeline << endl;
		oridata.push_back(dataline);
		timeInv.push_back(timeline);
	}
	if (oridata.size() == 0 || timeInv.size() == 0)
	{
		cout << "no file" << endl;
		system("pause");
		return 0;
	}
	int T = 1;
	cout << "times£º";
	cin >> T;
	int countt = 0;
	while (T--)
	{
		countt++;
		char savefilename1[1024];
		char plt[1024];
		strcpy(savefilename1, filepath);
		strcat(savefilename1,savefilename);
		sprintf(plt, "%s_%d.plt", savefilename1, countt);
		sprintf(savefilename1, "%s_%d.csv", savefilename1, countt);
		fstream fout(savefilename1, ios::out);
		fstream fpltout(plt, ios::out);
		fpltout << "set xlabel \"NUM\"" << endl;
		fpltout << "set ylabel \"mean\"" << endl;
		fpltout << "plot \"" << savefilename<<"_"<<countt<<".csv\"with lines title \"" << savefilename <<"\"" <<endl;
		fpltout << "pause 3600" << endl;
		double sumdata = oridata[0] * timeInv[0];
		double sumtime = timeInv[0];
		vector<double> meandata(oridata.size());
		double pre = oridata[0];
		if (sumtime == 0) fout << oridata[0] << endl;
		else
		{
			pre = sumdata / sumtime;
			fout << pre << endl;
		}
		meandata[0] = pre;
		for (int i = 1; i < oridata.size(); i++)
		{
			if (i > groupnum)
			{
				sumdata -= oridata[i - groupnum] * timeInv[i - groupnum];
				sumtime -= timeInv[i - groupnum];
			}
			sumdata += oridata[i] * timeInv[i];
			sumtime += timeInv[i];
			if (sumtime == 0)
			{
				fout << pre << endl; cout << "invalid" << endl;
			}
			else
			{
				pre = sumdata / sumtime;
				fout << pre << endl;
			}
			//cout << pre << endl;
			meandata[i] = pre;
		}

	}
	system("pause");
	return 0;
}