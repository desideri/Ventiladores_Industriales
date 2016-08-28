package com.example.kattyadesiderio.wilenco;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebView;

public class Web extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_web);

        WebView view = (WebView)this.findViewById(R.id.Web);
        String url = "http://wilenco.tk/";
        view.loadUrl(url);
    }
}
