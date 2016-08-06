package com.example.kattyadesiderio.wilencoapp.fragments;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.example.kattyadesiderio.wilencoapp.R;


public class FragmentOne extends Fragment{

    public static final String ARGS_SAMPLE="this_is_a_content";
    private String example_data;
    public FragmentOne(){

    }

    public static FragmentOne newInstance(String sample_argument){
        FragmentOne oneFragment = new FragmentOne();
        Bundle args = new Bundle();
        args.putString(ARGS_SAMPLE,sample_argument);
        oneFragment.setArguments(args);
        return oneFragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        example_data=getArguments().getString(ARGS_SAMPLE);
        Log.i("fragments",example_data);
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {

        return inflater.inflate(R.layout.fragment_one,container,false);
    }
}
