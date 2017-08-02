This python script downloads papers from the CVPR open access website and creates first
page montages of the papers by search term. This query term is searched in the titles of the papers,
and their first pages are used to make four-paper montages of all the papers that match your interest.

You can thus, at a glance check through pertinent papers for your topic of interest from the hundreds
of papers at CVPR.

Code modified from Anrej Karpathy's Arxiv Sanity preserver 
(https://github.com/karpathy/arxiv-sanity-preserver), 
and the name CVPR Sanity Preserver is a homage to his work.

Jay Chakravarty
(pchakra5@ford.com)
August 2017.

Some required dependencies:

python3
urllib
beautifulSoup
