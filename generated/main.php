<?php

class WebScraper {
    private $url;
    private $userAgent;
    private $curlOptions;

    public function __construct($url, $userAgent = 'Mozilla/5.0') {
        $this->url = $url;
        $this->userAgent = $userAgent;
        $this->curlOptions = array(
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HEADER => false,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_ENCODING => '',
            CURLOPT_USERAGENT => $this->userAgent,
            CURLOPT_AUTOREFERER => true,
            CURLOPT_CONNECTTIMEOUT => 30,
            CURLOPT_TIMEOUT => 30,
            CURLOPT_MAXREDIRS => 10,
        );
    }

    public function scrape() {
        $ch = curl_init($this->url);
        curl_setopt_array($ch, $this->curlOptions);
        $content = curl_exec($ch);
        $err = curl_errno($ch);
        $errmsg = curl_error($ch);
        $header = curl_getinfo($ch);
        curl_close($ch);
        return array($content, $header, $err, $errmsg);
    }

    public function parseHtml($html) {
        $dom = new DOMDocument();
        libxml_use_internal_errors(true);
        $dom->loadHTML($html);
        libxml_clear_errors();
        return $dom;
    }

    public function getData($dom, $selector) {
        $xpath = new DOMXPath($dom);
        $data = $xpath->query($selector);
        return $data;
    }
}

function main() {
    $url = 'https://example.com';
    $scraper = new WebScraper($url);
    list($html, $header, $err, $errmsg) = $scraper->scrape();
    $dom = $scraper->parseHtml($html);
    $selector = '//h1';
    $data = $scraper->getData($dom, $selector);
    foreach ($data as $node) {
        echo $node->nodeValue . "\n";
    }
}

main();

?>
