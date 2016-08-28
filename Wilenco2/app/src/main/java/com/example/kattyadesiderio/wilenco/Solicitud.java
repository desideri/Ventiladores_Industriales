package com.example.kattyadesiderio.wilenco;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebView;

public class Solicitud extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_solicitud);


        WebView view = (WebView)this.findViewById(R.id.Solicitudes);
        String url = "http://wilenco.tk/servicio/";
        view.loadUrl(url);
    }
}
