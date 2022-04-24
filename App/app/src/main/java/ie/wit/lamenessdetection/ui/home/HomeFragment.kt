package ie.wit.lamenessdetection.ui.home

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.webkit.CookieManager
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import ie.wit.lamenessdetection.R
import ie.wit.lamenessdetection.databinding.FragmentHomeBinding


class HomeFragment : Fragment() {

    private lateinit var homeViewModel: HomeViewModel
    private var _binding: FragmentHomeBinding? = null

    // This property is only valid between onCreateView and
    // onDestroyView.
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        homeViewModel =
            ViewModelProvider(this).get(HomeViewModel::class.java)

        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        val root: View = binding.root

        val textView: TextView = binding.textHome
        homeViewModel.text.observe(viewLifecycleOwner, Observer {
            textView.text = it
        })

        return root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val myWebView: WebView = view.findViewById(R.id.WebView1)
//        myWebView.webViewClient = object : WebViewClient() {
//            override fun shouldOverrideUrlLoading(
//                view: WebView,
//                url: String
//            ): Boolean {
//                view.loadUrl(url)
//                return true
//            }
//        }

//        myWebView.loadUrl("http://ec2-54-74-124-135.eu-west-1.compute.amazonaws.com:3000/d/RjpRrtw7k/herd-dashboard?orgId=1&from=1650683132401&to=1650726332401&viewPanel=4")
        myWebView.settings.javaScriptEnabled = true
        myWebView.settings.loadWithOverviewMode = true
        myWebView.settings.loadsImagesAutomatically = true
        myWebView.settings.useWideViewPort = true
        myWebView.settings.allowFileAccess = true
        myWebView.settings.allowContentAccess = true
        myWebView.settings.setAppCacheEnabled(true)
        myWebView.settings.javaScriptCanOpenWindowsAutomatically = true
        myWebView.settings.userAgentString = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Safari/537.36")
        //myWebView.webChromeClient = WebChromeClient()

        CookieManager.getInstance().setAcceptCookie(true)
        CookieManager.getInstance().acceptThirdPartyCookies(myWebView)

        val path =
            "<iframe src=\"http://ec2-54-74-124-135.eu-west-1.compute.amazonaws.com:3000/d-solo/RjpRrtw7k/herd-dashboard?orgId=1&from=1650712856279&to=1650756056279&panelId=4\" width=\"1200\" height=\"600\" frameborder=\"0\"></iframe>"
        myWebView.loadData(path, "text/html", "utf-8")
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}