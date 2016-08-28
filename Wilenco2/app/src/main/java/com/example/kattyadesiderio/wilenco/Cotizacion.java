package com.example.kattyadesiderio.wilenco;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebView;

public class Cotizacion extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cotizacion);

        WebView view = (WebView)this.findViewById(R.id.Cotizaciones);
        String url = "http://wilenco.tk/cotizacion/";
        view.loadUrl(url);
    }
}
