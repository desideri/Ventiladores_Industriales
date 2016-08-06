package com.example.kattyadesiderio.wilencoapp;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;

import java.util.ArrayList;

/**
 * Created by Kattya Desiderio on 05/08/2016.
 */
public class ViewPagerAdapter extends FragmentPagerAdapter {

    private ArrayList<Fragment> mfraglist = new ArrayList<>();
    private ArrayList<String> mfragtitles = new ArrayList<>();


    public ViewPagerAdapter(FragmentManager fm) {
        super(fm);
    }

    @Override
    public Fragment getItem(int position) {
        return mfraglist.get(position);
    }

    @Override
    public int getCount() {
        return mfraglist.size();
    }

    public void addFragment(Fragment fragment,String title){
        mfraglist.add(fragment);
        mfragtitles.add(title);
    }

    @Override
    public CharSequence getPageTitle(int position) {
        return mfragtitles.get(position);
    }
}

