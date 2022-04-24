package ie.wit.lamenessdetection.ui.dashboard

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.webkit.CookieManager
import android.webkit.WebView
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import ie.wit.lamenessdetection.R
import ie.wit.lamenessdetection.databinding.FragmentDashboardBinding

class DashboardFragment : Fragment() {

    private lateinit var dashboardViewModel: DashboardViewModel
    private var _binding: FragmentDashboardBinding? = null

    // This property is only valid between onCreateView and
    // onDestroyView.
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        dashboardViewModel =
            ViewModelProvider(this).get(DashboardViewModel::class.java)

        _binding = FragmentDashboardBinding.inflate(inflater, container, false)
        val root: View = binding.root


        return root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val myWebView: WebView = view.findViewById(R.id.webView)
        val myWebView2: WebView = view.findViewById(R.id.webView2)
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

        myWebView2.settings.javaScriptEnabled = true
        myWebView2.settings.loadWithOverviewMode = true
        myWebView2.settings.loadsImagesAutomatically = true
        myWebView2.settings.useWideViewPort = true
        myWebView2.settings.allowFileAccess = true
        myWebView2.settings.allowContentAccess = true
        myWebView2.settings.setAppCacheEnabled(true)
        myWebView2.settings.javaScriptCanOpenWindowsAutomatically = true
        myWebView2.settings.userAgentString = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Safari/537.36")

        CookieManager.getInstance().setAcceptCookie(true)
        CookieManager.getInstance().acceptThirdPartyCookies(myWebView)
        CookieManager.getInstance().acceptThirdPartyCookies(myWebView2)

        val path =
            "<iframe src=\"http://ec2-54-74-124-135.eu-west-1.compute.amazonaws.com:3000/d-solo/RjpRrtw7k/herd-dashboard?orgId=1&from=1650712856279&to=1650756056279&panelId=4\" width=\"1200\" height=\"600\" frameborder=\"0\"></iframe>"
        val path2 =
            "<iframe src=\"http://ec2-54-74-124-135.eu-west-1.compute.amazonaws.com:3000/d-solo/RjpRrtw7k/herd-dashboard?orgId=1&from=1650712856279&to=1650756056279&panelId=4\" width=\"1200\" height=\"600\" frameborder=\"0\"></iframe>"

        myWebView.loadData(path, "text/html", "utf-8")
        myWebView2.loadData(path2, "text/html", "utf-8")
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}