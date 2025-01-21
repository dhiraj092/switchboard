# [Playing the Peak Pricing Game with AI and a Nudge | Smith Business Insight](https://smith.queensu.ca/insight/content/Playing-the-Peak-Pricing-Game-with-AI-and-a-Nudge.php) 
 _https://smith.queensu.ca/insight/content/Playing-the-Peak-Pricing-Game-with-AI-and-a-Nudge.php_

**Driven by altruism,** the desire for a competitive edge or, more likely, t    he need to control costs, Canada’s biggest energy-guzzling companies spend a lot of time and money trying to reduce their carbon footprint. They retrofit equipment for greater efficiency. They hunt for low-carbon sources of raw materials. They use [swarm intelligence](https://en.wikipedia.org/wiki/Swarm_intelligence) to optimize schedules. They tweak product packaging and logistics. Just about every incremental improvement in energy efficiency trickles down to the bottom line and builds energy resilience.
For these firms on the hunt for new ideas, a [recently completed study](https://www.youtube.com/watch?v=h2Cw59ZoA4E) should pique plenty of interest. The novel boundary-spanning study used two types of power tools that are rarely mentioned in the same breath: artificial intelligence and behavioural nudging. By optimizing both algorithms and human psychology, the researchers discovered a promising way to even out the huge demand surges that occasionally hit electrical grids and cost industry so much money. Corporate sustainability executives and policymakers take notice.
## **Anticipating electricity premiums**
The story begins in Ontario with a familiar energy-saving policy: [critical peak pricing](https://www.energysage.com/electricity/critical-peak-pricing-overview/) (CPP). CPP is a form of dynamic pricing employed by many jurisdictions in North America and Europe that involves charging very high electrical prices to households and businesses during a select number of peak periods. The motivation is to reduce the risk of blackouts or utilities drawing on coal or gas for backup power. 
All electricity customers in Ontario pay a so-called [Global Adjustment](https://www.ieso.ca/Learn/Electricity-Pricing-Explained/Global-Adjustment), which covers the base cost of operating the electricity system. For jumbo “Class A” energy users — those that participate in the Industrial Conservation Initiative — consuming energy during peaks is extremely expensive, as their Global Adjustment is based on the [amount](https://www.ttpowergroup.com/guides/ontario-global-adjustment-fee) [of electricity they consumed](https://www.ttpowergroup.com/guides/ontario-global-adjustment-fee) during the peak five hours of energy demand over the year. Once the year is over, the peaks are identified, and the company is charged retroactively based on how much their consumption contributed to those five peaks multiplied by the entire province’s Global Adjustment.
Global Adjustment can add up to hundreds of thousands of dollars so big users have an incentive to mitigate their energy use during peak demand periods — perhaps shutting production lines, shifting employee schedules or using backup generators. The challenge, however, is that because the Global Adjustment is based on the entire year’s energy use, anticipating the five peak periods before they happen is like throwing darts while blindfolded. This gives rise to the most loathsome word in the corporate lexicon: uncertainty.
Making energy-saving production adjustments for just a few hours can be costly, and firms will resist making changes if there are too many false calls. Is there a better way to forecast the exact timing of demand peaks?
## **Critical peak pricing works** 
This is where the research team of Christopher Amaral of the University of Bath, Ceren Kolsarici and Nicole Robitaille of Smith School of Business and Iina Ikonen of the University of Groningen enter the story. Team members have complementary backgrounds in marketing analytics, artificial intelligence and consumer behaviour. They came together to test a multidisciplinary approach to reduce organizations’ energy consumption in a demand pricing setting.
For data, the researchers partnered with the consulting company [En-Pro](https://www.en-pro.com/what-we-do.html), which advises large industrial and commercial businesses on their energy use. En-Pro forecasts long-range hourly provincial energy demand and alerts their clients to predicted peak demands when energy consumption should be cut back. The researchers accessed anonymized client-level information for 25 of the largest organizations across nine industries in Ontario, including hourly energy consumption at the location level and hourly energy demand and temperature for the entire province.
From their first analysis of the data, it was clear that Ontario’s critical peak pricing program was accomplishing what it was designed to do for Class A customers, even before the researchers applied their experiments using AI and nudging.
They found that when En-Pro accurately predicted an energy peak and sent a curtailment call to their clients in time for them to adjust, the customers, on average, decreased their contribution to provincial energy demand by 320 kWh per hour — comparable to the biweekly energy consumption of an average household in Ontario. This represented an average annual energy cost savings of $162,000 per organization. (Firms with a backup generator, which makes it easier to cut back energy use quickly, reduced their energy by 31 per cent compared to 19 per cent by firms without generators.)
##  **Tweaking temperature forecasts**
The next question was whether the research team could improve the accuracy of En-Pro’s state-of-the-art energy demand forecasts with AI. Using a neural network time series, a form of machine learning inspired by how biological networks function in animal brains, they built a long-range hourly forecasting model for the entire province.
Their neural network model delivered as promised: It was 100 per cent accurate in predicting peak energy demand, compared to the 56 per cent accuracy of the benchmark models. As a result, the researchers were able to wring another $41,000 of savings per organization.
More accurate forecasts also meant greater trust in the curtailment calls. As the researchers note, the Ontario government only uses the top five peaks in the year to calculate the CPP premium for each organization, so any additional curtailment call would be a false alarm. The AI-based forecast led to half the number of curtailment calls sent and only four false alarms (compared to 14 false alarms by the benchmark models).
“The number of false alarms are detrimental,” says Ceren Kolsarici, “because in the long-term, these excess curtailment calls reduce trust in the program, particularly since curtailing energy is costly for organizations.” 
## **Nudge in the right direction** 
Pleased by the success of their AI model, the research team in the summer of 2022 then turned to improving the curtailment emails that En-Pro sent to clients. These bare-bones notices (see example below, “Class A Daily Bulletin”) feature the peak energy demand forecast, a suggested four-hour curtailment window and suggestions for actions to take.
The researchers mocked up a new email notice based on behavioural economics principles. It has been well documented that seemingly small contextual factors, such as a simple message and planning prompts that communicate the when, where and how of potential actions, can “nudge” people toward a desired behaviour.
Most nudging research focuses on changing individual behaviour. But one of the researchers, Nicole Robitaille, showed [in a previous study](https://smith.queensu.ca/insight/content/research-brief-at-tax-time-a-little-nudge-goes-a-long-way.php) that planning prompts could be effective at changing tax compliance behaviour at an organizational level as well.
The research team revised the email’s subject line to be more descriptive, highlighted the timing of the curtailment call by enlarging it and added three pieces of advice to reduce energy consumption to make the “how” of the planning prompt more concrete (see revised “Curtailment call” email below).
Based on the predictions from the neural network, the team sent out nine curtailment calls to En-Pro’s clients over the summer, some with the nudge and planning prompts and others with standard messaging.
When they examined the results, the experimental emails outperformed the standard messaging. Clients in the experimental group contributed less to the provincial energy demand during curtailment calls compared to those in the control group. It resulted in a lower average contribution during the top five peaks in 2022 and, consequently, an additional average savings of $120,585 in energy costs.
Best of all, the effectiveness of the nudging email did not diminish over time, even across nine exposures spanning 75 days. The study is among the first to show the lasting effects of nudges aimed at organizations.
The Class A Daily Bulletin email (left) asks big commercial electricity users in Ontario to reduce energy consumption during peak demand periods. To improve its effectiveness, researchers redesigned the email (right) using nudging principles, including a stronger subject line, simplified messaging, visuals and key information in a larger type.
## **Benefits of the AI-nudge tag team**
The study’s results suggest that artificial intelligence and behavioural insights employed together improve the effectiveness of critical peak pricing by 99 per cent, measured by the incremental increase in cost savings.
For government policymakers, energy consultants and corporate sustainability experts, there is a lot to like about this study. The government and energy consultants can be satisfied that critical peak pricing is working, and that it can be made even more effective by using a multidisciplinary approach to reduce uncertainty (and by encouraging the use of backup generators). 
And Ontario’s biggest energy producers can be more confident to make short-term adjustments in their production processes knowing the investment will mean a smaller energy bill. This is significant considering energy demand peaks are becoming more random and unpredictable.
Kolsarici is clearly pleased by the big payoff from the two-year study. Every one-hour reduction of energy per client due to the team’s AI-nudging intervention was equivalent to roughly 22 days of average household consumption. Companies that were part of the study saw an average cost saving of $350,000.
“The results are even more impressive when you consider that the 25 companies that were part of the study were trained by En-Pro on how to reduce energy consumption and are highly motivated to improve their performance under critical peak pricing,” she says. “This was a very challenging multi-stakeholder problem to address, but the impact has been outstanding for the clients and the environment.”
_This project was a finalist in the 2024 Gary L. Lilien ISMS Practice Prize, sponsored by the INFORMS Society for Marketing Science. View the research team’s presentation_ [_here_](https://www.youtube.com/watch?v=h2Cw59ZoA4E)_._
Tags:

# [Our Insight Topics | Smith Business Insight](https://smith.queensu.ca/insight/tag.php?tid=Social%20Impact) 
 _https://smith.queensu.ca/insight/tag.php?tid=Social%20Impact_

 Smith Business Insight - Our Insight Topics 
[Skip to main content](#main-content)
Smith  
* [About](#)
 
 [Smith Home](/index.php)[Profile](/about/index.php)[News](/news_blog/index.php)[The Dean](/about/dean.php)[Strategic Plan](/about/strategic-plan.php)[Equity, Diversity, Inclusion & Indigenization](/about/EDII/index.php)[Learning Environment](/about/learning_environment.php)[Partnerships](/about/partners/index.php) [Services](/about/services.php) [SmithStore _​_](http://smithqueens.com/smithstore) [Queen's University _​_](https://queensu.ca)
 
* [Learning](#)
 
 [Explore Our Programs](/academic_programs/index.php)[Undergraduate Programs](/academic_programs/undergraduate.php) [MBA Programs](/mba_programs/index.php) [Graduate Programs](/grad_studies/index.php) [Executive Education](/executiveeducation/index.php)[Certificates](/academic_programs/certificates.php)[International](/international/index.php)[SmithEdge](/smithedge/index.php)[Academic Integrity](/about/academic_integrity/index.php)
 
* [Insights & Research](#)
 
 [Smith Business Insight](/insight/index.php) [Research](/research/index.php) [Publications](/about/publications.php) [Centres](/centres/index.php)
 
* [Faculty](#)
 
 [Meet Our Faculty](/faculty_and_research/faculty.php) [Join Our Ranks](/faculty_and_research/Join_Our_Ranks.php)
 
* [Alumni & Giving](#)
 
 [Give to Smith](https://smith.queensu.ca/invest/) [Alumni](/alumni/index.php)
 
* [Recruit & Engage](#)
 
 [Recruiting](/recruiting/index.php) [Partnerships](/about/partners/index.php) [Work with Students](/engage/index.php) [Smith Business Consulting](/centres/business-consulting/index.php)
 
Fresh ideas from [Smith School of Business](/index.php)
* [Topics](#)
 
 ### Categories
 
 * [Leadership](/insight/sections.php?sid=Leadership)
 * [Teams](/insight/sections.php?sid=Teams)
 * [Diversity](/insight/sections.php?sid=Diversity)
 * [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
 * [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
 * [Social Impact](/insight/sections.php?sid=Social%20Impact)
 * [Marketing](/insight/sections.php?sid=Marketing)
 * [Strategy](/insight/sections.php?sid=Strategy)
 * [Finance](/insight/sections.php?sid=Finance)
 
 ### Collections
 
 * [Our Emotions at Work](/insight/collection/Our-Emotions-at-Work.php)
 * [Speaking of Economics](/insight/collection/Speaking-of-Economics.php)
 * [The Age of Corporate Purpose](/insight/collection/the-age-of-corporate-purpose.php)
 * [How To Make Hybrid Work](/insight/collection/how-to-make-hybrid-work.php)
 * [All Collections](/insight/collections.php)
 
 ### Subscribe to Our Newsletter
 
 Cutting-edge research and expert advice delivered straight to your inbox.
 
 [Subscribe](/insight/newsletter.php)
 
* [Webinars](/insight/webinars.php)
* [Podcast](/insight/podcast/index.php)
* [Videos](/insight/video.php)
* [About](/insight/about.php)
Search
# Social Impact
## [Why You Should Develop a Giving Strategy](/insight/content/Why-You-Should-Develop-a-Giving-Strategy.php)
Experts in philanthropy share the many benefits of thinking through — and defining — what, when and how you contribute to charitable causes
## [How AI Can Help Make Wind Energy a Breeze](/insight/content/How-AI-Can-Help-Make-Wind-Energy-a-Breeze.php)
Wind turbines are expensive to build and maintain. Advanced technology can boost efficiency and ROI
## [Five Ideas to Advance Economic Reconciliation](/insight/content/Five-Ideas-to-Advance-Economic-Reconciliation.php)
A panel of Indigenous finance and business leaders shares how corporate Canada can create a more equitable and prosperous future for all
## [Why the Model Minority is a Dangerous Myth](/insight/content/Why-the-Model-Minority-is-a-Dangerous-Myth.php)
Asians in North America are burdened by a false narrative that erases their struggles
## [A Marketer’s Meditation on Fly Fishing](/insight/content/A-Marketers-Meditation-Article.php)
What can a beloved summer pastime tell us about sustainably enjoying the natural world?
## [Empowering Women in Global Mining](/insight/content/Empowering-Women-in-Global-Article.php)
Canadian NGO shows how to bring real change to a rough and tumble sector
## [Green-Savvy Board Members Make Their Mark](/insight/content/Green-Savvy-Board-Members-Article.php)
A firm’s environmental performance rises with board member expertise and strong governance
## [Your Firm’s Most Undervalued Asset? Try Nature](/insight/content/Your-Firms-Most-Undervalued-Asset-Try-Nature.php)
Too few businesses understand the value of biodiversity — to the planet and their competitiveness
## [What Car Loans Can Teach Us About AI](/insight/content/What-Car-Loans-Can-Teach-Us-About-AI.php)
Research on car dealerships shows how artificial intelligence can boost profits and help more people get a car
## [Understanding the Child’s Hopscotch to Leadership](/insight/content/Understanding-the-Childs-Hopscotch-to-Leadership.php)
Parents’ socioeconomic status plays an outsized, yet indirect, role in whether kids emerge as leaders in adulthood
## [Why Do-Good Gifts May Miss the Mark](/insight/content/Why-Do-Good-Gifts-May-Miss-the-Mark.php)
Moral satisfaction is hard to transfer. Here’s how to give a charitable gift with meaning
## [Lessons From Quebec’s Cannabis Strategy](/insight/content/Lessons-From-Quebecs-Cannabis-Strategy.php)
The province’s unique approach to selling cannabis offers some next steps for regulators across Canada
[Load More](#)
## Editor’s Picks
1. [The New Rules of Public Speaking](/insight/content/The-New-Rules-of-Public-Speaking.php)
2. [The Untapped Potential of Customer Loyalty Plans](/insight/content/The-Untapped-Potential-of-Customer-Loyalty-Plans.php)
3. [How to Build Trusted Brands](/insight/content/How-to-Build-Trusted-Brands.php)
4. [How Catfish Effects Drive Stock Market Reform](/insight/content/How-Catfish-Effects-Drive-Stock-Market-Reform.php)
[Topics](#nav-menu-topics)
* [Leadership](/insight/sections.php?sid=Leadership)
* [Teams](/insight/sections.php?sid=Teams)
* [Diversity](/insight/sections.php?sid=Diversity)
* [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
* [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
* [Social Impact](/insight/sections.php?sid=Social%20Impact)
* [Marketing](/insight/sections.php?sid=Marketing)
* [Strategy](/insight/sections.php?sid=Strategy)
* [Finance](/insight/sections.php?sid=Finance)
[Collections](/insight/collections.php)
[Webinars](/insight/webinars.php)
[Podcast](/insight/podcast/index.php)
[Videos](/insight/video.php)
[About](/insight/about.php)
## Kingston
Goodes Hall 
Queen's University 
Kingston, Ontario 
Canada K7L 3N6
[1.877.533.2330](tel:+18775332330)
## Toronto
Simcoe Place 
200 Front Street West 
30th Floor
[416.365.7141](tel:+14163657141)
## Smith Programs
* [Undergraduate Programs](/academic_programs/undergraduate.php)
* [MBA Programs](/mba_programs/index.php)
* [Graduate Programs](/grad_studies/index.php)
* [Executive Education](/executiveeducation/index.php)
## Directories
* [Contact Us](/about/contact.php)
* [Smith Centres](/centres/index.php)
* [Smith Services](/about/services.php)
## Connect with Smith
* [Facebook](https://www.facebook.com/smithbusiness)
* [Instagram](https://www.instagram.com/smithbusiness/)
* [Twitter X](https://twitter.com/smithbusiness)
* [Linkedin](https://www.linkedin.com/company/smith-school-of-business-at-queen's-university)
* [WeChat](https://mp.weixin.qq.com/s/SoosIZFmLD0D01aSGJzgLw)
The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.
* [Give to Smith](/invest/ "Give to Smith")
* [Careers](/about/careers/ "Careers at Smith")
* [Program Portals](/academic_programs/student-portals.php "Program Portals")
* [Privacy](http://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy")
© Smith School of Business

# [CEISI - Contact](https://smith.queensu.ca/centres/ceisi/events/tricolour/contact.php) 
 _https://smith.queensu.ca/centres/ceisi/events/tricolour/contact.php_

The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.

# [Our Insight Topics | Smith Business Insight](https://smith.queensu.ca/insight/tag.php?tid=Entrepreneurship) 
 _https://smith.queensu.ca/insight/tag.php?tid=Entrepreneurship_

 Smith Business Insight - Our Insight Topics 
[Skip to main content](#main-content)
Smith  
* [About](#)
 
 [Smith Home](/index.php)[Profile](/about/index.php)[News](/news_blog/index.php)[The Dean](/about/dean.php)[Strategic Plan](/about/strategic-plan.php)[Equity, Diversity, Inclusion & Indigenization](/about/EDII/index.php)[Learning Environment](/about/learning_environment.php)[Partnerships](/about/partners/index.php) [Services](/about/services.php) [SmithStore _​_](http://smithqueens.com/smithstore) [Queen's University _​_](https://queensu.ca)
 
* [Learning](#)
 
 [Explore Our Programs](/academic_programs/index.php)[Undergraduate Programs](/academic_programs/undergraduate.php) [MBA Programs](/mba_programs/index.php) [Graduate Programs](/grad_studies/index.php) [Executive Education](/executiveeducation/index.php)[Certificates](/academic_programs/certificates.php)[International](/international/index.php)[SmithEdge](/smithedge/index.php)[Academic Integrity](/about/academic_integrity/index.php)
 
* [Insights & Research](#)
 
 [Smith Business Insight](/insight/index.php) [Research](/research/index.php) [Publications](/about/publications.php) [Centres](/centres/index.php)
 
* [Faculty](#)
 
 [Meet Our Faculty](/faculty_and_research/faculty.php) [Join Our Ranks](/faculty_and_research/Join_Our_Ranks.php)
 
* [Alumni & Giving](#)
 
 [Give to Smith](https://smith.queensu.ca/invest/) [Alumni](/alumni/index.php)
 
* [Recruit & Engage](#)
 
 [Recruiting](/recruiting/index.php) [Partnerships](/about/partners/index.php) [Work with Students](/engage/index.php) [Smith Business Consulting](/centres/business-consulting/index.php)
 
Fresh ideas from [Smith School of Business](/index.php)
* [Topics](#)
 
 ### Categories
 
 * [Leadership](/insight/sections.php?sid=Leadership)
 * [Teams](/insight/sections.php?sid=Teams)
 * [Diversity](/insight/sections.php?sid=Diversity)
 * [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
 * [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
 * [Social Impact](/insight/sections.php?sid=Social%20Impact)
 * [Marketing](/insight/sections.php?sid=Marketing)
 * [Strategy](/insight/sections.php?sid=Strategy)
 * [Finance](/insight/sections.php?sid=Finance)
 
 ### Collections
 
 * [Our Emotions at Work](/insight/collection/Our-Emotions-at-Work.php)
 * [Speaking of Economics](/insight/collection/Speaking-of-Economics.php)
 * [The Age of Corporate Purpose](/insight/collection/the-age-of-corporate-purpose.php)
 * [How To Make Hybrid Work](/insight/collection/how-to-make-hybrid-work.php)
 * [All Collections](/insight/collections.php)
 
 ### Subscribe to Our Newsletter
 
 Cutting-edge research and expert advice delivered straight to your inbox.
 
 [Subscribe](/insight/newsletter.php)
 
* [Webinars](/insight/webinars.php)
* [Podcast](/insight/podcast/index.php)
* [Videos](/insight/video.php)
* [About](/insight/about.php)
Search
# Entrepreneurship
## [Our Top 10 Stories of 2024](/insight/content/Top-stories-of-2024.php)
Evolving leadership trends and technological advancements drove interest in our most popular content from the past year
## [How Firms Create Entrepreneurial Competitors](/insight/content/How-Firms-Create-Entrepreneurial-Competitors.php)
It’s great when employees have psychological ownership in an organization. Until it isn’t
## [The Myths Startup Founders Tell Themselves](/insight/content/The-Myths-Startup-Founders-Tell-Themselves.php)
The entrepreneurial ecosystem is filled with mistaken beliefs that too many young companies follow, often to their detriment
## [What Happens When Employees Become Owners?](/insight/content/What-Happens-When-Employees-Become-Owners.php)
Changes to federal income tax laws are expected to create a new era of employee ownership in Canada. That’s a good thing
## [Barry Cross’ Laws of Innovation, Operation and Execution](/insight/content/Barry-Cross-Laws-of-Innovation-Operation-and-Execution.php)
Discover 10 essential principles that can help strengthen your company’s performance and reduce risk
## [Growing the Indigenous Startup Ecosystem](/insight/content/Growing-Indigenous-Startup-Ecosystem.php)
First Nations, Métis and Inuit founders are building more businesses than the Canadian average. But support still lags
## [The Business of Family](/insight/content/The-Business-of-Family.php)
Explore why some family businesses endure while others fizzle out
## [How Not to Love Your Ideas to Death](/insight/content/How-Not-to-Love-Your-Ideas-to-Death.php)
Not everyone is going to adore your light-bulb moments as much as you. The good news: the critics can help
## [Why Are Some Family Businesses Built to Last?](/insight/content/Why-Are-Some-Family-Businesses-Built-to-Last.php)
The dynamics that make family businesses flourish go much deeper than a certain hot drama on TV
## [Making Productivity a Priority in Canada](/insight/content/Making-Productivity-a-Priority-in-Canada.php)
Driving greater prosperity and growth depends on leaders pulling the appropriate levers to increase value and reduce waste
## [The Case for Foreign Acquisition of Rising Stars](/insight/content/The-Case-for-Foreign-Acquisition-of-Rising-Stars.php)
Some of Canada’s most promising startups opt to sell themselves rather than scale up. And yes, that can be good for our economy
## [Fighting for Venture Financing](/insight/content/Fighting-for-Venture-Financing.php)
The startup funding landscape has changed. But entrepreneurs can still find ways to secure funding and flourish
[Load More](#)
## Editor’s Picks
1. [The New Rules of Public Speaking](/insight/content/The-New-Rules-of-Public-Speaking.php)
2. [The Untapped Potential of Customer Loyalty Plans](/insight/content/The-Untapped-Potential-of-Customer-Loyalty-Plans.php)
3. [How to Build Trusted Brands](/insight/content/How-to-Build-Trusted-Brands.php)
4. [How Catfish Effects Drive Stock Market Reform](/insight/content/How-Catfish-Effects-Drive-Stock-Market-Reform.php)
[Topics](#nav-menu-topics)
* [Leadership](/insight/sections.php?sid=Leadership)
* [Teams](/insight/sections.php?sid=Teams)
* [Diversity](/insight/sections.php?sid=Diversity)
* [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
* [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
* [Social Impact](/insight/sections.php?sid=Social%20Impact)
* [Marketing](/insight/sections.php?sid=Marketing)
* [Strategy](/insight/sections.php?sid=Strategy)
* [Finance](/insight/sections.php?sid=Finance)
[Collections](/insight/collections.php)
[Webinars](/insight/webinars.php)
[Podcast](/insight/podcast/index.php)
[Videos](/insight/video.php)
[About](/insight/about.php)
## Kingston
Goodes Hall 
Queen's University 
Kingston, Ontario 
Canada K7L 3N6
[1.877.533.2330](tel:+18775332330)
## Toronto
Simcoe Place 
200 Front Street West 
30th Floor
[416.365.7141](tel:+14163657141)
## Smith Programs
* [Undergraduate Programs](/academic_programs/undergraduate.php)
* [MBA Programs](/mba_programs/index.php)
* [Graduate Programs](/grad_studies/index.php)
* [Executive Education](/executiveeducation/index.php)
## Directories
* [Contact Us](/about/contact.php)
* [Smith Centres](/centres/index.php)
* [Smith Services](/about/services.php)
## Connect with Smith
* [Facebook](https://www.facebook.com/smithbusiness)
* [Instagram](https://www.instagram.com/smithbusiness/)
* [Twitter X](https://twitter.com/smithbusiness)
* [Linkedin](https://www.linkedin.com/company/smith-school-of-business-at-queen's-university)
* [WeChat](https://mp.weixin.qq.com/s/SoosIZFmLD0D01aSGJzgLw)
The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.
* [Give to Smith](/invest/ "Give to Smith")
* [Careers](/about/careers/ "Careers at Smith")
* [Program Portals](/academic_programs/student-portals.php "Program Portals")
* [Privacy](http://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy")
© Smith School of Business

# [CEISI - Overview](https://smith.queensu.ca/centres/ceisi/events/tricolour/index.php) 
 _https://smith.queensu.ca/centres/ceisi/events/tricolour/index.php_

## TriColour Venture Fund
## Up to $150k in Funding
TriColour Venture fund (TCVF) at Smith School of Business is Canada's first student-advised venture capital fund. Guided by experienced entrepreneurs and investors, TCVF fund allows Full Time MBA and Commerce students to gain the ultimate experiential learning opportunity through managing a multi-million dollar fund.
This academic course invests up to $150,000 into real ventures. Students meet directly with potential portfolio companies, assess the opportunities, conduct in-depth due diligence, and make recommendations to the Investment Advisory Board - a committee of seasoned entrepreneurs, angel investors, and venture capitalists.
Deals are syndicated with some of Canada's leading venture capital companies and angel investors.
The TCVF is seeded with contributions from alumni and friends of Queen's University, and all proceeds from the Fund are reinvested into maintaining and expanding the innovative educational program.
### What is the process?
* Application intake for TriColour Venture Fund is from June to August. 
 **Deadline: Sunday, August 25, 2024 – 5 pm (ET)**
* Initial screening uses a framework to evaluate each submission as an investment opportunity. Up to four companies will be selected for deeper analysis.
* The Due Diligence process for selected ventures is from August through December. This evaluation process involves face-to-face meetings, pitch presentations, financial modelling, research, and analysis.
* In the first week of December, the students make recommendations to the Investment Advisory Board. Successful companies will be eligible to receive up to $150,000 in funding as a co-investment with the venture's current lead investor or potential new investors.
* The Investment Advisory Board acts on the students' recommendations and engages the eligible companies in concluding due-diligence work and negotiating investment terms.
### Criteria to submit
* We are looking for early stage companies (Prototype or MVP ready) or businesses seeking funding for growth
* The ideal companies would be seeking an investment round amount of up to $750K
* **Important** - Companies should submit:
 1. An Executive Summary or Investors Briefing/Memo
 2. 4-minute video pitch presentation (with slides)
 3. Detailed business pitch deck
* Ventures should already be working with, or in the process of engaging with, a lead investor who has/will support the business with more than $150K in seed funding
### Ready to apply?
TriColour applications are now open. The application Dropbox will close on Sunday, August 25th at 5 pm (ET)
Please save all files with your business name and upload them to this [secure Dropbox](https://www.dropbox.com/request/1aiO9cUN926v1oqBiYWQ).
## Have any questions?
If you have any questions or comments regarding TriColour Venture Fund, please get in touch with us.
## Our Investment Portfolio
### Therapeutic Monitoring Systems
Ottawa, Ontario - 2012
Therapeutic Monitoring Systems Inc. (TMS) is developing clinical decision support software applications that provide critical care physicians and staff with remarkable insights into patient status and prognosis. Seamlessly integrating with existing monitors, our CIMVA family of software applications continuously analyze patient vital sign variability in order to detect changes in patient health status not otherwise observable using current standard-of-care monitoring in the ICU. Clinical studies to date strongly indicate that CIMVA holds the promise of significantly improving the diagnosis, prognosis and treatment of critically ill patients, enabling more timely and effective critical care decisions.
[therapeuticmonitoring.com](https://therapeuticmonitoring.com/)
### Profound Medical Inc.
Toronto, Ontario - 2011
Arguably the best medical imaging tool in common use today, Magnetic Resonance Imaging (MRI) enables a clinician to “see” in detail the internal organs of a patient non-invasively. Ultrasound imaging and thermal coagulation therapy have proven utility in several medical applications. When combining the two methodologies, the opportunity exists for an optimal and vastly superior clinical outcome. PMI has developed a novel MRI-compatible ultrasound energy wand to deliver controlled thermal therapy to the regions of the prostate gland via a trans-urethral approach. The system has been extensively tested and delivered consistent and predictable proof-of-concept results in mathematical, gel, pre-clinical models.
[profoundmedical.com](http://www.profoundmedical.com/)
### CrowdWave Games
Ottawa, Ontario - 2011
CrowdWave® engages fans interactively. Fans connect through play with each other, with the team and with sponsors. Our proprietary system of cameras, server and software captures and interprets fan movement to control branded big-screen experiences. Fans cooperate or compete, section versus section, level versus level, simply by moving their arms. Those movements control games and polls customized for teams and sponsors during breaks in the on-court, on-field or on-ice action. CrowdWave® entertains, CrowdWave® connects, CrowdWave® drives premium sponsorship revenue.
### SPARQ Systems Inc.
Kingston, Ontario - 2010
SPARQ Systems is an Ontario-based manufacturer of smart micro-inverters for photovoltaic (PV) power systems. A micro-inverter is a miniaturized voltage converter suitable for use with solar panels, significantly improving the overall efficiency of PV systems under normal as well as adverse conditions.
[sparqsys.com](http://www.sparqsys.com/)
### Vennsa Technologies, Inc.
Toronto, Ontario - 2010
Vennsa Technologies is the leading supplier of automated debugging and error localization software. Leveraging over 15 years of cutting edge research and patented IP, Vennsa's technology has been validated by numerous industrial partners. Its product automates the manual tasks of debug and error localization at the register transfer level (RTL), drastically reducing the time required to locate and correct errors.
[vennsa.com](http://www.vennsa.com/)
### Datec Coating Corporation
Mississauga, Ontario - 2006
Datec Coating Corporation is an innovative high tech materials science company that provides coatings and coating services for high performance coatings development, coating applications and heating solutions.
[dateccoating.com](http://www.dateccoating.com/)

# [Research - Smith Research Excellence Awards](https://smith.queensu.ca/research/awards.php) 
 _https://smith.queensu.ca/research/awards.php_

## New Researcher Achievement Award
The primary goal of the annual New Researcher Achievement Award is the recognition of faculty members whose research during the pre-tenure period is acknowledged as outstanding, and has brought credit to Smith School of Business. Receipts of this award will encourage ongoing research that will continue to appear in high quality academic publications.
### Guang Li
Guang Li is an assistant professor of Management Science and a Scotiabank Scholar. She received her PhD from the Marshall School of Business at the University of Southern California in 2016, her MEng from Massachusetts Institute of Technology, and MSc from the National University of Singapore. Her research, which focuses on revenue management, retail operations, and supply chain management, has been funded by the Natural Sciences and Engineering Research Council of Canada, and her work has been published in FT50 journals, including _Operations Research, Manufacturing & Service Operations Management,_ and _Production & Operations Management._
### Nicole Robitaille
Nicole Robitaille is an assistant professor of Marketing, working in consumer behaviour and decision making, exploring ways to improve public policy and consumer welfare. She received her PhD from the University of Toronto’s Rotman School of Management and her MSc in Marketing from Concordia University’s John Molson School of Business. Nicole has published in top journals, including FT50s, like the _Journal of Marketing, Management Science,_ and the _Harvard Business Review._ She was recently awarded a Financial Times Responsible Business Education Award for her research on organ donation in Ontario, for which she also received the Ontario Government’s prestigious Amethyst Award for Outstanding Achievement.
## Award for Research Excellence
The primary goal of the annual Award for Research Excellence is the recognition of an individual faculty member whose research is acknowledged as outstanding, and has brought considerable credit to Smith School of Business. Receipt of this award will result in ongoing research that will continue to appear in high quality academic publications.
### Ning Zhang
Ning Zhang is a professor of accounting and Commerce 1983 Distinguished Faculty Fellow. He is a prolific researcher whose work has appeared in FT50 journals. He earned his PhD in business administration from Duke University in North Carolina and his master’s degree in economics from the State University of New York at Binghamton. His interests center on information and incentives in financial markets, and he has been published in leading journals, including _Journal of Accounting Research, Journal of Accounting and Economics, The Accounting Review, Management Science,_ and _Review of Accounting Studies._
## New PhD Student Research Excellence Award
The purpose of the New PhD Student Research Excellence Award is to recognize an individual PhD student whose pre-comprehensive exam academic progress and demonstrated research potential are acknowledged as outstanding, as guided by the vision for the PhD program.
### Kaylee Somerville
Kaylee Somerville researches intervention strategies for leaders, behavioural economics, and decision-making at work. She is a staff writer at The Decision Lab, contributing pieces on gratitude, loss aversion, distracted driving, and online communities. Her work explores barriers that managers encounter in being effective leaders and, in collaboration with her supervisor Julian Barling, is a co-author of a forthcoming book chapter in _An Introduction to Contemporary Work Psychology._
## PhD Student Research Excellence Award
The purpose of the PhD Student Research Excellence Award is to recognize an individual PhD student whose academic progress and demonstrated research potential during the post-comprehensive exam stage of the PhD program are acknowledged as outstanding, as guided by the vision for the PhD program.
### Alyssa Grocutt
Alyssa Grocutt studies workplace safety, including safety-related leadership behaviours, parental workplace injuries and their impacts, and has already received distinctions including the Minerva Rising Star of the Year in 2023. Her work has been published in _Safety Science, Human Resource Development International,_ and _Organizational Dynamics._ Together with Julian Barling, she co-authored a book chapter in _Occupational health and wellbeing._ Another avenue of Alyssa’s research focuses on tattoos in professional settings.
## Smith Graduate Supervision Award
This award recognizes a faculty member whose contributions to graduate supervision have inspired students and contributed meaningfully to their learning. Other criteria include: inspiring students’ commitment to, and involvement in, research; mentoring; and providing leadership in students’ career development.
### Anthony Goerzen
Anthony Goerzen, Sobey Professor of International Business, received his PhD from the University of Western Ontario. His extensive teaching experience includes the Ivey School of Business, the UVic School of Business, and Babson College. This award recognizes Anthony’s impactful and inspiring leadership as a mentor and educator of young researchers. Graduate students benefit from Anthony’s significant management experience, which he brings to his pedagogy.
## Smith Graduate Teaching Excellence Award
Recipients of this award are faculty members in at least the second year of full-time appointment who have demonstrated an outstanding commitment to students in the PhD-MSc program. Graduate students interpret what constitutes teaching excellence by considering how well the instructor generates motivation, the effectiveness of the pedagogical approach, the extra-classroom supports offered, and the commitment of the faculty member over and above the norm.
### Gongtai Wang
Gongtai Wang is an assistant professor of Digital Technology who worked as a postdoctoral researcher in Business Information Systems Discipline at UQ Business School of Queensland, Australia before joining the Smith faculty. He received his PhD from Warwick Business School and has also been a system engineer in the information technology industry, an experience he brings to his engaging classes, which focus on rethinking and redesigning traditional products and services using emergent digital technologies.

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?c=MBA) 
 _https://smith.queensu.ca/news_blog/archive.php?c=MBA_

[## Financial Times releases 2024 EMBA Rankings
](https://smith.queensu.ca/news_blog/2024/2024-Financial-Times-releases-2024-EMBA-Rankings.php)
October 15, 2024
Kingston, Ont. – Smith School of Business’ two Executive MBA programs have been ranked among the top 75 EMBA programs in the world by the Financial Times (FT).
[## Smith MBA ranked #1 in Canada
](https://smith.queensu.ca/news_blog/2024/2024-Smith-MBA-ranked-1-in-Canada.php)
February 12, 2024
Kingston, Ont. – The Full-time MBA at Smith School of Business has secured the top spot in the country in the recently released Financial Times Global MBA ranking.
[## Smith MBA ranked among Top 75 in the world
](https://smith.queensu.ca/news_blog/2023/2023_Smith_MBA_ranking.php)
February 13, 2023
Kingston, Ont. – The Financial Times has ranked the Full-Time MBA at Smith School of Business in the top 75 in its annual ranking of global MBA programs.
[## Smith launches new scholarships for Black and Indigenous students
](https://smith.queensu.ca/news_blog/2022/2022_Smith_launches_new_scholarships_for_Black_and_Indigenous_students.php)
March 3, 2022
Kingston, Ont. – Two new scholarships at Smith are helping to make business education more accessible to students from two equity-deserving groups. The Smith School of Business Scholarship for Black Students and Smith School of Business Scholarship for Indigenous Students were created to enhance diversity while increasing access and inclusion for underrepresented groups.
[## Smith partners with Nigeria’s Lagos Business School
](https://smith.queensu.ca/news_blog/2021/2021_Smith_partners_with_Nigerias_Lagos_Business_School.php)
October 15, 2021
Kingston, Ont. – Smith School of Business is pleased to announce a new partnership with the graduate business school of Pan-Atlantic University in Nigeria, West Africa. Students in Smith’s MBA and Master of International Business will now be able to pursue exchange opportunities at Lagos Business School.

# [Dr. Brenda Brouwer appointed Interim Dean](https://smith.queensu.ca/news_blog/2019/2019_Brenda_Brouwer_Interim_Dean.php) 
 _https://smith.queensu.ca/news_blog/2019/2019_Brenda_Brouwer_Interim_Dean.php_

Dr. Brenda Brouwer, Interim Dean of Smith School of Business
**Kingston, Ont. –** On November 13, 2019, Brenda Brouwer was appointed Interim Dean of Smith School of Business, effective November 18, 2019.  Dr. Brouwer takes over from Teri Shearer who served temporarily as Interim Dean succeeding David Saunders.  
Dr. Brouwer recently completed a secondment with the Vector Institute for Artificial Intelligence (AI), where she joined the executive team as Head, Academic Partnerships. In this role she developed and led the talent development initiative focusing on cultivating relationships between the academy and industry to support a talent pipeline of well-trained master’s graduates with the skills, competencies and knowledge that organizations at the forefront of AI in Canada seek. Her time at Vector illustrated the importance of building networks between academies and organizations to promote knowledge and talent mobilization. 
Prior to her secondment at the Vector Institute, Dr. Brouwer was the Vice-Provost and Dean of the School of Graduate Studies and Postdoctoral Affairs at Queen’s University for eight years, preceded by five years as the Associate Dean in the School of Graduate Studies and Postdoctoral Affairs. She provided academic and administrative leadership which saw the expansion and development of graduate credentials including professional and applied advanced degrees, the development of resources that support academic excellence and student well-being, and the introduction of innovative and professional programming to meet the evolving needs of students entering an increasingly diverse labour market. Dr. Brouwer also provided national leadership in graduate education as President of the Canadian Association for Graduate Studies from 2015-2017. 
Dr. Brouwer joined Queen’s after completing a PhD in Neuroscience at the University of Toronto. She holds a BSc in Kinesiology (University of Waterloo) and an MSc in Biomechanics (McGill University). She is a professor in the School of Rehabilitation Therapy with cross appointments to the School of Kinesiology & Health Studies and the Centre for Neuroscience. Dr. Brouwer maintains a successful research program that focuses on quantifying the biomechanical, neuromuscular, and metabolic demands of mobility in healthy aging and stroke, and she has supervised more than 47 graduate students and several post-doctoral fellows. She has published more than 90 peer-reviewed papers and book chapters from work funded through external research grants.
Dr. Brouwer has served on numerous Senate committees, Council of Ontario Universities’ committees and working groups including the Council on Quality Assurance and the Highly Skilled Workforce Steering Committee. She has also been a member of the US Council of Graduate Studies Advisor group for completion in STEM master’s programs.

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=201910) 
 _https://smith.queensu.ca/news_blog/archive.php?a=201910_

The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.

# [Conflict Analytics Lab launches AI tool to streamline vaccine injury claims process](https://smith.queensu.ca/news_blog/2021/2021_Conflict_Analytics_Lab_launches_Vaccine_Mediator_tool.php) 
 _https://smith.queensu.ca/news_blog/2021/2021_Conflict_Analytics_Lab_launches_Vaccine_Mediator_tool.php_

**Kingston, Ont**. – The [Conflict Analytics Lab](https://conflictanalytics.queenslaw.ca/) (CAL), a joint project between Queen’s Law and Smith School of Business, has launched an online dispute resolution tool for COVID-19 vaccination claims in partnership with researchers from the University of Oxford, University College Dublin and the British Institute of International and Comparative Law.
Vaccine Mediator is an innovative tool that allows people who have experienced severe adverse reactions to an approved vaccine to report possible side effects and pre-assess their eligibility for compensation. Users are provided with a self-report and a personalized, jurisdiction-specific next-steps guide. The platform also lets them submit a pre-drafted claim to the relevant government agency. Vaccine Mediator is part of CAL’s AI-powered legal aid platform [MyOpenCourt](https://tool.myopencourt.org/).
Several Smith and Queen’s students helped create the tool. They are: Commerce student Cindy Lin, Law students Avinash Pillay, Solinne Jung, Yoonhyun Cho, Anushka Pharthyal and David Liang; and Computing Science student Tobias Carryer.
“It’s incredibly rewarding to be applying the skills I’ve acquired as a business student in such an impactful way,” says Lin, Comm’22. “At CAL, our aim is to create a future where legal aid is available to anyone who needs it—and now it’s possible with these tools. We’re beginning to see a tangible difference in our communities as the number of users increases, and we hope to sustain this momentum when developing new projects to democratize access to justice."
Compensation frameworks, like Canada’s Vaccine Injury Support Program released on June 1, set out levels of compensation based on the extent of harm suffered. Such frameworks are important given the millions of people vaccinated as protection from COVID-19. The Vaccine Mediator tool will help governments process vaccine injury claims more efficiently, mitigate the need for civil proceedings and help ease people’s vaccination hesitancy.
“Accessible information and reliable pathways to support are critical, particularly when making medical decisions. In the event of rare and adverse complications, our system guides individuals through the compensation process, from application to settlement, and connects them with supervised law student mediators for information and help along the way,” notes Professor Samuel Dahan, CAL director.
The first iteration of Vaccine Mediator is now operational in Canada and the U.S. and is customized based on the users’ jurisdiction and availability of vaccine injury compensation programs. The next iteration of the tool aims to use the self-reported data from the first, along with survey and curated medical data, to build and then operate a more robust screening system to assess claims’ validity. It will also identify potential legal remedies for injured persons.
“Information gathered and analyzed from the first iteration will be used to help users assess whether their symptoms are drawn from false information. We’ll help combat the spread of misinformation by providing real-time, up-to-date vaccine injury facts,” Dahan explains.
To learn more about Vaccine Mediator, visit **tool.myopencourt.org/vaccine-mediator**. The platform is intended to help users navigate government compensation programs. It does not store personal or medical information, nor does it constitute medical or legal advice.
**About the Conflict Analytics Lab**
A project of [Queen’s Law](https://law.queensu.ca/) and Smith School of Business, the [Conflict Analytics Lab](https://conflictanalytics.queenslaw.ca/) is a research-based consortium concerned with the application of data science and machine learning to dispute resolution. Conflict analytics is the process of extracting actionable knowledge from negotiation, mediation and settlement agreements.

# [Our Insight Topics | Smith Business Insight](https://smith.queensu.ca/insight/tag.php?tid=Women) 
 _https://smith.queensu.ca/insight/tag.php?tid=Women_

 Smith Business Insight - Our Insight Topics 
[Skip to main content](#main-content)
Smith  
* [About](#)
 
 [Smith Home](/index.php)[Profile](/about/index.php)[News](/news_blog/index.php)[The Dean](/about/dean.php)[Strategic Plan](/about/strategic-plan.php)[Equity, Diversity, Inclusion & Indigenization](/about/EDII/index.php)[Learning Environment](/about/learning_environment.php)[Partnerships](/about/partners/index.php) [Services](/about/services.php) [SmithStore _​_](http://smithqueens.com/smithstore) [Queen's University _​_](https://queensu.ca)
 
* [Learning](#)
 
 [Explore Our Programs](/academic_programs/index.php)[Undergraduate Programs](/academic_programs/undergraduate.php) [MBA Programs](/mba_programs/index.php) [Graduate Programs](/grad_studies/index.php) [Executive Education](/executiveeducation/index.php)[Certificates](/academic_programs/certificates.php)[International](/international/index.php)[SmithEdge](/smithedge/index.php)[Academic Integrity](/about/academic_integrity/index.php)
 
* [Insights & Research](#)
 
 [Smith Business Insight](/insight/index.php) [Research](/research/index.php) [Publications](/about/publications.php) [Centres](/centres/index.php)
 
* [Faculty](#)
 
 [Meet Our Faculty](/faculty_and_research/faculty.php) [Join Our Ranks](/faculty_and_research/Join_Our_Ranks.php)
 
* [Alumni & Giving](#)
 
 [Give to Smith](https://smith.queensu.ca/invest/) [Alumni](/alumni/index.php)
 
* [Recruit & Engage](#)
 
 [Recruiting](/recruiting/index.php) [Partnerships](/about/partners/index.php) [Work with Students](/engage/index.php) [Smith Business Consulting](/centres/business-consulting/index.php)
 
Fresh ideas from [Smith School of Business](/index.php)
* [Topics](#)
 
 ### Categories
 
 * [Leadership](/insight/sections.php?sid=Leadership)
 * [Teams](/insight/sections.php?sid=Teams)
 * [Diversity](/insight/sections.php?sid=Diversity)
 * [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
 * [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
 * [Social Impact](/insight/sections.php?sid=Social%20Impact)
 * [Marketing](/insight/sections.php?sid=Marketing)
 * [Strategy](/insight/sections.php?sid=Strategy)
 * [Finance](/insight/sections.php?sid=Finance)
 
 ### Collections
 
 * [Our Emotions at Work](/insight/collection/Our-Emotions-at-Work.php)
 * [Speaking of Economics](/insight/collection/Speaking-of-Economics.php)
 * [The Age of Corporate Purpose](/insight/collection/the-age-of-corporate-purpose.php)
 * [How To Make Hybrid Work](/insight/collection/how-to-make-hybrid-work.php)
 * [All Collections](/insight/collections.php)
 
 ### Subscribe to Our Newsletter
 
 Cutting-edge research and expert advice delivered straight to your inbox.
 
 [Subscribe](/insight/newsletter.php)
 
* [Webinars](/insight/webinars.php)
* [Podcast](/insight/podcast/index.php)
* [Videos](/insight/video.php)
* [About](/insight/about.php)
Search
# Women
## [Beyond the Glass Ceiling](/insight/content/Beyond-the-Glass-Ceiling.php)
How to lead with confidence and grow your career
[Load More](#)
## Editor’s Picks
1. [The New Rules of Public Speaking](/insight/content/The-New-Rules-of-Public-Speaking.php)
2. [The Untapped Potential of Customer Loyalty Plans](/insight/content/The-Untapped-Potential-of-Customer-Loyalty-Plans.php)
3. [How to Build Trusted Brands](/insight/content/How-to-Build-Trusted-Brands.php)
4. [How Catfish Effects Drive Stock Market Reform](/insight/content/How-Catfish-Effects-Drive-Stock-Market-Reform.php)
[Topics](#nav-menu-topics)
* [Leadership](/insight/sections.php?sid=Leadership)
* [Teams](/insight/sections.php?sid=Teams)
* [Diversity](/insight/sections.php?sid=Diversity)
* [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
* [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
* [Social Impact](/insight/sections.php?sid=Social%20Impact)
* [Marketing](/insight/sections.php?sid=Marketing)
* [Strategy](/insight/sections.php?sid=Strategy)
* [Finance](/insight/sections.php?sid=Finance)
[Collections](/insight/collections.php)
[Webinars](/insight/webinars.php)
[Podcast](/insight/podcast/index.php)
[Videos](/insight/video.php)
[About](/insight/about.php)
## Kingston
Goodes Hall 
Queen's University 
Kingston, Ontario 
Canada K7L 3N6
[1.877.533.2330](tel:+18775332330)
## Toronto
Simcoe Place 
200 Front Street West 
30th Floor
[416.365.7141](tel:+14163657141)
## Smith Programs
* [Undergraduate Programs](/academic_programs/undergraduate.php)
* [MBA Programs](/mba_programs/index.php)
* [Graduate Programs](/grad_studies/index.php)
* [Executive Education](/executiveeducation/index.php)
## Directories
* [Contact Us](/about/contact.php)
* [Smith Centres](/centres/index.php)
* [Smith Services](/about/services.php)
## Connect with Smith
* [Facebook](https://www.facebook.com/smithbusiness)
* [Instagram](https://www.instagram.com/smithbusiness/)
* [Twitter X](https://twitter.com/smithbusiness)
* [Linkedin](https://www.linkedin.com/company/smith-school-of-business-at-queen's-university)
* [WeChat](https://mp.weixin.qq.com/s/SoosIZFmLD0D01aSGJzgLw)
The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.
* [Give to Smith](/invest/ "Give to Smith")
* [Careers](/about/careers/ "Careers at Smith")
* [Program Portals](/academic_programs/student-portals.php "Program Portals")
* [Privacy](http://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy")
© Smith School of Business

# [London calling | Smith Magazine](https://smith.queensu.ca/magazine/issues/spring-2024/connect/london-calling.php) 
 _https://smith.queensu.ca/magazine/issues/spring-2024/connect/london-calling.php_

Julie Ioffe, photographed in Central London in March
My parents instilled a love of learning in me. My dad still, to this day, has a set of encyclopedias that I read growing up. If you wanted to keep me busy as a child, you just had to give me a book. From that, I grew to love puzzles and solving problems
Though I was always very science and very math-oriented, I was also athletic and adventurous. I played volleyball in high school and university, and I’ve been a dancer most of my life. I got into running because somebody told me I couldn’t run a marathon. So I ran three. And to feed my sense of wanderlust, I’ve travelled to over 50 countries so far.
Career-wise, at first, I wanted to be a doctor. I was interested in the human brain, so I got a dual degree from the University of Calgary in neuroscience and clinical psychology. I published research on how to prevent memory loss associated with aging. I was very proud of all my work in the field, but I didn’t see myself making a career out of medicine.
My first job out of university was working at a TD branch in Calgary, my hometown, as a financial adviser. There, I discovered my interest in investing — the numbers, formulas and analytical nature of the work. I started my CFA (Chartered Financial Analyst designation) to progress my knowledge and began to learn more about macro investing and how it moves the world.
In 2015, when I was a macroeconomic analyst in New York City, I was given a project to study populism’s potential effects on the financial markets. I think no one thought this topic was relevant at the time, which is why it went to someone junior like me. As I was doing my analysis, Brexit and then Trump threw some unexpected curveballs. Suddenly, my work was at the centre of attention at a major global bank.
I came into the MBA at Smith very academically focused. But the program helped me recognize the importance of cultivating relationships with people. I’m great friends with several of my classmates to this day. I value their thoughts massively and they impact my life quite a bit.
After my MBA, I wanted to live in Europe. London seemed a logical place for a finance career. Today, I’m a fixed income portfolio manager at TD. London is such a vibrant city and has vast opportunities to meet very interesting senior people in finance and politics. I can call someone at the Bank of England and say, “Hey, I’m right next door. Can I pop over to discuss the effects of monetary policy on inequality?”
I want to make a difference in the world, and because I have this love of economics, I think that’s the way I can do it. I’m doing research on my own time now. My thesis is that monetary and fiscal policy should be for people. You’ll read about inflation and GDP numbers, but it’s missing the quality of life and satisfaction of an average citizen. We should also assess the inequality of opportunity and access to education or health care. This is the side of economics where I hope to make a positive impact.

# [Our Insight Topics | Smith Business Insight](https://smith.queensu.ca/insight/tag.php?tid=Gender%20Differences) 
 _https://smith.queensu.ca/insight/tag.php?tid=Gender%20Differences_

 Smith Business Insight - Our Insight Topics 
[Skip to main content](#main-content)
Smith  
* [About](#)
 
 [Smith Home](/index.php)[Profile](/about/index.php)[News](/news_blog/index.php)[The Dean](/about/dean.php)[Strategic Plan](/about/strategic-plan.php)[Equity, Diversity, Inclusion & Indigenization](/about/EDII/index.php)[Learning Environment](/about/learning_environment.php)[Partnerships](/about/partners/index.php) [Services](/about/services.php) [SmithStore _​_](http://smithqueens.com/smithstore) [Queen's University _​_](https://queensu.ca)
 
* [Learning](#)
 
 [Explore Our Programs](/academic_programs/index.php)[Undergraduate Programs](/academic_programs/undergraduate.php) [MBA Programs](/mba_programs/index.php) [Graduate Programs](/grad_studies/index.php) [Executive Education](/executiveeducation/index.php)[Certificates](/academic_programs/certificates.php)[International](/international/index.php)[SmithEdge](/smithedge/index.php)[Academic Integrity](/about/academic_integrity/index.php)
 
* [Insights & Research](#)
 
 [Smith Business Insight](/insight/index.php) [Research](/research/index.php) [Publications](/about/publications.php) [Centres](/centres/index.php)
 
* [Faculty](#)
 
 [Meet Our Faculty](/faculty_and_research/faculty.php) [Join Our Ranks](/faculty_and_research/Join_Our_Ranks.php)
 
* [Alumni & Giving](#)
 
 [Give to Smith](https://smith.queensu.ca/invest/) [Alumni](/alumni/index.php)
 
* [Recruit & Engage](#)
 
 [Recruiting](/recruiting/index.php) [Partnerships](/about/partners/index.php) [Work with Students](/engage/index.php) [Smith Business Consulting](/centres/business-consulting/index.php)
 
Fresh ideas from [Smith School of Business](/index.php)
* [Topics](#)
 
 ### Categories
 
 * [Leadership](/insight/sections.php?sid=Leadership)
 * [Teams](/insight/sections.php?sid=Teams)
 * [Diversity](/insight/sections.php?sid=Diversity)
 * [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
 * [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
 * [Social Impact](/insight/sections.php?sid=Social%20Impact)
 * [Marketing](/insight/sections.php?sid=Marketing)
 * [Strategy](/insight/sections.php?sid=Strategy)
 * [Finance](/insight/sections.php?sid=Finance)
 
 ### Collections
 
 * [Our Emotions at Work](/insight/collection/Our-Emotions-at-Work.php)
 * [Speaking of Economics](/insight/collection/Speaking-of-Economics.php)
 * [The Age of Corporate Purpose](/insight/collection/the-age-of-corporate-purpose.php)
 * [How To Make Hybrid Work](/insight/collection/how-to-make-hybrid-work.php)
 * [All Collections](/insight/collections.php)
 
 ### Subscribe to Our Newsletter
 
 Cutting-edge research and expert advice delivered straight to your inbox.
 
 [Subscribe](/insight/newsletter.php)
 
* [Webinars](/insight/webinars.php)
* [Podcast](/insight/podcast/index.php)
* [Videos](/insight/video.php)
* [About](/insight/about.php)
Search
# Gender Differences
## [Five Ideas to Improve Gender Equity Today](/insight/content/Five-Ideas-to-Improve-Gender-Equity-Today.php)
A panel of experts shares how to make your workplace better for women and non-binary people — right now
## [New Ways to Break the Glass Ceiling](/insight/content/New-Ways-to-Break-the-Glass-Ceiling.php)
Why behavioural economics should become a tool for executive recruitment
## [The Problem With How We Talk About Diversity](/insight/content/the-problem-with-how-we-talk-about-diversity.php)
Celebrating stars who break the glass ceiling can set back the cause for equality. Ditto for pushing the business case
## [How Relationships at Home Affect Leaders at Work](/insight/content/how-relationships-at-home-affect-leaders-at-work.php)
Research shows why companies should offer more personal support to people in leadership roles
## [Can the Canadian Armed Forces Recruit More Women?](/insight/content/how-can-the-canadian-armed-forces-recruit-more-women.php)
Previous efforts have failed to convince women that there’s no life like it. But researchers may have a better way
## [The Shadow Over Female Investment Analysts](/insight/content/the-shadow-over-female-investment-analysts.php)
Many investors think female stock pickers are more risk averse. In truth, women perform as well, and maybe better, than men
## [The Gender Gap in Severance Deals. And What it Reveals](/insight/content/the-gender-gap-in-severance-deals-and-what-it-reveals.php)
Women CEOs negotiate better severance deals than men—for good reason, unfortunately
## [Start-Up Funding: Jack Gets the Bread, Jill the Crumbs](/insight/content/start-up-funding-jack-gets-the-bread-jill-the-crumbs.php)
If it’s not implicit bias, then why do female entrepreneurs struggle to access venture capital?
## [Women as Leaders: Do They Make a Difference?](/insight/content/women-as-leaders-do-they-make-a-difference.php)
They tend to have “communal” priorities that shape corporate policies on social responsibility
## [Breadwinners, Breadsharers, and the Status of Women’s Work](/insight/content/breadwinners-breadsharers-and-the-status-of-womens-work.php)
The value husbands place on their wives’ contribution depends more on the social status the job offers than the money it brings in
## [The Marital Lives of High-Status Women](/insight/content/the-marital-lives-of-high-status-women.php)
Women who hold higher status than their partners have a greater chance of experiencing divorce. Having a helpful husband is one antidote to the Oscar love curse
## [Women on Boards: A Battle for Legitimacy](/insight/content/women-on-boards-a-battle-for-legitimacy.php)
How organizations account for female board membership can end up marginalizing the very people they want to champion
[Load More](#)
## Editor’s Picks
1. [The New Rules of Public Speaking](/insight/content/The-New-Rules-of-Public-Speaking.php)
2. [The Untapped Potential of Customer Loyalty Plans](/insight/content/The-Untapped-Potential-of-Customer-Loyalty-Plans.php)
3. [How to Build Trusted Brands](/insight/content/How-to-Build-Trusted-Brands.php)
4. [How Catfish Effects Drive Stock Market Reform](/insight/content/How-Catfish-Effects-Drive-Stock-Market-Reform.php)
[Topics](#nav-menu-topics)
* [Leadership](/insight/sections.php?sid=Leadership)
* [Teams](/insight/sections.php?sid=Teams)
* [Diversity](/insight/sections.php?sid=Diversity)
* [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
* [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
* [Social Impact](/insight/sections.php?sid=Social%20Impact)
* [Marketing](/insight/sections.php?sid=Marketing)
* [Strategy](/insight/sections.php?sid=Strategy)
* [Finance](/insight/sections.php?sid=Finance)
[Collections](/insight/collections.php)
[Webinars](/insight/webinars.php)
[Podcast](/insight/podcast/index.php)
[Videos](/insight/video.php)
[About](/insight/about.php)
## Kingston
Goodes Hall 
Queen's University 
Kingston, Ontario 
Canada K7L 3N6
[1.877.533.2330](tel:+18775332330)
## Toronto
Simcoe Place 
200 Front Street West 
30th Floor
[416.365.7141](tel:+14163657141)
## Smith Programs
* [Undergraduate Programs](/academic_programs/undergraduate.php)
* [MBA Programs](/mba_programs/index.php)
* [Graduate Programs](/grad_studies/index.php)
* [Executive Education](/executiveeducation/index.php)
## Directories
* [Contact Us](/about/contact.php)
* [Smith Centres](/centres/index.php)
* [Smith Services](/about/services.php)
## Connect with Smith
* [Facebook](https://www.facebook.com/smithbusiness)
* [Instagram](https://www.instagram.com/smithbusiness/)
* [Twitter X](https://twitter.com/smithbusiness)
* [Linkedin](https://www.linkedin.com/company/smith-school-of-business-at-queen's-university)
* [WeChat](https://mp.weixin.qq.com/s/SoosIZFmLD0D01aSGJzgLw)
The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.
* [Give to Smith](/invest/ "Give to Smith")
* [Careers](/about/careers/ "Careers at Smith")
* [Program Portals](/academic_programs/student-portals.php "Program Portals")
* [Privacy](http://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy")
© Smith School of Business

# [The New Rules of Public Speaking | Smith Business Insight](https://smith.queensu.ca/insight/content/The-New-Rules-of-Public-Speaking.php) 
 _https://smith.queensu.ca/insight/content/The-New-Rules-of-Public-Speaking.php_

**You’re called to take the microphone** in front of a room packed with people whose engagement you need and whose opinion you value. How do you feel?
Public speaking tends to spark some strong, visceral reactions — even among leaders whose jobs centre around it. “I loathe making speeches, and always have,” [Richard Branson once admitted](https://fortune.com/2015/01/12/richard-branson-on-how-to-calm-public-speaking-jitters/). Warren Buffett has said the very thought of taking a podium used to make him “[physically ill](https://www.cnbc.com/2019/03/21/billionaire-warren-buffett-says-a-100-dollar-course-had-the-biggest-impact-on-his-success.html).”
If you can relate, you’re certainly not alone. [Glossophobia](https://www.merriam-webster.com/dictionary/glossophobia) is a real thing, with [up to 30 per cent](https://pubmed.ncbi.nlm.nih.gov/22156935/) of the general population experiencing diagnosable public speaking anxiety. In the quarter-century since Jerry Seinfeld joked that, at a funeral, more folks would “rather be in the casket than doing the eulogy,” the collective understanding that a lot of people truly dread public speaking has become as common as a dramatic pause at a TED Talk.  
But the public speaking landscape has also changed during that time, which means that those of us who fear standing up in front of a room full of people are operating on some outdated assumptions.
In recent years, audience expectations have shifted, and the speakers who resonate most with them have adapted accordingly. The slick and authoritative archetype established by the likes of Tony Robbins hasn’t gone away, but it is now sharing the stage with speakers with a more diverse and accessible range of traits and tendencies.
“People are looking for trust. They’re responding to personal connection as much as professional poise,” explains Jordyn Benattar, founder and president of [Speakwell](https://www.letsspeakwell.com/), a Toronto-based firm that provides public speaking coaching services to thousands of individuals and organizations internationally. “I don’t know the extent to which a voice that is ‘on’ — one that is performative, scripted or didactic — is really going to pull people in these days.”
## **Authenticity trumps artifice** 
Benattar learned the power of speaking well early in life. She developed a knack for storytelling as a child actor, which she parlayed into an internationally competitive debate and speaking career in her teen years. “As I became more proficient, more articulate, more concise and more confident speaking to large groups of people, I noticed that people noticed me,” Benattar explains. “I saw the respect you earn and the credibility that you carry by virtue of how you present yourself.” (Fun fact: Benattar started Speakwell as a side hustle while a student at Queen’s University.)
The most effective speakers today are not those who ape a particular style, she says. Rather, they’re people who bring their true selves to the stage. “Audiences today place huge value on authenticity,” Benattar explains. Most audiences are sophisticated enough to see through artificial performances, she points out, preferring instead a what-you-see-is-what-you-get communication style. Audiences have lost the illusion that experts must be perfect to carry authority, and many simply relate better to speakers who admit to challenges than to those who project a glossier veneer.
“People want to see that you’re not performing, that you’re speaking to a room of people the same way you would in a one-on-one conversation,” Benattar reasons. “That’s how people begin to trust you, feel connected with you, and build rapport with you. If you seem completely phony to your audience, it’s disappointing for them — like meeting a celebrity who’s nothing like what they thought.”
Furthermore, most speakers are simply better at communicating when they’re not pretending to be someone else. That’s why the work Speakwell does with clients almost always begins with some self-reflection — not elocution, or stage presence, or any other tactic. “It’s not about training people to be a cookie-cutter version of somebody else,” Benattar says. “It’s about finding a speaking style that feels consistent and right and true to them, so that’s what shows up whenever they open their mouths. That’s really the only way to be a great public speaker. Otherwise, at some point, you’ll get out of ‘character.’”
## **Audiences crave connection**
[Joze Piranian](https://www.linkedin.com/in/jozepiranian/), MIB’13, shares Benattar’s view that audiences crave authenticity — he sees it every day. Piranian travels the world as a [keynote speaker](https://www.jozepiranian.com/) and comedian, and he does so with a severe stutter. He’s noted a clear evolution in what moves the audiences he addresses: “I think there is less emphasis on perfection and more on connection,” he says. “I am perhaps not what one might expect a public speaker to sound like. But if we look at it through the lens of connection, rather than perfection, the style of public speaking I deliver is impactful and effective.”
Piranian often opens his talks by acknowledging that growing up with a speech impediment in Lebanon was very difficult and admitting that he often coped by staying quiet. He’s also upfront about how his eventual journey to find and embrace his voice — which is the subject of the recent documentary _Words Left Unspoken_ — was not without roadblocks. “When I can talk about those challenges in a vulnerable way, it does create a connection with the audience,” Piranian says.
Why? When speakers lower their own defenses — by say, sharing a vulnerable story or joking about elephants in the room — audiences tend to react by lowering theirs too. “Emotion is the currency of commonality,” Piranian says. “An audience member does not have to have had the same experience that I did to connect with my story. As long as I am conveying emotions that they have had before — like fear, or self-consciousness, or anxiety — all of a sudden, a niche experience like mine can have a universal appeal.” 
Once that connection is established, Piranian says that audiences are far more likely to take in whatever insights or wisdom the speaker might have to share — and remember it. It creates a depth of engagement that simply isn’t possible via more traditional speaking styles that favour polished pontification.
“Audiences tend to gravitate towards individuals with emotional depth,” Piranian reasons. “When you can give the world a glimpse of that, it makes people feel like they are less alone. We all go through days when our emotions can be utter chaos, and when we can hear someone else articulate that journey it ends up acting as a form of authority.” 
## **Clarity creates credibility**
Of course, it’s not just what you say that matters. It’s also how you say it. And on that matter, experts agree audience attention spans [are shrinking](https://www.wsj.com/articles/how-to-restore-our-attention-spans-11673031247) and today’s best speakers know how to keep it tight. As Benattar puts it: “You need to hit the nail on the head in as few words as possible.”
That doesn’t necessarily mean blasting through addresses with TikTok-style speed or replacing substance with soundbites. But it does lend extra import to preparing a message that is snappy, unambiguous and memorable. “You have to have a very strong controlling idea,” confirms [Matt Reesor](https://smith.queensu.ca/faculty_and_research/faculty_list/reesor-matthew.php), a communications expert at Smith School of Business, who teaches leaders how to sharpen their messaging. “And you have to deliver it in a clear and concise way.”
It’s always been important for speakers to anchor their talks in a key message, says Reesor, who has been working in the space for two decades. But the proliferation of distractions today means that few speakers retain the luxury of taking their time to get to the point. “The need to get that message out there as quickly as possible is one of the clearest ways that communication has changed,” Reesor says.
The through-line in all of this is a general desire among audiences for transparency — for speakers to put all their metaphorical cards out on the table. We live in an age of misinformation and fragmentation, and people want messengers that feel legit. “The facts no longer speak for themselves,” Reesor explains. “What people choose to believe depends on who they trust.” In this context, speaking traits like those flagged by our experts — authenticity, connection and clarity — help to foster what is perhaps the most potent commodity in verbal communication today: credibility.
“You can have really strong presentation skills, but if the audience doesn’t view you as trustworthy, it doesn’t matter — your message is not going to land,” Reesor says. “It really does all come down to credibility.”
Tags:

# [CEISI - Programs](https://smith.queensu.ca/centres/ceisi/programs-initiatives/programs.php) 
 _https://smith.queensu.ca/centres/ceisi/programs-initiatives/programs.php_

The Centre for Entrepreneurship, Innovation & Social Impact offers the following programs and opportunities to enhance the student learning experience and assist entrepreneurs and SMEs.
## Master of Management Innovation & Entrepreneurship
The program is designed to develop effective leaders in highly entrepreneurial and innovative career pursuits. Graduates leave the program ready to handle any entrepreneurial endeavour from the formation of a startup, to social innovation, to innovation within a corporate environment.
[View MMIE Program](https://smith.queensu.ca/grad_studies/mei/index.php)
## Queen’s Innovation Centre Summer Initiative (QICSI)
QICSI is a 16-week summer program that offers the valuable opportunity to start your own business while being paid and receiving seed funding. QICSI is a highly competitive, intense and well-resourced program that takes place full time in-person on Queen's Campus from May-August and therefore only the most dedicated are encouraged to apply.
[Learn more about QICSI](https://www.queensu.ca/innovationcentre/programs/queens-innovation-centre-summer-initiative-qicsi)
## Smith Scale-Up Summit
The Smith Scale-Up Summit is Canada’s only student-led conference connecting prominent entrepreneurs and scale-up leaders with students from a premier business school. Scaling Canadian companies is crucial to our success in the 21st-century economy. Through interactive learning, networking, and idea sharing, we can equip the next generation to drive our economy forward.
## Queen’s Entrepreneurs Competition
The QEC is an international business pitch competition held in Toronto, Canada, with +$60,000 in prizes dedicated to helping talented entrepreneurs from around the world jump-start their businesses - and their dreams.
[Visit QEC](https://theqec.ca/)
## Dunin-Deshpande Queen’s Innovation Centre
The mission of DDQIC is to catalyze this potential, developing entrepreneurial mindsets and fostering a culture of innovation across Queen’s University, the Kingston community, and globally. We build changemakers by encouraging and supporting their entrepreneurial initiatives through startup incubators, workshops, programs, courses, and pitch competitions.
[Visit DDQIC](https://www.queensu.ca/innovationcentre/)
## Venture for Canada
As a national charity, Venture for Canada is on a mission to foster the entrepreneurial skills and mindsets of young Canadians. Their vision is a Canada where young people can equitably realize their entrepreneurial potential to build the most prosperous place in the world.
[Venture for Canada](https://ventureforcanada.ca/)

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=201511) 
 _https://smith.queensu.ca/news_blog/archive.php?a=201511_

[## Fall Convocation 2015
](https://smith.queensu.ca/news_blog/2015/fall-convocation-master-of-science.php)
November 20, 2015
Members of Smith School of Business' undergraduate and graduate programs received their degrees. Diplomas were conferred on students of the Graduate Diploma in Business and Graduate Diploma in Accounting programs.
[## Commerce team 2nd at international case competition in Hong Kong
](https://smith.queensu.ca/news_blog/2015/2015-11-04-case.php)
November 4, 2015
Kingston, Ont. November 4, 2015 - Smith School of Business Commerce students excelled at the Citi-HKUST International Case Competition in Hong Kong, capturing second place in a field of 18 teams. This by-invitation competition, held Oct. 25-30, attracted students from a diverse mix of top-ranked international business schools in Asia, Europe and North America.

# [Why You Shouldn’t Put a Price on a Great Gift | Smith Business Insight](https://smith.queensu.ca/insight/content/Why-You-Shouldnt-Put-a-Price-on-a-Great-Gift.php) 
 _https://smith.queensu.ca/insight/content/Why-You-Shouldnt-Put-a-Price-on-a-Great-Gift.php_

Who doesn’t love to be a rubbernecker to spectacular gift crashes? The cockroach stuffed animal. The 50 pounds of russet potatoes. The colouring book and used crayons for a nineteenth birthday.
Yes, these are all amusing examples of human folly, but wipe that smug smile off your face. While we may know a lousy gift when we receive it, few are adept at predicting what others will appreciate.
Social scientists have looked at this phenomenon from all angles and agree: Gift givers look for gifts that wow and impress. Recipients want gifts that are useful and easy to enjoy. Givers are suckers for “[smile-seeking](https://journals.sagepub.com/doi/abs/10.1177/0956797618761373)” gifts that elicit immediate reactions (a dozen blooming roses!). Recipients prefer “value-seeking” gifts (two dozen rose buds that can be enjoyed for longer).
Studies show that people appreciate the gifts they requested more than the “thoughtful” gifts they never asked for.
Perhaps the most consequential gap between giver and givee concerns gift price and feelings of appreciation. Gift givers are convinced that the more they spend, the more appreciation they’ll receive. Surely a Rolex shows a lot of love. [But that’s not true](https://www.sciencedirect.com/science/article/abs/pii/S0022103108002175). Recipients don’t appreciate pricier gifts more than modest gifts. Evidence even suggests that they tend to assume the gift cost less than it did.
This mismatch around gift price is odd, says [Aybike Mutluoglu](https://www.linkedin.com/in/aybikemutluoglu/?originalSubdomain=ca), a PhD student in marketing and consumer behaviour at Smith School of Business. “If you look at it from an economic perspective,” she says, “more expensive gifts represent both an objectively higher investment and greater value to recipients.”
## **Money changes everything**
Mutluoglu is fascinated by gifting behaviour and how it touches disciplines from anthropology and sociology to psychology and economics. It’s certainly a deep well for researchers to draw from. Mutluoglu herself has weighed in with studies that explore why an expensive gift—however well meaning—can be a risky proposition for the giver.
Her research, conducted with Smith colleagues [Laurence Ashworth](https://smith.queensu.ca/faculty_and_research/faculty_list/ashworth-laurence.php) and [Nicole Robitaille](https://smith.queensu.ca/faculty_and_research/faculty_list/robitaille-nicole.php), suggests that expensive gifts can cause people on the receiving end to become suspicious of the giver’s motives.
“Previous evidence shows that mere reminders of money cause people to be more self-focused and less communal,” says Mutluoglu.
> “If money causes people to pursue things that benefit themselves, we thought it might also increase the likelihood that people will consider self-serving motives to explain others’ behaviour.”
Mutluoglu, Ashworth and Robitaille tested their theories in a series of studies.
In the first, they wanted to know if an expensive gift alone was enough to trigger suspicion or only when recipients had a reason to be suspicious (when the gift was from a work colleague versus a friend, for example, or when the price tag was left on the gift). They asked one group of undergraduate students to imagine themselves receiving a typically priced gift bottle from the liquor store and another group an expensive bottle from the store. They varied whether the gift came from a colleague or friend and whether the price tag was left on or not. The researchers found that expensive gifts could activate suspicious thoughts even when recipients had no reason to be suspicious.
In a followup study conducted right after Christmas, they replicated the effect with real gifts received by participants from romantic partners, friends and parents.
## **Experiences beat durable goods**
Would recipients also be suspicious if a gift represented an investment of time and effort rather than money? To find out, the researchers asked their panel to imagine either that the gift came from a swanky high-end retailer or from a store that was out of the way for the gift giver to visit. Money, but not effort, triggered suspicion. That was consistent with their idea that money can make people question others’ motives.
The final puzzle concerned material versus experiential gifts. Experiential gifts have already been shown to have a halo effect. Compared to a tangible product, experiences [make recipients happier](https://journals.sagepub.com/doi/full/10.1177/0963721416656937) and [foster stronger giver-recipient relationships](https://psycnet.apa.org/record/2017-27060-003). It’s all about the gooey emotions that experiences bring out. And generally, material purchases are more likely to be seen as [motivated by selfishness](https://journals.sagepub.com/doi/10.1177/0146167210362790).
Given these findings, one would think that experiential gifts would be less likely to arouse suspicion than material gifts. To test this theory, a panel was asked to imagine receiving a birthday gift from a friend: either a bottle of wine or a winery tour. As expected, study participants were more suspicious of the gift of the bottle of wine (material) than the tour of a winery (experience).
“We found that experiential gifts could serve as a buffer against the suspicion induced by the gift’s monetary value,” says Mutluoglu. “When a gift is more material, it’s more likely to be viewed as a tangible expression of the expense, thereby increasing the possibility of activating thoughts of self-interest in recipients.”
## **Relationships gone sour**
On one level, expensive gifts do leave a positive impression. This study showed that when people perceived a gift as expensive, they judged it to be objectively better and they appreciated it. But that didn’t stop them from suspecting that the giver’s motives were not genuine.
Such suspicions can also affect relationships. As part of their study, Mutluoglu and her colleagues collected data on recipients’ impressions of the gift giver. They found that, as a result of suspicions surrounding gift expense, recipients felt less close to the giver and thought of them less favourably.
So where does this leave you when a celebration or milestone rolls around that you want to mark in style? For one thing, don’t assume that more expensive is better. Perception of expense differs across individuals, situations, occasions or relationships, says Mutluoglu. Make sure your price tag will not be perceived as “too much” to avoid eliciting suspicion.
If you want to give a big-ticket gift, pick one that doesn’t explicitly convey how much money you spent on it. “Do something to disconnect the gift from the money,” says Mutluoglu. “Certainly, don’t try to convey the expense of the gift, as givers frequently seem to do.”
Better yet, gift an experience. Material gifts may be durable but experiences are as likely—if not more—to leave a lasting impression. (Message to travel or entertainment companies that package experiences: Make it easy for consumers to buy these types of ephemeral gifts. For example, create experiential gift registries.)
Now that we have expensive gifts all cleared up, there’s one last perplexing part of the gifting story: How did we get it so wrong?
We know what it’s like to be on the receiving end of pricey yet ill-considered gifts and have our suspicions aroused. But we seem to have no muscle memory when it comes to buying expensive gifts for others. We make the same mistakes over and over. Retailers aren’t complaining, of course, but perhaps it’s time we break the third wall and consult our inner givee for gift ideas that truly hit home.
Tags:

# [CPIA - Faculty & Instructors](https://smith.queensu.ca/centres/cpia/program-details/faculty.php) 
 _https://smith.queensu.ca/centres/cpia/program-details/faculty.php_

You’ll learn from distinguished Queen’s University faculty members and expert instructors, benefiting from years of academic research and industry experience.
## Dr. Christopher Cotton
Chris Cotton is a Professor of Economics at Queen's University, holds the prestigious Jarislowsky-Deutsch Chair in Economic & Financial Policy, and is a co-founder of the Certificate in Professional Impact Analysis program. He is Director of the John Deutsch Institute for the Study of Economic Policy, and co-director of the Centre for Innovative Policy Research at Queen’s.
Dr. Cotton is a cross-appointed professor in the Schools of Public Policy and Medicine at Queen’s, and an invited researcher with J-PAL at MIT. He is a co-owner and research advisor at Limestone Analytics, and the scientific director of the Canadian Public Economics Group.
From 2021-2024, Prof. Cotton was co-director of the One Society Network, a national research network of economists, public health officials, and other researchers working to measure the broader impacts of COVID-19 and pandemic policy. He also served on the Royal Society of Canada’s COVID Working Group Economic Recovery and Global Canada’s Covid Strategic Choices Group.
He has been published in top scientific journals such as the American Economic Review, Management Science, the Journal of Public Economics, and the Journal of Labor Economics and has included seminal papers on several topics. He has received major grant awards from the Social Sciences and Humanities Research Council of Canada (SSHRC), the Natural Sciences and Engineering Research Council of Canada (NSERC), the Tri-Council’s New Frontiers in Research Fund (NFRF), Canada’s Digital Technology Supercluster, and the Spenser Foundation for Education Research.
He regularly advises major firms, governments, and organizations including the World Health Organization, USAID, Nutrition International, World Vision, and others.
## Dr. Bahman Kashi
Bahman Kashi is a Continuing Adjunct Assistant Professor at Queen’s University, and the founder and an economist with Limestone Analytics. He is a co-founder and the Academic Director of the Certificate in Professional Impact Analysis program.
Dr. Kashi has consulted in the areas of economic impact assessment, public investment management, economic analysis of development projects, and evaluation of social programs. He has worked on capacity building and technical advisory projects in Rwanda, Kenya, South Africa, Zimbabwe, Nigeria, Haiti, Malaysia, Canada, United States, Cyprus, Ghana, Lesotho, Indonesia, and Switzerland.
His research interests include the economics of energy, transport, and telecommunication markets; private sector engagement and innovative finance; integration of environmental and social impacts into cost-benefit analysis, monitoring and evaluation; and institutional aspects of impact analysis.
Dr. Kashi has held numerous professional positions under multi-year technical contracts, including the Research Director for USAID’s Learning, Evaluation, and Analysis Project (LEAP) III (2018-2022), a Senior Advisor to the Economic Analysis division of the Millennium Challenge Corporation (MCC) (2018-2021), the Program Manager for the 5-year consulting contract with MCC on gender and social inclusion (GSI) (2021 - 2026), and the Lead Expert on a 5-year consulting contract for supporting the Economic Analysis division of MCC.
## Dr. Elspeth Murray
Elspeth Murray is an Associate Professor, Director of the Centre for Entrepreneurship, Innovation & Social Impact, and CIBC Fellow in Entrepreneurship at Smith School of Business, Queen’s University.
She served as Associate Dean (MBA and Master’s Programs) from 2012-2022 and has been a professor of Strategy and Entrepreneurship at Smith School of Business since 1996. Prior to joining Smith, she worked in industry for firms including IBM and Canadian Tire. Dr. Murray teaches on many MBA and Queen’s Executive Education programs for Smith School of Business.
As an integral part of her work in the strategy and new venture fields, Dr. Murray specializes in the management of change. In 2002, she co-authored a best-selling book, Fast Forward: Organizational Change in 100 Days, Oxford University Press, with Dr. Peter Richardson. Her current research is focused on understanding how organizations are reaping the benefits of embracing purpose beyond profits, and how society is benefiting as a result. Dr. Murray consults widely with firms. Current and past clients include BMW Canada, Torex Gold, Wawanesa Insurance, Versacold Logistics, Ontario’s Technical Safety Standards Authority, and the Auditor General for Canada. She serves as a Director for several firms and is an advisor to numerous start-ups and CEO's.

# [Our Insight Topics | Smith Business Insight](https://smith.queensu.ca/insight/tag.php?tid=Teams) 
 _https://smith.queensu.ca/insight/tag.php?tid=Teams_

 Smith Business Insight - Our Insight Topics 
[Skip to main content](#main-content)
Smith  
* [About](#)
 
 [Smith Home](/index.php)[Profile](/about/index.php)[News](/news_blog/index.php)[The Dean](/about/dean.php)[Strategic Plan](/about/strategic-plan.php)[Equity, Diversity, Inclusion & Indigenization](/about/EDII/index.php)[Learning Environment](/about/learning_environment.php)[Partnerships](/about/partners/index.php) [Services](/about/services.php) [SmithStore _​_](http://smithqueens.com/smithstore) [Queen's University _​_](https://queensu.ca)
 
* [Learning](#)
 
 [Explore Our Programs](/academic_programs/index.php)[Undergraduate Programs](/academic_programs/undergraduate.php) [MBA Programs](/mba_programs/index.php) [Graduate Programs](/grad_studies/index.php) [Executive Education](/executiveeducation/index.php)[Certificates](/academic_programs/certificates.php)[International](/international/index.php)[SmithEdge](/smithedge/index.php)[Academic Integrity](/about/academic_integrity/index.php)
 
* [Insights & Research](#)
 
 [Smith Business Insight](/insight/index.php) [Research](/research/index.php) [Publications](/about/publications.php) [Centres](/centres/index.php)
 
* [Faculty](#)
 
 [Meet Our Faculty](/faculty_and_research/faculty.php) [Join Our Ranks](/faculty_and_research/Join_Our_Ranks.php)
 
* [Alumni & Giving](#)
 
 [Give to Smith](https://smith.queensu.ca/invest/) [Alumni](/alumni/index.php)
 
* [Recruit & Engage](#)
 
 [Recruiting](/recruiting/index.php) [Partnerships](/about/partners/index.php) [Work with Students](/engage/index.php) [Smith Business Consulting](/centres/business-consulting/index.php)
 
Fresh ideas from [Smith School of Business](/index.php)
* [Topics](#)
 
 ### Categories
 
 * [Leadership](/insight/sections.php?sid=Leadership)
 * [Teams](/insight/sections.php?sid=Teams)
 * [Diversity](/insight/sections.php?sid=Diversity)
 * [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
 * [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
 * [Social Impact](/insight/sections.php?sid=Social%20Impact)
 * [Marketing](/insight/sections.php?sid=Marketing)
 * [Strategy](/insight/sections.php?sid=Strategy)
 * [Finance](/insight/sections.php?sid=Finance)
 
 ### Collections
 
 * [Our Emotions at Work](/insight/collection/Our-Emotions-at-Work.php)
 * [Speaking of Economics](/insight/collection/Speaking-of-Economics.php)
 * [The Age of Corporate Purpose](/insight/collection/the-age-of-corporate-purpose.php)
 * [How To Make Hybrid Work](/insight/collection/how-to-make-hybrid-work.php)
 * [All Collections](/insight/collections.php)
 
 ### Subscribe to Our Newsletter
 
 Cutting-edge research and expert advice delivered straight to your inbox.
 
 [Subscribe](/insight/newsletter.php)
 
* [Webinars](/insight/webinars.php)
* [Podcast](/insight/podcast/index.php)
* [Videos](/insight/video.php)
* [About](/insight/about.php)
Search
# Teams
## [It’s Time to Redefine the Confident Leader](/insight/content/Its-Time-to-Redefine-the-Confident-Leader.php)
Arrogance is so passé. There are better ways to demonstrate competence and capability at work
## [What Does It Take to Make Good Decisions?](/insight/content/What-Does-It-Take-to-Make-Good-Decisions.php)
Leaders often struggle with the hard choices before them. A well-defined process can put them on the right path
## [How Firms Create Entrepreneurial Competitors](/insight/content/How-Firms-Create-Entrepreneurial-Competitors.php)
It’s great when employees have psychological ownership in an organization. Until it isn’t
## [Ready to Build Your Board Career?](/insight/content/Ready-to-Build-Your-Board-Article.php)
Board service can be both satisfying and good for your resumé. But where to start? We spoke to experts for advice
## [How Peer Pressure Does the Manager’s Dirty Work](/insight/content/How-Peer-Pressure-Does-the-Managers-Dirty-Work.php)
Open office productivity gets a boost with a strategic approach to seating assignments
## [How to Approach Your Dream Mentor](/insight/content/How-to-Approach-Your-Dream-Mentor.php)
What’s really involved in asking someone to help you guide and shape your career? More than you think
## [The Pain Behind the Silence](/insight/content/The-Pain-Behind-the-Silence.php)
How depression and anxiety show up in work performance, and how leaders can respond
## [What Happens When Employees Become Owners?](/insight/content/What-Happens-When-Employees-Become-Owners.php)
Changes to federal income tax laws are expected to create a new era of employee ownership in Canada. That’s a good thing
## [Team Canada Athletes on How to Harness Pressure](/insight/content/Team-Canada-Harness-Pressure.php)
Eight elite athletes share lessons on managing high-stakes situations, whether you’re on a ball court or in a boardroom
## [Why We Keep Checking Our Email on Holidays](/insight/content/Why-We-Keep-Checking-Our-Email-Article.php)
Despite ample evidence for the benefits of unplugging, most of us have a hard time going out-of-office
## [How to Thrive as an Introverted Leader](/insight/content/How-to-Thrive-as-an-Introverted-Leader.php)
Extroverts tend to hog the spotlight, but you don’t have to be loud to make an impact
## [How to Craft a Cringe-Free Personal Brand](/insight/content/Crafting-a-Personal-Brand-Article.php)
Spelling out why you’re awesome may feel crass, but it can help you stand out to employers, peers and clients
[Load More](#)
## Editor’s Picks
1. [The New Rules of Public Speaking](/insight/content/The-New-Rules-of-Public-Speaking.php)
2. [The Untapped Potential of Customer Loyalty Plans](/insight/content/The-Untapped-Potential-of-Customer-Loyalty-Plans.php)
3. [How to Build Trusted Brands](/insight/content/How-to-Build-Trusted-Brands.php)
4. [How Catfish Effects Drive Stock Market Reform](/insight/content/How-Catfish-Effects-Drive-Stock-Market-Reform.php)
[Topics](#nav-menu-topics)
* [Leadership](/insight/sections.php?sid=Leadership)
* [Teams](/insight/sections.php?sid=Teams)
* [Diversity](/insight/sections.php?sid=Diversity)
* [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
* [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
* [Social Impact](/insight/sections.php?sid=Social%20Impact)
* [Marketing](/insight/sections.php?sid=Marketing)
* [Strategy](/insight/sections.php?sid=Strategy)
* [Finance](/insight/sections.php?sid=Finance)
[Collections](/insight/collections.php)
[Webinars](/insight/webinars.php)
[Podcast](/insight/podcast/index.php)
[Videos](/insight/video.php)
[About](/insight/about.php)
## Kingston
Goodes Hall 
Queen's University 
Kingston, Ontario 
Canada K7L 3N6
[1.877.533.2330](tel:+18775332330)
## Toronto
Simcoe Place 
200 Front Street West 
30th Floor
[416.365.7141](tel:+14163657141)
## Smith Programs
* [Undergraduate Programs](/academic_programs/undergraduate.php)
* [MBA Programs](/mba_programs/index.php)
* [Graduate Programs](/grad_studies/index.php)
* [Executive Education](/executiveeducation/index.php)
## Directories
* [Contact Us](/about/contact.php)
* [Smith Centres](/centres/index.php)
* [Smith Services](/about/services.php)
## Connect with Smith
* [Facebook](https://www.facebook.com/smithbusiness)
* [Instagram](https://www.instagram.com/smithbusiness/)
* [Twitter X](https://twitter.com/smithbusiness)
* [Linkedin](https://www.linkedin.com/company/smith-school-of-business-at-queen's-university)
* [WeChat](https://mp.weixin.qq.com/s/SoosIZFmLD0D01aSGJzgLw)
The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.
* [Give to Smith](/invest/ "Give to Smith")
* [Careers](/about/careers/ "Careers at Smith")
* [Program Portals](/academic_programs/student-portals.php "Program Portals")
* [Privacy](http://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy")
© Smith School of Business

# [Our Insight Topics | Smith Business Insight](https://smith.queensu.ca/insight/tag.php?tid=Sustainability) 
 _https://smith.queensu.ca/insight/tag.php?tid=Sustainability_

 Smith Business Insight - Our Insight Topics 
[Skip to main content](#main-content)
Smith  
* [About](#)
 
 [Smith Home](/index.php)[Profile](/about/index.php)[News](/news_blog/index.php)[The Dean](/about/dean.php)[Strategic Plan](/about/strategic-plan.php)[Equity, Diversity, Inclusion & Indigenization](/about/EDII/index.php)[Learning Environment](/about/learning_environment.php)[Partnerships](/about/partners/index.php) [Services](/about/services.php) [SmithStore _​_](http://smithqueens.com/smithstore) [Queen's University _​_](https://queensu.ca)
 
* [Learning](#)
 
 [Explore Our Programs](/academic_programs/index.php)[Undergraduate Programs](/academic_programs/undergraduate.php) [MBA Programs](/mba_programs/index.php) [Graduate Programs](/grad_studies/index.php) [Executive Education](/executiveeducation/index.php)[Certificates](/academic_programs/certificates.php)[International](/international/index.php)[SmithEdge](/smithedge/index.php)[Academic Integrity](/about/academic_integrity/index.php)
 
* [Insights & Research](#)
 
 [Smith Business Insight](/insight/index.php) [Research](/research/index.php) [Publications](/about/publications.php) [Centres](/centres/index.php)
 
* [Faculty](#)
 
 [Meet Our Faculty](/faculty_and_research/faculty.php) [Join Our Ranks](/faculty_and_research/Join_Our_Ranks.php)
 
* [Alumni & Giving](#)
 
 [Give to Smith](https://smith.queensu.ca/invest/) [Alumni](/alumni/index.php)
 
* [Recruit & Engage](#)
 
 [Recruiting](/recruiting/index.php) [Partnerships](/about/partners/index.php) [Work with Students](/engage/index.php) [Smith Business Consulting](/centres/business-consulting/index.php)
 
Fresh ideas from [Smith School of Business](/index.php)
* [Topics](#)
 
 ### Categories
 
 * [Leadership](/insight/sections.php?sid=Leadership)
 * [Teams](/insight/sections.php?sid=Teams)
 * [Diversity](/insight/sections.php?sid=Diversity)
 * [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
 * [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
 * [Social Impact](/insight/sections.php?sid=Social%20Impact)
 * [Marketing](/insight/sections.php?sid=Marketing)
 * [Strategy](/insight/sections.php?sid=Strategy)
 * [Finance](/insight/sections.php?sid=Finance)
 
 ### Collections
 
 * [Our Emotions at Work](/insight/collection/Our-Emotions-at-Work.php)
 * [Speaking of Economics](/insight/collection/Speaking-of-Economics.php)
 * [The Age of Corporate Purpose](/insight/collection/the-age-of-corporate-purpose.php)
 * [How To Make Hybrid Work](/insight/collection/how-to-make-hybrid-work.php)
 * [All Collections](/insight/collections.php)
 
 ### Subscribe to Our Newsletter
 
 Cutting-edge research and expert advice delivered straight to your inbox.
 
 [Subscribe](/insight/newsletter.php)
 
* [Webinars](/insight/webinars.php)
* [Podcast](/insight/podcast/index.php)
* [Videos](/insight/video.php)
* [About](/insight/about.php)
Search
# Sustainability
## [Our Top 10 Stories of 2024](/insight/content/Top-stories-of-2024.php)
Evolving leadership trends and technological advancements drove interest in our most popular content from the past year
## [How AI Can Help Make Wind Energy a Breeze](/insight/content/How-AI-Can-Help-Make-Wind-Energy-a-Breeze.php)
Wind turbines are expensive to build and maintain. Advanced technology can boost efficiency and ROI
## [Playing the Peak Pricing Game with AI and a Nudge](/insight/content/Playing-the-Peak-Pricing-Game-with-AI-and-a-Nudge.php)
An innovative study shows how big business and the environment can benefit by optimizing algorithms and human behaviour
## [Stakeholderism Needs a Reality Check](/insight/content/Stakeholderism-reality-check.php)
How should organizations resolve the inherent conflicting interests of modern capitalism?
## [A Marketer’s Meditation on Fly Fishing](/insight/content/A-Marketers-Meditation-Article.php)
What can a beloved summer pastime tell us about sustainably enjoying the natural world?
## [Empowering Women in Global Mining](/insight/content/Empowering-Women-in-Global-Article.php)
Canadian NGO shows how to bring real change to a rough and tumble sector
## [Green-Savvy Board Members Make Their Mark](/insight/content/Green-Savvy-Board-Members-Article.php)
A firm’s environmental performance rises with board member expertise and strong governance
## [Your Firm’s Most Undervalued Asset? Try Nature](/insight/content/Your-Firms-Most-Undervalued-Asset-Try-Nature.php)
Too few businesses understand the value of biodiversity — to the planet and their competitiveness
## [The Perks of Knowing Your Java’s Story](/insight/content/The-Perks-of-Knowing-Your-Javas-Story.php)
New research shows the economic value of traceability for coffee producers
## [Yes, Blockchain Does Have a Kryptonite](/insight/content/Yes-Blockchain-Does-Have-a-Kryptonite.php)
New research on supply chains reveals three vulnerabilities that can breach blockchain’s shield of trust
## [The Carbon Tax Signal](/insight/content/The-Carbon-Tax-Signal.php)
It may not make a dent in emissions, but the carbon tax can spur technological innovation
## [Why We Need to Supercharge Carbon Pricing](/insight/content/Why-We-Need-to-Supercharge-Carbon-Pricing.php)
A carbon emissions market is necessary but insufficient to reach climate targets. Here’s the case for clean tech subsidies and alternate financing
[Load More](#)
## Editor’s Picks
1. [The New Rules of Public Speaking](/insight/content/The-New-Rules-of-Public-Speaking.php)
2. [The Untapped Potential of Customer Loyalty Plans](/insight/content/The-Untapped-Potential-of-Customer-Loyalty-Plans.php)
3. [How to Build Trusted Brands](/insight/content/How-to-Build-Trusted-Brands.php)
4. [How Catfish Effects Drive Stock Market Reform](/insight/content/How-Catfish-Effects-Drive-Stock-Market-Reform.php)
[Topics](#nav-menu-topics)
* [Leadership](/insight/sections.php?sid=Leadership)
* [Teams](/insight/sections.php?sid=Teams)
* [Diversity](/insight/sections.php?sid=Diversity)
* [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
* [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
* [Social Impact](/insight/sections.php?sid=Social%20Impact)
* [Marketing](/insight/sections.php?sid=Marketing)
* [Strategy](/insight/sections.php?sid=Strategy)
* [Finance](/insight/sections.php?sid=Finance)
[Collections](/insight/collections.php)
[Webinars](/insight/webinars.php)
[Podcast](/insight/podcast/index.php)
[Videos](/insight/video.php)
[About](/insight/about.php)
## Kingston
Goodes Hall 
Queen's University 
Kingston, Ontario 
Canada K7L 3N6
[1.877.533.2330](tel:+18775332330)
## Toronto
Simcoe Place 
200 Front Street West 
30th Floor
[416.365.7141](tel:+14163657141)
## Smith Programs
* [Undergraduate Programs](/academic_programs/undergraduate.php)
* [MBA Programs](/mba_programs/index.php)
* [Graduate Programs](/grad_studies/index.php)
* [Executive Education](/executiveeducation/index.php)
## Directories
* [Contact Us](/about/contact.php)
* [Smith Centres](/centres/index.php)
* [Smith Services](/about/services.php)
## Connect with Smith
* [Facebook](https://www.facebook.com/smithbusiness)
* [Instagram](https://www.instagram.com/smithbusiness/)
* [Twitter X](https://twitter.com/smithbusiness)
* [Linkedin](https://www.linkedin.com/company/smith-school-of-business-at-queen's-university)
* [WeChat](https://mp.weixin.qq.com/s/SoosIZFmLD0D01aSGJzgLw)
The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.
* [Give to Smith](/invest/ "Give to Smith")
* [Careers](/about/careers/ "Careers at Smith")
* [Program Portals](/academic_programs/student-portals.php "Program Portals")
* [Privacy](http://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy")
© Smith School of Business

# [Julian Barling](https://smith.queensu.ca/faculty_and_research/faculty_list/barling-julian.php) 
 _https://smith.queensu.ca/faculty_and_research/faculty_list/barling-julian.php_

Professor of Organizational Behaviour & Borden Chair of Leadership at Smith School of Business
## Overview
Julian is the Borden Chair of Leadership at Smith School of Business, Queen’s University, and the author of _Brave New Workplace: Designing Productive, Healthy and Safe Organizations_ (2023) and _The Science of Leadership: Lessons From Research for Organizational Leaders_ (2014) both of which were published by Oxford University Press.
[Download Full CV _​_](https://smith.queensu.ca/faculty_and_research/faculty_list/CVs/Julian-Barling-CV1.pdf) [Download Image _​_](https://smith.queensu.ca/faculty_and_research/faculty_list/download_images/barling-julian.jpg)
### Academic Area
* Organizational Behaviour
### Interest Topics
* Behaviour & Psychology
* Leadership & Teams
### Highlights
#### Distinguished University Professor, and Borden Chair of Leadership
The Distinguished University Professor Program recognizes professors for exhibiting an outstanding and sustained research record, teaching excellence, and significant and lasting contributions to Queen’s, Canada, and the world.
#### Fellow of the Royal Society of Canada
The fellowship of the RSC comprises over 2000 Canadian scholars, artists, and scientists, peer-elected as the best in their field. These are distinguished men and women from all branches of learning who have made remarkable contributions in the arts, the humanities and the sciences, as well as in Canadian public life.
[Learn more about the fellowship](https://rsc-src.ca/en)  
## Faculty Details
### Profile
#### Full Bio
Julian is the author of _Brave New Workplace: Designing Productive, Healthy and Safe Organizations_ (2023) and _The Science of Leadership: Lessons From Research for Organizational Leaders_ (2014) both of which were published by Oxford University Press.
His research interests focus on the nature and development of transformational leadership and employee well-being, and he is also the author of well over 200 research articles and book chapters, and the author or editor of several books, including _Employment, Stress and Family Functioning_ (1990, Wiley & Sons); _The Union and Its Members: A Psychological Approach_ (1992, Oxford University Press); _Changing Employment Relations: Behavioral and Social Perspectives_ (1995, American Psychological Association); _Young Workers_ (1999, American Psychological Association); and _The Psychology of Workplace Safety_ (2004, American Psychological Association).  He is also co-editor of the _Handbook of Workplace Violence_ (2006, SAGE Publications), and senior editor of both the _Handbook of Work Stress_ (2005), _Handbook of Organizational Behaviour_ (2008), all published by SAGE, _The Psychology of Green Organizations_ (2015, Oxford University Press), and _Work and Sleep: Research Insights for the Workplace_ (Oxford University Press, 2016). 
Julian was formerly the editor of the American Psychological Association's _Journal of Occupational Health Psychology_, served as the chair of the American Psychological Association's Task Force on Workplace Violence in 2001-2, and was the chair of the Advisory Council on Occupational Health and Safety to the Ontario Minister of Labour from 1989-1991.
Julian is a Fellow for the Royal Society of Canada, the Society of Industrial and Organizational Psychology, the European Academy of Occupational Health Psychology, the Association for Psychological Science, and the Canadian Psychological Association. Julian has received numerous awards for his  research, including the Outstanding Career Contribution in Occupational Health Psychology from the European Association of Occupational Health Psychology in 2011, the Distinguished Scientific Contribution, Canadian Society for Industrial & Organizational Psychology in 2016, and the Lifetime Career Achievement in Research Award from the American Psychological Association, NIOSH, and the Society for Occupational Health Psychology in 2017. He received the Queen’s University Prize for “Excellence in Research” in 1997.
MacLean's magazine named Julian as one of Queen's University's most popular professors in 1996. Julian received the National Post's "Leaders in Business Education" award in 2001, and Queen's University's Award for Excellence in Graduate Student Supervision in 2008.
In an external analysis in 2018, Julian was ranked as one of the 10 most influential leadership researchers in the world
#### Academic Degrees
**PhD** 
Witwatersrand (1979)
**M.A.** 
Witwatersrand (1975)
**Bachelor of Arts (Honours) Psychology** 
Witwatersrand (1974)
**Bachelor of Arts** 
Witwatersrand (1973)
#### Academic Experience
**Smith School of Business, Queen’s University 
**Borden Chair of Leadership (2012 - Present) 
Associate Dean, Research, PhD & Programs (1999-2011) 
Chair, Research, PhD & Programs (1997-1999) 
Director, Executive MBA Program (1995-1996) 
Professor (1994 - Present)
**Institute for Work Psychology, University of Sheffield** Associate Member (1997-2004)
**Department of Psychology, Queen’s University 
**Professor (1988-1994) 
Chair, Graduate Program (1988-1991) 
Associate Professor (1984-1988)
**Department of Psychology, University of the Witwatersrand 
**Professor (1979-1984) 
Head, Division of Industrial Psychology (1979-1984) 
Lecturer/Senior Lecturer (1976-1979)
### Publications
#### Books
Barling, J. (2023). Brave new workplace: Designing productive, healthy and safe organizations. NY: 
Oxford University Press. 
• Reviewed in Occupational Health Sciences, September, 2023: 
[https://301eeb64-085b-44ae-b446-4b21262f8a96.filesusr.com/ugd/562aea\_a0d51f7415064c8da0e6633e6e94c33d.pdf](https://301eeb64-085b-44ae-b446-4b21262f8a96.filesusr.com/ugd/562aea_a0d51f7415064c8da0e6633e6e94c33d.pdf) 
• Reviewed in Globe and Mail, April 17th, 2023. Giving workers job autonomy may be the key to 
your leadership success. [https://www.theglobeandmail.com/business/careers/management/article-giving-workers-job-autonomy-may-be-the-key-to-your-leadership-success/](https://www.theglobeandmail.com/business/careers/management/article-giving-workers-job-autonomy-may-be-the-key-to-your-leadership-success/)     
• Reviewed in the Toronto Sun, July 12, 2023. Linda White. The Brave new workplace: Create 
environments in which employees can flourish: professor.
Barling, J., Barnes, C.M., Carleton, E., & Wagner, D.T. (2016) (Eds.) _Sleep and work: Research insights for the workplace_. NY: Oxford University Press.  [https://www.oxfordscholarship.com/view/10.1093/acprof:oso/9780190217662.001.0001/acprof-9780190217662](https://www.oxfordscholarship.com/view/10.1093/acprof:oso/9780190217662.001.0001/acprof-9780190217662)
Robertson, J.L., & Barling, J. (2015). (Eds.) _The Psychology of Green Organizations_. NY: Oxford University Press. [https://global.oup.com/academic/product/the-psychology-of-green-organizations-9780199997480?cc=ca&lang=en&](https://global.oup.com/academic/product/the-psychology-of-green-organizations-9780199997480?cc=ca&lang=en&)
Barling, J. (2014). _The Science of Leadership: Lessons from Research for Organizational Leaders_. NY: Oxford University Press. [https://global.oup.com/academic/product/the-science-of-leadership-9780199757015?cc=ca&lang=en&](https://global.oup.com/academic/product/the-science-of-leadership-9780199757015?cc=ca&lang=en&)
Barling, J., & Cooper, C.L. (2008) _The Sage Handbook of Organizational Behavior Vol. 1: Micro Approaches_. UK. Sage Publications. [https://sk.sagepub.com/reference/hdbk\_orgbehavior1](https://sk.sagepub.com/reference/hdbk_orgbehavior1)
Kelloway, E.K., Barling, J., & Hurrell, J.J. (2006) (Eds.) _Handbook of Workplace Violence_. CA: Sage. [https://sk.sagepub.com/reference/hdbk\_workviolence](https://sk.sagepub.com/reference/hdbk_workviolence)
Barling, J., Kelloway, E.K., & Frone, M. (2005) (Eds.) _Handbook of Work Stress_. CA: Sage Publications. [https://us.sagepub.com/en-us/nam/handbook-of-work-stress/book226100](https://us.sagepub.com/en-us/nam/handbook-of-work-stress/book226100)
Barling, J., & Frone, M. (2004) (Eds.) _The psychology of workplace safety_.  Washington, DC:  American Psychological Association. [https://psycnet.apa.org/record/2003-88217-000](https://psycnet.apa.org/record/2003-88217-000)
Barling, J., & Kelloway, E.K. (1999) (Eds.) _Young workers: Varieties of experience_. Washington, DC: American Psychological Association. [https://psycnet.apa.org/record/1999-02025-000](https://psycnet.apa.org/record/1999-02025-000)
Tetrick, L.E., & Barling, J.  (1995) (Eds.) _Changing employment relations:  Behavioral and social perspectives_.  Washington, D.C.:  American Psychological Association. [https://psycnet.apa.org/record/1995-99042-000](https://psycnet.apa.org/record/1995-99042-000)
Barling, J., Fullagar, C., & Kelloway, E.K. (1992). _The union and its members:  A psychological perspective_.  New York: Oxford University Press. [https://global.oup.com/academic/product/the-union-and-its-members-9780195073362?cc=ca&lang=en&](https://global.oup.com/academic/product/the-union-and-its-members-9780195073362?cc=ca&lang=en&)
Barling, J. (1990).  _Employment, stress and family functioning_.  London:  John Wiley and Sons. [https://www.amazon.ca/Employment-stress-family-functioning-Barling/dp/0471917737/ref=sr\_1\_1?keywords=julian+barling+work+stress+and+employment+functioning&qid=1578496064&sr=8-1](https://www.amazon.ca/Employment-stress-family-functioning-Barling/dp/0471917737/ref=sr_1_1?keywords=julian+barling+work+stress+and+employment+functioning&qid=1578496064&sr=8-1)
Barling, J., Fullagar, C., & Bluen, S. (Eds.) (1986).  _Behaviour in organizations:  South African perspectives_ (2nd ed).  Johannesburg:  McGraw Hill.
Barling, J. (Ed.) (1983).  _Behaviour in organizations:  South African perspectives_.  Johannesburg:  McGraw Hill.
Beaty, D., & Barling, J. (1982).  _Positive exam results without stress_.  Johannesburg:  McGraw Hill.
#### **Manuscripts**
Barling, J., Granger, S., Weatherhead, J., Turner, N., & Pupco, S. (2020) Children’s self-control mediates the relationship between early socioeconomic status and later leader role emergence: A multi-context, multi-source lifespan study (Under first review at _Journal of Applied Psychology_).
Barling, J., Granger, S., Weatherhead, J., Turner, N. (2019). Persistence and timing of family socioeconomic adversity and affluence and children’s later leadership role occupancy. (To be submitted to _Organizational Science_)
Cloutier, A., & Barling, J. (2020). Romantic Relationships Affect Leadership Quality: An Experiment. (Revision requested by the _Journal of Applied Psychology_)
Cloutier, A., & Barling, J. (2019). Perceptions, Expectations and Realities of Leaders’ Mental Health. (To be submitted to the _Journal of Occupational Health Psychology_).
Suurd Ralph, C., & Barling, J. Leader Inconsistency, Subjective Attitude Ambivalence and Follower Outcomes (Under first review at _Journal of Applied Psychology_)
Trivisonno, M., & Barling, J. A passion for leadership: Model conceptualization and development of a measure. (Under first review at the _European_ _Journal of Work and Organizational Psychology_.)
Barling, J., Carleton, E., Trivisonno, M., McEvoy, A., & Dupre, K. Why does my leader just do nothing? Personal predictors of passive leadership behaviors. (Under first review at the _Journal of Business and Psychology.)_
#### Journal Articles
Lyubykh, Z., Biricik Gulseren, D., Turner, N., Barling, J., & Seifert, M. (in press). Shared Transformational Leadership and Safety Behaviors of Employees, Leaders, and Teams: A Multilevel Investigation. _Journal of Occupational and Organizational Psychology._
Lyubykh, Z., Dupré, K.E., Barling, J., & Turner, N. (in press). Retaliating against abusive supervision with aggression and violence: The moderating role of organizational intolerance of aggression. _Work & Stress._
Turner, N., Barling, J., Dawson, J.F., Deng, C., Parker, S.K., Patterson, M.G., & Stride, C.B. (in press). Human resource management and organizational injury rates. _Journal of Safety Research_
Arnold, K.A., Turner, N., Barling, J., & Iverson, R. (in press). Feeling safe while doing sex work: Motivation for entering sex work moderates the relationship between perceptions of physical danger and desire to leave sex work. _Safety Science_.
Lyubykh, Z., Turner, N., Barling, J., Reich, T.C., & Batten, S. (2021). Employee disability disclosure and managerial prejudices in the return-to-work context. _Personnel Review, 50_, 770-778.
Carleton, E., & Barling, J. (2020). Indirect effects of obstructive sleep apnea on work withdrawal: A quasi-experimental treatment outcome study. _Journal of Occupational Health Psychology, 25_, 426-438.
Turner, N., Deng, C, Barling, J. & Spencer, K. (2020). Differential mental health consequences of strikes and lockouts. _Canadian Journal of Behavioral Science, 52_, 149-153. [https://doi.org/10.1037/cbs0000161](https://psycnet.apa.org/doi/10.1037/cbs0000161)
Dionisi, A., & Barling, J. (2019). What happens at home doesn’t stay at home: The role of family and romantic partner conflict in destructive leadership. _Stress and Health, 35,_ 304-317. [https://onlinelibrary.wiley.com/doi/abs/10.1002/smi.2858](https://onlinelibrary.wiley.com/doi/abs/10.1002/smi.2858)
Carleton, E., & Barling, J. (2018). Adult ADHD Symptoms and Passive Leadership: The Mediating Role of Daytime Sleepiness. _Stress and Health_. _Stress and Health, 34_, 663-673. [https://onlinelibrary.wiley.com/doi/abs/10.1002/smi.2833?af=R](https://onlinelibrary.wiley.com/doi/abs/10.1002/smi.2833?af=R)
Carleton, E., Barling, J., & Trivisonno, M. (2018). Leaders' trait mindfulness and transformational leadership: The mediating roles of leaders' positive affect and leadership self-efficacy. _Canadian Journal of Behavioural Science,_ 50, 185-194_._
Robertson, J., Dionisi, A.M., & Barling, J. (2018). Linking attachment theory to abusive supervision. _Journal of Managerial Psychology, 33_, 214-228.
Dionisi, A., & Barling, J. (2018). It Hurts Me Too: Examining the Impact of Male Gender Harassment on Observers’ Well-Being and Emotions. _Journal of Occupational Health Psychology, 23_, 303-319. [https://psycnet.apa.org/fulltext/2018-29381-001.pdf](https://psycnet.apa.org/fulltext/2018-29381-001.pdf)
Barling, J., Akers, A., & Beiko, D. (2018). The Impact of Positive and Negative Intraoperative Surgeons’ Leadership Behaviors on Surgical Team Performance. _American Journal of Surgery,_ 215, 14-18.
Byrne, A., & Barling, J. (2017). When she brings home the job status: Non-normative job status inconsistencies, status leakage and marital instability. _Organization Science, 28(2)_, 177-192.
Robertson, J., & Barling, J. (2017). Contrasting the Nature and Effects of Environmentally-Specific and General Transformational Leadership. _Journal of Leadership and Organizational Studies, 38,_ 22-41.
Robertson, J., & Barling, J. (2017). Toward a New Measure of Organizational Environmental Citizenship Behavior. _Journal of Business Research_, _75_, 57-66.
Barling, J., & Cloutier, A. (2017). Leaders’ mental health at work: Empirical, methodological and policy directions. _Journal of Occupational Health Psychology, 22,_ 394-406.
Barling, J., & Frone, M.R. (2017).
If only my leader would just do _something_! Passive leadership undermines employee well-being through role stressors and psychological resource depletion. _Stress and Health, 33,_ 211-222.
Barling, J., & Weatherhead, J. (2016). Persistent exposure to poverty limits later leader emergence. _Journal of Applied Psychology_, _101_, 1305-1318.
Beiko, D., Barling, J., Houle, A.M., Davies, T.O., & Oake, J.S. (2016). Exploring the business of urology: Leadership. _Canadian Urological Association Journal_, 10, 241-245.
Carleton, E., Barling, J., Christie, A., Trivisonno, M., Tulloch, K., & Beachamp, M. (2016). Scarred for the rest of my career? Career-long effects of abusive leadership on professional athlete aggression and task performance. _Journal of Sport and Exercise Psychology, 38,_ 409-422.
Dupré, K., & Barling, J. (2015). Organizational safety and outcomes for families. _Psynopsis: Canada’s Psychology Magazine, 37(4), 12-13_. (Invited article). [http://www.cpa.ca/docs/File/Psynopsis/fall2015/index.html](http://www.cpa.ca/docs/File/Psynopsis/fall2015/index.html)
Dionisi, A.M., & Barling, J. (2015). Spillover and crossover of sex-based harassment from work to home: Supervisor gender harassment affects romantic relationship functioning via targets’ anger. _Journal of Organizational Behavior, 36_, 196-215.
Dupré, K., Dawes, K., & Barling, J. (2014) Harm to those who serve: Effects of direct and vicarious customer-initiated workplace aggression. _Journal of Interpersonal Violence, 29_, 2355-2377.
LeBlanc, M., Barling, J., & Turner, N. (2014). Intimate partner aggression and women’s work outcomes. _Journal of Occupational Health Psychology, 19_, 399-412.
Bergenwall, A., Kelloway, E.K., & Barling, J. (2014). Odd jobs, bad habits and ethical implications: Smoking-related outcomes of children's early employment intensity. _Journal of Business Ethics, 122_, 269-282.
Beauchamp, M. R., Liu, Y., Morton, K. L., Martin, L. J., Wilson, A. H., Wilson, A. J., Sylvester, B. D., Zumbo, B. D., & Barling, J. (2014). Transformational Teaching and Adolescent Physical Activity: Multilevel and Mediational Effects. _International Journal of Behavioral Medicine, 21_, 537-546_._
Byrne, A., Dionisi, A., Barling, J., Akers, A., Robertson, J., Lys, R., Wylie, J., & Dupré, K. (2014). The Depleted Leader: The influence of leaders' diminished psychological resources on leadership behaviors. _Leadership Quarterly, 25, 344-357_. (Nominated for the 2014 LQ Best Paper Award.)
Byrne, A., Barling, J., & Dupré, K.E. (2014). Leader apologies and employee and leader well-being. _Journal of Business Ethics, 121_, 91-106.
Christie, A.M. & Barling, J. (2014). When what you want is what you get: Pay dispersion and communal sharing preference. _Applied Psychology: An International Review, 63,_ 541-563_._  
Robertson, J., & Barling, J. (2013). Greening organizations through leaders’ influence on employees’ pro-environmental behaviors. _Journal of Organizational Behavior, 34_, 176-194. (Received the Citation of Excellence from Emerald Group Publishing)
Hoption, C.B., Turner, N., & Barling, J. (2013). It's not you, it's me: Transformational leadership and self-deprecating humor. _Leadership and Organizational Development Journal, 34_, 4-19_._
Arnold, K.A., Turner, N., Barling, J., Kelloway, E.K., & McKee, M. (2013). Transformational leadership and psychological well-being: The mediating role of meaningful work. In C.L. Cooper & I.T. Robertson (Eds.) _Management and happiness_ (pp. 93-103). London: Edward Elgar. (Reprinted from _Journal of Occupational Health Psychology_, 2007, _12_, pp. 193-203).
Dionisi, A.M., Barling, J., & Dupré, K. (2012). Revisiting the comparative outcomes of workplace aggression and sexual harassment. _Journal of Occupational Health Psychology, 14_, 398-408_._
Hoption, C.B., Christie, A., & Barling, J. (2012). Submitting to the Follower Label: Followership, Positive Affect and Extra-Role Behaviors. _Journal of Psychology,_ _220(4),_ 221-230. (Special Issues: "Follower centric Approaches to Leadership").
Simola, S.K., Barling, J., & Turner, N. (2012). Transformational leadership and leaders’ mode of care reasoning. _Journal of Business Ethics, 108_, 229-237.
Kelloway, E.K., Turner, N., Barling, J., & Loughlin, C.A. (2012). Transformational leadership, transactional leadership, and employee psychological well-being: The mediating role of trust. _Work and Stress, 26_, 39-55.
Christie, A., Barling, J. & Turner, N. (2011). Pseudo-transformational leadership: Model specification and outcomes. _Journal of Applied Social Psychology, 41_, 2943-2984.
Morton, K., Barling, J., Beauchamp, M., Masse, L., Zumbo, D., & Rhodes, R.E. (2011). The Application of Transformational Leadership Theory to Parenting: Questionnaire Development and Implications for Adolescent Self-Regulatory Efficacy and Life Satisfaction. _Journal of Sport & Exercise Psychology, 33_, 688-709.
Beauchamp, M.R., Barling, J., & Morton, K. (2011) Transformational Teaching and Adolescent Self-determined motivation, self-efficacy, and intentions to engage in leisure time physical activity: A Randomized Controlled Pilot Trial. _Applied Psychology: Health and Well-Being, 3_, 127-150_._
Mendelson, M.B., Turner, N., & Barling, J.  (2011). Perceptions of the presence and effectiveness of high involvement work systems and their relationship to employee attitudes: A test of competing models. _Personnel Review,_ 40, 45-69.
Kelloway, E.K., & Barling, J. (2010). Leadership development as an intervention in occupational health psychology. _Work and Stress_, 24, 260-279.
Dupré, K.E., Barling, J., Turner, N., & Stride, C.B. (2010). Comparing Perceived Injustices from Supervisors and Romantic Partners as Predictors of Aggression. _Journal of Occupational Health Psychology,_ 15_,_ 359-370.
Beauchamp, M.R., Barling, J., Li, Z., Morton, K.L., Keith, S.E., & Zumbo, B.D. (2010). Development and psychometric properties of the Transformational Teaching Questionnaire. _Journal of Health Psychology,_ 15, 1123-1134.
Christie, A., & Barling, J. (2010). Beyond status: Relating status inequality to performance and health in teams.  _Journal of Applied Psychology_, 95, 920-934.
Hershcovis, M.S., & Barling, J. (2010). Comparing victim attributions and outcomes for workplace aggression and sexual harassment.  _Journal of Applied Psychology, 95_, 874-888.
Morton, K.L., Barling, J., Rhodes, R.E., Masse, L., Zumbo, B.D., & Beauchamp, M.R. (2010). Extending transformational leadership theory to parenting and adolescent health behaviors: An integrative and theoretical review. _Health Psychology Review_, 4, 128-157.
Inness, M., Turner, N., Barling, J., & Stride, C.B. (2010). Transformational leadership and employee safety performance: A within-person, between-job design.  _Journal of Occupational Health Psychology,_ 15, 279-290.
Tucker, S., Turner, N., Barling, J., & McEvoy, M. (2010). Transformational leadership and children’s aggression in team setting: A short-term, longitudinal study. _Leadership Quarterly,_ 21, 389-399.
Simola, S.K., Barling, J., & Turner, N. (2010). Transformational leadership and leader moral orientation: Contrasting an ethic of justice and an ethic of care. _Leadership Quarterly,_ 21, 179-188.
Hershcovis, M. S & Barling, J. (2010). Towards a multi-foci approach to workplace aggression: A meta-analytic review of outcomes from different perpetrators. _Journal of Organizational Behavior._ 31, 24-44.
Christie, A.M., & Barling, J. (2009). Disentangling the Indirect Links between SES and Health: The dynamic roles of work stressors and personal control. _Journal of Applied Psychology_, 94, 1466-1478.
Inness, M., LeBlanc, M., & Barling, J. (2008). Psychosocial predictors of supervisor-, peer-, subordinate-, and service provider-targeted aggression. _Journal of Applied Psychology,_ 93, 1401-1411_._
Barling, J., Christie, A., & Turner, N.  (2008). Pseudo-transformational leadership: Toward the development and test of a model.  _Journal of Business Ethics_, 81, 851-861.
Inness, M., Barling, J., Turner, N., & Rogers, K. (2007).  De-marketing tobacco through price changes and consumer attempts to quit smoking_._  _Journal of Business Ethics_, 77, 405-416.
Arnold, K.A., Turner, N., Barling, J., Kelloway, E.K., & McKee, M. (2007).  Transformational leadership and psychological well-being: The mediating role of meaningful work.  _Journal of Occupational Health Psychology,_ 12, 193-203.
Carson, J., Barling, J., & Turner, N. (2007).  Group alcohol climate, alcohol consumption, and student performance.  _Group Dynamics: Theory, Research and Practice_, 11, 31-41.
Zacharatos, A., Hershcovis, M.S., Turner, N., & Barling, J. (2007).  Human resource management in the North American automobile industry: A meta-analysis.  _Personnel Review,_ 36, 231-254.
Hershcovis, S., Turner, N., Barling, J, Arnold, K., Dupré, K., Inness, M., Leblanc, M., & Sivanathan, N. (2007).  Predicting workplace aggression: A meta-analytic approach.  _Journal of Applied Psychology_, 92, 228-238.
Dupré, K., Inness, M., Connelly, C.E., Barling, J., & Hoption, C.  (2006). Workplace aggression in teenage part-time employees.  _Journal of Applied Psychology._ 91, 987-997.
Dupré, K., & Barling, J. (2006). Predicting and preventing supervisory workplace aggression.  _Journal of Occupational Health Psychology_, 11, 13-26.
Tucker, S., Turner, N., Barling, J., Reid, E., & Elving, C. (2006).  Apologies and transformational leadership.  _Journal of Business Ethics,_ 63, 195-207.
Barling, J. (2005).  Editorial: “And now, the time has come…”.  _Journal of Occupational Health Psychology,_ 10, 307-309.
Inness, M., Barling, J., & Turner, N. (2005). Understanding supervisor-targeted aggression:  A within-person, between-jobs design.  _Journal of Applied Psychology,_ 90, 731-739.
Zacharatos, A., Barling, J., & Iverson, R.D. (2005).  High performance work systems and occupational safety.  _Journal of Applied Psychology_, 90, 77-93.
Francis, L., & Barling, J. (2005). Organizational injustice and psychological strain.  _Canadian Journal of Behavioral Science,_ 37, 250-261.
LeBlanc, M. M., & Barling, J. (2004).   Workplace aggression.  _Current Directions in Psychological Science,_ 13, 9-12.
Barling, J., Kelloway, E.K., & Iverson, R.D.  (2003). High quality work, members’ employee morale and occupational injuries.  _Journal of Applied Psychology_, 88, 276-283.
Barling, J., Kelloway, E.K., & Iverson, R.D. (2003). Accidental outcomes: Attitudinal consequences of workplace injuries.  _Journal of Occupational Health Psychology_, 8, 74-85.
Kelloway, E.K., Barling, J., Kelley, E., Comtois, J., & Gaitan, B. (2003).  Remote transformational leadership.  _Leadership and Organization Development Journal,_ 24(3_)_, 163-171.
Barling, J., Loughlin, C., & Kelloway, E.K. (2002).  Development and test of a model linking safety-specific transformational leadership and occupational safety.  _Journal of Applied Psychology,_ 87, 488-496.
Turner, N., Barling, J., Epitropaki, O., Butcher, B., & Milner, C.  (2002). Transformational leadership and moral reasoning.  _Journal of Applied Psychology_, 87, 304-311.
Barling, J. (2002).  Editorial.  _Journal of Occupational Health Psychology,_ 7, 1-2.
Kelloway, K., Loughlin, C., Barling, J., & Nault, A. (2002). Counterproductive and organizational citizenship behaviors: separate but related constructs. _International Journal of Selection and Assessment_, 10(1-2), 143-151.
Barling, J., Rogers, A.J., & Kelloway, E.K.  (2001). Behind closed doors:  Organizational and personal consequences of sexual harassment and workplace violence for in-home workers.  _Journal of Occupational Health Psychology,_ 6, 255-269.
Loughlin, C., & Barling, J. (2001).  Young workers' work values, attitudes, and behaviours.  _Journal of Occupational and Organizational Psychology,_ 74, 543-558. (Invited article in special centennial issue of the British Psychological Society.)
Arnold, K.A., Barling, J. & Kelloway, E.K. (2001). Transformational leadership or the iron cage: Which predicts trust, commitment and team efficacy? _Leadership and Organization Development Journal,_ 22,  315-320.
Hepburn, C.G., & Barling, J.  (2001). To vote or not to vote:  Abstaining in union representation elections.  _Journal of Organizational Behavior_, 22, 569-592.
Charbonneau, D., Barling, J., & Kelloway, E.K. (2001). Transformational leadership and sports performance:  The mediating role of intrinsic motivation.  _Journal of Applied Social Psychology_, 31, 1521-1534.
Kelloway, E.K., & Barling, J.  (2000). Knowledge work as organizational behavior.  _International Journal of Management Reviews_, 2, 287-304.
Barling, J. (2000).  Editorial.  _Journal of Occupational Health Psychology, 5_, 1-2.
Barling, J. (2000). A response to Kokko and Pulkkinen's "Aggression in childhood and long-term unemployment in adulthood." _Prevention & Treatment_, 3, Article 33. Available on the World Wide Web:  [http://journals.apa.org/prevention/volume3/pre0030033c.html](http://journals.apa.org/prevention/volume3/pre0030033c.html)
Kelloway, E.K., & Barling, J. (2000).  What we have learned about developing transformational leaders. _Leadership and Organization Development Journal,_ 21, 355-362.
Zacharatos, A., Barling, J., & Kelloway, E.K.  (2000) Development and effects of transformational leadership in adolescents.  _Leadership Quarterly,_ 11, 211-226.
Barling, J., Slater, F., & Kelloway, E.K. (2000).  Transformational leadership and emotional intelligence:  An exploratory study.  _Leadership and Organization Development Journal,_ 21, 157-161.
Barling, J., & Hutchinson, I. (2000).   Commitment vs. control-oriented safety practices, safety reputation and perceived safety climate.  _Canadian Journal of Administrative Science,_ 17, 76-84.
Kelloway, E.K., & Barling, J. (2000, June/July).  Developing transformational leaders:  How do you do it and does it matter?  _HR Professional_, 45-49.
Kelloway, E.K., Barling, J., & Helleur, J. (2000).  Enhancing transformational leadership:  The roles of training and feedback. _Leadership and Organization Development Journal,_ 21, 145-149.
Barling, J., Zacharatos, A., & Hepburn, C.G. (1999).  Parents’ job insecurity affects children’s academic performance through cognitive difficulties.  _Journal of Applied Psychology,_ 84, 437-444.
Barling, J., & Mendleson, M.B.  (1999). Parents’ job insecurity affects children’s grade school performance via the mediating effect of beliefs in an unjust world and negative mood.  _Journal of Occupational Health Psychology,_ 4, 347-355.
Greenberg, L., & Barling, J.  (1999). Predicting employee aggression against coworkers, subordinates and supervisors.  _Journal of Organizational Behavior,_ 20, 897-913.
Kelloway, E.K., & Barling, J. (1999).  When children work:  implications for youth, society and organizations.  _International Journal of Management Reviews_, 1, 159-170.
Sauter, S.L., Hurrell, J.J., Fox, H., Tetrick, L.E., & Barling, J.  (1999). Occupational health psychology:  An emerging discipline.  _Industrial Health,_ 37, 199-211.
Barling, J., Dupré, K., & Hepburn, C.G. (1998).  Effects of parents’ job insecurity on children’s work beliefs and attitudes_.  Journal of Applied Psychology,_ 83, 112-118. (Translated into Polish and reprinted as:  “Wplpw poczucia niepewnosci zawodowej rodzicow na prezentowane prezez ich dzieci przekonania I postawy wobec pracy” Wychowanie na co dzien, 1998, 7-10.)
Loughlin, C.A., & Barling, J.  (1998). Teenagers’ part-time employment and their work-related attitude and aspirations.  _Journal of Organizational Behaviour,_ 19, 197-207.
Dekker, I., & Barling, J. (1998).  Personal and organizational predictors of workplace sexual harassment of women by men. _Journal of Occupational Health Psychology,_ 3, 7-18.
Adams-Roy, J., & Barling, J. (1998). Predicting the decision to confront or report sexual harassment.  _Journal of Organizational Behaviour,_ 19, 329-336.
Kelloway, E.K., Barling, J., & Harvey, S.  (1998). Changing employment relations:  What can unions do?  _Canadian Psychology,_ 39, 124-132.
Wright, B., & Barling, J.  (1998). “The executioner’s song”:  Listening to downsizers reflect on their experiences.  _Canadian Journal of Administrative Sciences,_ 15, 339-355.
Kelloway, E.K., Barling, J., & Carroll, A.  (1998). Perceived causes and consequences of property rights to jobs.  _Journal of Business and Psychology,_ 12, 505-514.
Dekker, I., Greenberg, L., & Barling, J. (1998). Predicting union attitudes in student part-time workers.  _Canadian Journal of Behavioural Science,_ 30, 49-55.
Stewart, W., & Barling, J. (1996). Fathers’ work experiences effect children’s behavior via job-related affect and parenting behaviors.  _Journal of Organizational Behavior_, 221-232.
Barling, J., Weber, T., & Kelloway, E.K.  (1996). Effects of transformational leadership training on attitudinal and financial outcomes:  A field experiment.  _Journal of Applied Psychology,_ 81, 827-832.
Kelloway, E.K., Barling, J., & Agar, S. (1996).  Pre-employment predictors of children’s union attitudes:  The moderating role of identification with parents.  _Journal of Social Psychology,_ 136, 413-415.
Barling, J., Dekker, I., Loughlin, C., Kelloway, E.K., Fullagar, C., & Johnson, D. (1996).  Prediction and replication of the organizational and personal consequences of workplace sexual harassment.  _Journal of Managerial Psychology,_ 11(5), 4-25.
Hepburn, C.G., & Barling, J. (1996).  Eldercare responsibilities, interrole conflict and employee absence:  A daily study.  _Journal of Occupational Health Psychology,_ 1, 311-318.
Steele, J., & Barling, J. (1996). Influence of maternal sex-role beliefs and role satisfaction on daughters’ vocational interests. _Sex Roles_, 34,637-648.
Barling, J., & Kelloway, E.K. (1996).  Job insecurity and health:  The moderating role of workplace control. _Stress Medicine,_ 12, 253-260.
Barling, J., Kelloway, E.K., & Cheung, D. (1996).  Time management and achievement striving interact to predict car sales performance.  _Journal of Applied Psychology_, 81, 821-826.
Stewart, W., & Barling, J. (1996).  Daily work stressors, mood and interpersonal job performance:  A meditational model.  _Work and Stress_, 4, 336-351.
Dekker, I., Barling, J., & Kelloway, E.K. (1996).  Work force size and multifaceted job satisfaction:  A cross-national investigation.  _Journal of Social Psychology_, 136, 201-208.
Barling, J., Kelloway, E.K., & Rogers, K., (1995).  Some effects of teenagers’ part-time employment:  The quantity and quality of work make the difference_.  Journal of Organizational Behavior,_ 16, 143-154 (Reprinted in: Stone, P., & Cannon, M. (Eds). (1997) Organizational psychology (Volume 3) (pp. 145-156).  UK:  Ashgate. 
Barling, J., & Boswell, R. (1995).  Work performance and the achievement striving and impatient-irritability dimensions of type A behaviour.  _Applied Psychology:  An International Review,_ 44, 143-153.
MacEwen, K.E., Barling, J., Kelloway, E.K., & Higginbottom, S.F. (1995).  Predicting retirement anxiety:  The roles of parental socialization and personal planning.  _Journal of Social Psychology_, 135, 203-213.
Dekker, I., & Barling, J. (1995).  Workforce size and role-related stress.  _Work and Stress,_ 9, 45-54.
Barling, J. (1995).  Work and family:  In search of the missing links.  _Employee Counselling Today,_ 7 (7), 18-27.  (Reprinted from the _Journal of Employee Assistance Research_, 1992, I, with permission).
Barling, J., Kelloway, E.K., & Fullagar, C. (1995).  The role of transformational leadership in shop steward effectiveness.  _Workplace Topics_, 4(2), 59-70.
MacEwen, K.E., & Barling, J. (1994).  Maternal employment experiences affect children’s behavior via mood, cognitive difficulties and parenting behavior:  A reply to Otto and Atkinson.  _Journal of Marriage and the Family,_ 56, 507-510.
Barling, J., MacEwen, K.E., Kelloway, E.K., & Higginbottom, S.F. (1994). Predictors and outcomes of elder care-based interrole conflict.  _Psychology and Aging,_ 9, 391-397.
Henningfield, J.E., Ramstrom, L.M., Husten, C., Giorino, G., Barling, J., Weber, C., Kelloway, E.K., Strecher, V.J., & Jarvis, M.J. (1994). Smoking and the workplace:  Realities and solutions.  _Journal of Smoking-Related Diseases_, 5, 261-270.
MacEwen, K.E., & Barling, J. (1994).  Daily consequences of work interference with family and family interference with work.  _Work and Stress,_ 8, 244-254.
Kelloway, E.K., & Barling, J. (1993). Member’s participation in local union activities:  Measurement, prediction, replication.  _Journal of Applied Psychology_, 262-279.
Barling, J., MacEwen, K.E., & Nolte, M.L. (1993). Homemaker role experiences affect toddler behaviors via maternal well-being and parenting behavior.  _Journal of Abnormal Child Psychology,_ 21, 213-229.
Kelloway, E.K., Barling, J., & Shah, A.  (1993). Industrial relations stress and job satisfaction:  Concurrent effects and mediation.  _Journal of Organizational Behaviour_, 14, 447-458.
Higginbottom, S., Barling, J., & Kelloway, E.K. (1993).  Linking retirement experiences and marital satisfaction:  A mediational model.  _Psychology and Aging,_ 8, 508-516.
MacEwen, K., & Barling, J. (1993). Type A behavior and marital satisfaction:  Differential effect of achievement striving and impatience/irritability.  _Journal of Marriage and the Family,_ 55, 1001-1010.
Barling, J., & Phillips, M. (1993). Interactional, formal and distributive justice in the workplace:  An exploratory study.  _Journal of Psychology,_ 127, 649-656.
Barling, J., & MacIntyre, A. (1993).  Daily work role stress, mood and emotional exhaustion.  _Work and Stress_, 7, 315-325.
Barling, J., & Charbonneau, D. (1992).  Disentangling the relationship between achievement striving and impatience-irritability dimensions of type A behaviour, performance and health.  _Journal of Organizational Behaviour,_ 13, 369-377.
MacEwen, K., Barling, J., & Kelloway, E.K. (1992).  Effects of short-term role overload on marital interactions _Work and Stress,_ 6, 117-126.
Barling, J., & MacEwen, K.E. (1992). Linking work experiences with facets of marital functioning.  _Journal of Organizational Behavior,_ 13, 573-584.
Barling, J., Fullagar, C., Kelloway, E.K., & McElvie, L. (1992). Union loyalty and strike propensity.  _Journal of Social Psychology,_ 132, 581-590.
Barling J. (1992). Work and family: In search of the missing links. _Journal of Employee Assistance Research,_ 1, 271-285.
Fullagar, C., Barling, J., & Christie, P. (1991).  Dual commitment in aggressive and protective unions.  _Applied Psychology:  An International Review_, 40, 93-104.
Fullagar, C., & Barling, J. (1991). Predictors and outcomes of different patterns of organizational and union loyalty_.  Journal of Occupational Psychology,_ 64, 129-143.
Barling, J. (1991).  Work and life: Getting it all together.  _Contemporary Psychology,_ 36, 509-510.
Barling, J., Kelloway, E.K., & Bremermann, E.H. (1991). Pre-employment predictors of union attitudes:  The role of family socialization and work beliefs.  _Journal of Applied Psychology,_ 76, 725-731.
MacEwen K.E., & Barling, J. (1991).  Maternal employment experiences affect children’s behaviour via mood, cognitive difficulties and parenting behavior.  _Journal of Marriage and the Family,_ 53, 635-644.
Barling, J., & MacEwen, K.E. (1991).  Maternal employment experiences, attention problems and behavioural performance:  A mediational model.  _Journal of Organizational Behaviour,_ 12, 495-505.
Kelloway, E.K., & Barling J. (1991).  Job characteristics, role stress and mental health.  _Journal of Occupational Psychology_, 64, 291-304.
Barling, J., Kryl, I.P., & Bluen, S.D. (1990). “Finally, all the questionnaires are back”:  Bias in the time taken to return survey questionnaires.  _Personality and Individual Differences,_ 11, 177-180.
Barling, J., Wade, W.C., & Fullagar, C. (1990). Predicting employee commitment to company and union:  Divergent models.  _Journal of Occupational Psychology,_ 63, 49-61.
Bluen, S.D., Barling, J., & Burns, W. (1990). Predicting sales performance, job satisfaction and depression by using the achievement strivings and impatience-irritability dimensions of Type A behavior.  _Journal of Applied Psychology,_ 75, 212-216.
Barling J., Bluen, S.D., & Moss, V. (1990). Dimensions of Type A behavior and marital dissatisfaction.  _Journal of Psychology, 124_, 311-319.
Barling, J., & Kryl, I. (1990). Moderators of the relationship between daily work stress and mood.  _Work and Stress,_ 4, 319-329.
Kelloway, E.K., & Barling, J. (1990). Item content vs. item wording:  Disentangling role conflict and role ambiguity_.  Journal of Applied Psychology,_ 75, 738-742.
Fullagar, C., & Barling, J. (1989). A longitudinal test of a model of the antecedents and consequences of union loyalty. _Journal of Applied Psychology,_ 74, 213-227.
O’Leary, K.D., Barling, J., Arias, I., Rosenbaum, A., Malone, J., & Tyree, A. (1989). Prevalence and stability of physical aggression between spouses:  A longitudinal analysis.  _Journal of Consulting and Clinical Psychology,_ 57, 263-268.
Barling J., Fullagar, C., & Marchl-Dingel, J. (1988).  Employment commitment as a moderator of the maternal employment/child behaviour relationship.  _Journal of Organizational Behavior,_ 9, 113-122.
Barling J. MacEwen, K.E., & Pratt, L. (1988).  Manipulating the type and source of social support:  An experimental investigation. _Canadian Journal of Behavioural Science,_ 20, 140-154.
Barling, J. (1988). Industrial relations:  A blind spot in the teaching, research and practice of I/O psychology. _Canadian Psychology,_ 29, 103-108.
MacEwen, K.E., & Barling, J. (1988).  Interrole conflict, family support and marital functioning in employed mothers:  A short-term, longitudinal study.  _Journal of Organizational Behavior,_ 9, 241-250.
MacEwen, K.E., & Barling, J. (1988). Multiple stressors, violence in the family of origin and marital aggression:  A longitudinal investigation.  _Journal of Family Violence,_ 3, 73-87.
Barling, J., & MacEwen, K.E. (1988). A multitrait-multimethod matrix of four maternal employment role experiences.  _Journal of Organizational Behaviour,_ 9, 335-344.
Barling, J., & Milligan, J. (1987).  Some psychological consequences of striking:  A six month longitudinal analysis.  _Journal of Occupational Behaviour_, 8, 127-137. (Reprinted and distributed by the Industrial Relations Centre, Reprint Series No. 71, Queen’s University).
Barling, J., Bluen, S.D., & Fain, R. (1987). Psychological functioning following an acute disaster.  _Journal of Applied Psychology,_ 72, 683-690.
Jouriles, E., Barling, J., & O’Leary, K.D. (1987).  Predicting behavioral problems in maritally violent homes.  _Journal of Abnormal Child Psychology,_ 15, 165-173.
Bluen, S.D., & Barling, J. (1987). Stress in the industrial relations process:  Development of the Industrial Relations Events Scale. _South African Journal of Psychology,_ 17, 151-159.
Barling, J., O’Leary, K.D., Jouriles, E., Vivian, D., & MacEwen, K.E. (1987). Factor similarity of the Conflict Tactics Scales across samples, spouses and sites:  Issues and implications. _Journal of Family Violence,_ 2, 37-53.
Barling, J., & Rosenbaum, A. (1986).  Work stressors and wife abuse.  _Journal of Applied Psychology,_ 71, 346-348.
Barling, J. (1986). Interrole conflict and marital functioning amongst employed fathers. _Journal of Occupational Behaviour,_ 7, 1-8.
Barling J. (1986). Fathers’ work experiences, the father-child relationship and children’s behavior.  _Journal of Occupational Behavior,_ 7, 61-66.
Suchet, M., & Barling, J. (1986). Employed mothers:  Interrole conflict, spouse support and marital functioning.  _Journal of Occupational Behavior,_ 7_,_ 167-178.
Barling, J., & Bullen, G. (1985).  Dietary factors and hyperactivity:  A failure to replicate.  _Journal of Genetic Psychology,_ 146, 117-123.
Marks, M.P., & Barling, J. (1985). Does understanding of social learning principles influence children’s behavior? _Journal of Genetic Psychology,_ 146, 501-506.
Barling, J., & Van Bart, D. (1984).  Mothers’ subjective work experiences and the behaviour of their nursery school children. _Journal of Occupational Psychology_, 57, 49-56.
Barling, J., (1984). Effects of husbands’ work experiences on wives’ marital satisfaction.  _Journal of Social Psychology,_ 124, 219-225.
Barling, J., & Jannsens, P. (1984). Work stressors, gender differences and psychosomatic health problems.  _South African Journal of Psychology,_ 14, 50-53.
Barling, J., & Barenbrug, A. (1984). Some personal consequences of flexible work schedules. _Journal of Social Psychology,_ 123, 137-138.
Barling J., & Fullagar, C. (1983). Children’s attitudes to television commercials: An alternative perspective. _Journal of Psychology,_ 113, 25-30.
Fullagar, C., & Barling, J. (1983). Social learning theory:  An alternative approach to advertising effectiveness. _South African Journal of Psychology,_ 13, 18-22.
Barling, J., & Beattie, J. (1983). Self-efficacy beliefs and sales performance.  _Journal of Organizational Behavior Management_, 5, 41-51.
Barling, J., & Abel, M. (1983).  Self-efficacy beliefs and tennis performance.  _Cognitive Therapy and Research_, 7, 265-272.
Barling, J., & Snipelisky, B. (1983).  Assessing the determinants of children’s academic self-efficacy beliefs:  A replication.  _Cognitive Therapy and Research_, 7, 371-376.
Simon, M., & Barling, J. (1983). Self-efficacy beliefs and racial behaviours in male children. _South African Journal of Psychology,_ 13, 71-76.
Barling, J. (1983). Behavior therapy on South Africa_. Journal of Behavior Therapy and Experimental Psychiatry,_ 14, 369.
Bluen, S.D., & Barling, J. (1983). Work values in White South African males.  _Journal of Cross-Cultural Psychology,_ 14, 329-335.
Barling, J. (1982). Self-determined performance standards and attributional style in children’s scholastic performance.  _British Journal of Educational Psychology,_ 52, 100-103.
Steele, K.L., & Barling, J. (1982). Self-instruction and learning disabilities: Maintenance, generalization and subject characteristics.  _Journal of Psychology,_ 106, 141-154.
Barling, J. (1982). Are you a candidate for a heart attack? _Management_, November.  34, 37, 39, 41.
Barling, J., & Bresgi, I. (1982). Cognitive factors in athletic (swimming) performance:  A failure to replicate.  _Journal of Psychology_.
Barling, J. (1982). Maternal antecedents of children’s multidimensional locus of control beliefs.  _Journal of Genetic Psychology,_ 140, 155-156.
Barling, J. (1982). Developmental trends in children’s psychological conservatism:  A rejoinder to Powell and Stewart.  _Journal of Genetic Psychology,_ 140, 311-312.
Keyser, V., & Barling, J. (1981).  Determinants of children’s self-efficacy beliefs in an academic environment.  _Cognitive Therapy and Research_, 5, 29-40.
Barling, J. (1981).  Developmental trends in children’s psychological conservatism:  A failure to replicate.  _Journal of Genetic Psychology,_ 138, 143-144.
Barling, J. (1981). A cross-cultural test of Maslow’s motivation theory in industry.  _South African Journal of Psychology,_ 11, 47-51.
Barling, J., & Bolon, K. (1981). Effects of alcohol, expectancies, sex and social setting on locus of control.  _Journal of Studies on Alcohol,_ 42, 680-683.
Lentsoane, S.J., & Barling, J. (1980).  Perceived leadership behaviour and dimensions of job satisfaction in Indian and White salesmen in South Africa.  _South African Journal of Psychology,_ 10, 62.
Barling, J., & Fincham, F.D. (1980).  Alcohol, psychological conservatism and sexual interest in male social drinkers.  _Journal of Social Psychology,_ 112, 135-144.
Bolon, K., & Barling J. (1980). Multidimensional locus of control: The case of white South African students.  _Journal of Social Psychology,_ 111, 295-296.
Barling J., & Bolon, K. (1980). The measurement of self-rated depression:  A multidimensional approach.  _Journal of Genetic Psychology,_ 137, 309-310.
Barling, J. (1980). Multidimensional locus of control beliefs among South African mothers.  _Journal of Social Psychology,_ 111, 295-296. 
Barling, J. (1980). Factor structure of children’s locus of control beliefs:  A cross-cultural approach.  _Journal of Social Psychology,_ 111, 143-144.
Gluckman, S., & Barling, J. (1980). Effects of a remedial program on visual-motor perception in spinal bifida children.  _Journal of Genetic Psychology,_ 136, 195-202.
Barling J., & Patz, M. (1980). Differences following self-and external reinforcement as a function of locus of control and age: A social learning analysis.  _Personality and Individual Differences,_ 1, 79-85.
Barling, J. (1980). Performance standards and reinforcement effects on children’s academic performance:  A test of social learning theory.  _Cognitive Therapy and Research,_ 4, 409-418.
Barling, J. (1980). A multi-stage, multi-dependent variable assessment of normal children’s self-regulation of academic performance.  _Child Behavior Therapy,_ 2, (2), 43-54.
Barling, J. (1979). Verbal proficiency:  A confounding variable in the reliability of children’s attitude scales?  _Child Development,_ 50, 1254-1256.
Barling, J., & Wainstein, T. (1979). Attitudes, labelling bias and behavior modification in work organizations.  _Behavior Therapy,_ 10, 129-136.
Barling, J., & Fincham, F.D. (1979). Effects of self-and externally imposed reinforcement (material and social) on intelligence test performance of above-average IQ children.  _Journal of Genetic Psychology,_ 135, 63-70.
Barling, J., & Fincham, F.D. (1979). Maslow’s need hierarchy and dimensions of perceived locus of control. _Journal of Genetic Psychology,_ 134, 313-314.
Barling, J., & Fincham, F.D. (1979). Cultural and sexual effects on children’s psychological conservatism.  _Journal of Social Psychology,_ 107, 15-21.
Fincham, F.D., & Barling, J. (1979). The effects of alcohol on moral functioning in male social drinkers.  _Journal of Genetic Psychology,_ 134, 79-88.
Barling, J., & Fincham, F.D. (1979). The effects of alcohol on psychological conservatism.  _Journal of Social Psychology,_ 107, 129-130.
Press, L., Burt, I., & Barling, J. (1979).  Racial Preferences among South African Black and White preschool children.  _Journal of Social Psychology,_ 107, 125-126.
Barling, J. (1979). Children’s psychological conservatism and social desirability. _South African Journal of Psychology,_ 9, 153.
Barling, J. (1979). Toward a definition of behavior modification.  _Psychotherapeia_, 5, 2-6.
Bolon, K., & Barling, J. (1979). Alcohol, expectancies and social setting effects on depression.  _South African Journal of Psychology,_ 10, 46-49.
Fincham, F.D., & Barling, J. (1978). Locus of control and generosity in learning disabled, normal achieving and gifted children. _Child Development,_ 49, 530-533.
Barling J., & Fincham, F.D. (1978).  Locus of control beliefs in male and female Indian and White schoolchildren in South Africa.  _Journal of Cross-Cultural Psychology,_ 9, 227-235.
Barling, J. Fincham, F.D. (1978). Performance standards in learning disabled, normal achieving and gifted children.  _Journal of Behavioural Science,_ 2, 307-308.
Bolon, K., & Barling, J. (1978).  Alcohol consumption, expectancy and multi-dimensional locus of control in male and female social drinkers.  _Journal of Behavioural Science,_ 2, 331-337.
Wulfsohn, D., & Barling, J. (1978). From external to self-control:  Behavioral treatment of trichotillomania in an eleven year old child. _Psychological Reports,_ 42, 1171-1174.
Barling J., & Lanham, W. (1978). Consequences of birth control beliefs amongst Black, Coloured, Indian and White South Africans_.  Journal of Social Psychology,_ 105, 149-150.
Barling, J., (1978). The image of behaviour modification: A critical analysis. _South African Journal of Psychology,_ 9, 98-103.
Barling, J. (1977). Increasing isolation and specialization of applied behavior analysis within behavior modification.  _Psychological Reports,_ 40, 1047-1050.
Barling, J. (1977). An empirical test of Maslow’s theory of work motivation in an industrial setting.  _Psychologia Africana,_ 17, 99-110.
Barling, J. (1977). A critical review of the application of Maslow’s motivation theory in industry.  _Perspectives in Industrial Psychology_, 3, 3-36.
Barling J., & Neall, R.J. (1977). Organizational acceleration: An irrelevant variable? _South African Journal of Psychology,_ 7, 54-61.
Saad, L.J., & Barling, J. (1977). Relating pay incentives to work performance:  Effects of fixed ratio (group and individual contingent) versus fixed interval reinforcement in industry.  _Psychologia Africana,_ 17, 135-142.
Barling J., & Hannon, A.E. (1977). Self-control:  The target of behaviour modification.  _Psychotherapeia,_ 3, 1923.
Barling, J. (1976). Organizational behavior modification (A book review).  _Psychologia Africana,_ 16, 215-216.
Barling, J. (1976). Behavioural treatment of enuresis and encopresis in a young boy.  _South African Journal of Medicine_, 50, 1274.
Barling, J. (1976). An empirical test of the “career stages” alternative to Maslow’s need hierarchy in an industrial setting. _South African Journal of Psychology_, 6, 52-56.
Barling, J., & Zimbler, A. (1976). A descriptive analysis of the activities of the Johannesburg Crisis Clinic and some implications for community mental health.  _Psychotherapeia,_ 2, 17-24.
#### Book Chapters
Grocutt, A., & Barling, J. (in press). _Miscarriage and work_. In C.L. Cooper and A. Kinder (Eds.) _Occupational Health and Wellbeing_. London: Routledge.
Pupco, S., & Barling, J. (2021). _Leadership and well-being_. In C.L. Cooper and E.K. Kelloway (Eds.) _A Research Agenda for Stress and Well-being_. London: Edward Elgar Publishing.
Cloutier, A., & Barling J. (2020) _Leadership in flexible work systems_. In S. Norgate & C.L. Cooper (Eds.) _Flexible Work: Designing Our Healthier Future Lives_  London: Routledge.
Trivisonno, M. & Barling, J. (2019). A Passion for Leadership. In R. Vallerand & N. Houlfort (Eds.), _Passion for Work: Determinants and Consequences_ (pp. 411-437). NY: Oxford University Press.
Carleton, E. L., & Barling, J. (2017). Leadership and mental illness: Realities and new directions. In E. K. Kelloway, K. Nielsen & J.K. Dimoff (Eds.) _Leading to occupational health and safety_ (pp. 307-322) London: Wiley-Blackwell. 
Carleton, E., & Barling, J. (2017). Sleep, work and well-being. In C. L. Cooper and J.C. Quick (Eds.) _The Wiley handbook of stress and health: A guide to research and practice_ (pp. 485-500). London: Wiley-Blackwell.
Barling, J., & Turner, N. (2016). Workplace safety. In S.G. Rogelberg, K.M. Shockley, & S. Tonidaniel (Eds.) _Encyclopedia of industrial and organizational psychology (2nd ed.)_ (pp. 1783-1785). Thousand Oaks, CA: Sage.
Barling, J., & Turner, N. (2016). Workplace injuries. In S.G. Rogelberg, K.M. Shockley, & S. Tonidaniel (Eds.) _Encyclopedia of industrial and organizational psychology_ _(2nd ed.)_ (1778-1779). Thousand Oaks, CA: Sage.
Trivisonno, M., & Barling, J. (2016). Organizational leadership and employee commitment. In J.P. Meyer (Ed.) _Handbook of Employee Commitment_ (pp. 305-318). UK: Edward Elgar Publishing.
Barling, J., Barnes, C.M., Carleton, E.L., & Wagner, D.T. (2016). Work and sleep: Looking back, and moving forward. In J. Barling, C.M. Barnes, E.L. Carleton & D.T. Wagner (Eds.) _Work and Sleep: Research Insights for the Workplace_. NY: Oxford University Press (pp. 3-10).
Carleton, E.L., & Barling, J. (2016). Sleep and work withdrawal. In J. Barling, C.M. Barnes, E.L. Carleton & D.T. Wagner (Eds.) _Work and Sleep: Research Insights for the Workplace_. NY: Oxford University Press (pp. 193-212).
Byrne, A. & Barling, J. (2015). Leadership and Project Management Teams. In F. Chiocchio, E.K. Kelloway, & B. Hobbs (Eds.), _The Psychology of Project Teams: An Interdisciplinary Perspective_ (pp. 137-163)_._ NY: Oxford University Press.
Robertson, J.L., & Barling, J. (2015). The role of leadership in promoting workplace pro-environmental behaviors. In J.L. Robertson & J. Barling (Eds.). _The Psychology of Green Organizations_. NY: Oxford University Press.
Barling, J., Kelloway, E.K., & Weber, T.  (1996). Effects of transformational leadership training on attitudinal and financial outcomes:  A field experiment.  _Journal of Applied Psychology,_ 81, 827-832. Reprinted in R. Hall, D. Grant & J. Raelin (Eds.) (2014) _Leadership Development and Practice_ (Vol. 1). CA: Sage Publications.
Hoption, C., Phelan, J., & Barling, J. (2014). Transformational leadership in sport.  In M.R. Beauchamp & M.A. Eys (Eds.) _Group dynamics in exercise and sport psychology: Contemporary themes_ (2nd ed., pp. 55-72). NY: Routledge.
Robertson, J., & Barling, J. (2014). Lead well, be well: Leadership behaviors influence employee well-being. In P. Chen & C.L. Cooper (Eds.) _Well-being: A complete reference guide, Volume 3, Work and Well-being_ (pp. 235-251). London: Wiley-Blackwell.
Robertson, J., & Barling, J. (2014). Corporate Social Responsibility and Psychologically Healthy Workplaces. In A. Day, E.K. Kelloway, & J.R. Hurrell (Eds.) (2014). _Workplace Well-being: How to Build Psychologically Healthy Workplaces_ (p. 264-280). London: Wiley.
Barling, J., & Carson, J. (2013). The impact of management style on mental well-being at work. In C.L. Cooper and I.T. Robertson (Eds.) _Management and happiness_. UK: Edward Elgar.
Arnold, K.A., Turner, N., Barling, J., Kelloway, E.K., & McKee, M. (2013).  Transformational leadership and psychological well-being: The mediating role of meaningful work.  _Journal of Occupational Health Psychology, 2007,_ 12, 193-203. Reprinted in C.L. Cooper and I.T. Robertson (Eds.) _Management and happiness_. UK: Edward Elgar.
Dionisi, A., & Barling, J. (2011). Sexual harassment: A big problem in small and medium enterprises? In E.K. Kelloway & C.L. Cooper (Ed.) _Occupational health and safety in small and medium enterprise_ (pp. 129-158).  London, UK: Elgar.
Christie, A., & Barling, J. (2011). A short history of occupational health psychology: A biographical approach. In A.S. Antoniou & C. Cooper (Eds.) _New directions in organizational psychology and behavioral medicine (_pp. 7-24). Surrey, UK: Gower Publishing.
Barling, J., & Griffiths, A. (2011). The history of occupational health psychology.  In J. C. Quick & L.E. Tetrick (Eds.) _Handbook of occupational health psychology 2nd ed_ (pp.  21-34) American Psychological Association:  Washington, DC.
Barling, J., Christie, A., & Hoption, A. (2010). Leadership. In S. Zedeck et al (Ed.) _Handbook of Industrial and Organizational Psychology_ (pp. 183-240). Washington, DC: American Psychological Association.
Kelloway, E.K., Inness, M., Barling, J., Francis, L., & Turner, N. (2010). Loving one’s job: construct development and implications for well-being. In P.L. Perrewe & D.C. Ganster  (Eds.) _Research in Occupational Stress and Well Being (Vol. 8)_: UK: Emerald Publishing.
Barling, J., Dupré, K., & Kelloway, E.K. (2009). Predicting Workplace Aggression: Myths, Realities, and Remaining Questions. _Annual Review of Psychology, 60_, 671-692.
Carson, J., & Barling, J. (2008). Work and well-being.  In J. Barling and C.L. Cooper (Eds), _The Sage Handbook of Organizational Behavior Volume 1: Micro approaches (pp. 675-692)_. London, UK: Sage Publications.
Carson, J., & Barling, J. (2008).  Romantic relationships at work: Old issues, new challenges.  In K. Naswall, J. Hellgren & M. Sverke (Eds.)  _The individual in the changing working life._  (pp. 195-210) UK: Cambridge University Press.
Raver, J., & Barling, J. (2008).  Workplace aggression and conflict: Constructs, commonalities, and challenges for future inquiry.  In C.K.W. De Dreu and M.J. Gelfand (Eds.) _The psychology of conflict and conflict management in organizations (211- 244)_. NJ: Lawrence Erlbaum Associates.
Hershcovis, M.S., & Barling, J. (2007). A relational perspective on workplace aggression: An examination of perpetrators and targets. In J. Langan-Fox, C. Cooper, & R. Klimoski (Eds.), _Research companion to the Dysfunctional Workplace: Management Challenges and Symptoms_ (PP. 268-284). Cheltenham, UK: Edward Elgar Publishing Ltd.
Hoption, C., Phelan, J., & Barling, J. (2007). Transformational leadership in sport.  In M.R. Beauchamp & M.A. Eys (Eds.) _Group dynamics in exercise and sport psychology: Contemporary themes_ (pp. 45-60). NY: Routledge.
Barling, J., & Turner, N. (2007). Workplace safety. In S. Rogelberg (Ed.) _Encyclopedia of industrial and organizational psychology (Vol. 2)_ (pp. 902-905). Thousand Oaks, CA: Sage.
Turner, N., & Barling, J. (2007). Workplace injuries. In S. Rogelberg (Ed.) _Encyclopedia of industrial and organizational psychology (Vol. 2)_ (pp. 897-900). Thousand Oaks, CA: Sage
Christie, A.M. & Barling J. (2006). Careers and Health. In J.H. Greenhaus, & G.A. Callanan (Eds.), _Encyclopedia of Career Development_. CA: Sage Publications.
Hershcovis, M.S., & Barling, J. (2006).  Preventing workplace violence.  In E.K. Kelloway, J. Barling & J.J. Hurrell Jr III (Eds.) _Handbook of workplace violence_ (pp. 607-632). CA: Sage.
Leblanc, M., Dupré, K., & Barling, J. (2006). Public-initiated violence.  In E.K. Kelloway, J. Barling & J.J. Hurrell Jr III (Eds.) _Handbook of workplace violence (_pp. 261-280). CA: Sage.
Inness, M.M., Barling, (2005).  Terrorism.  _Handbook of Work Stress_. 375-398. CA: Sage Publications.
Dupré, K., Barling, J., & LeBlanc, M.L. (2005).  The many faces of control at work.  In C.L. Cooper (Ed.) _Handbook of Stress Medicine and Health_ (pp. 375-398). London: Wiley.
Kelloway, E.K., Sivanathan, N., Francis, L., & Barling, J. (2005).  Poor leadership.  In J. Barling, E.K. Kelloway, & M. Frone (2005) (Eds.) _Handbook of Work Stress_ (pp. 89-112) CA: Sage Publications.
LeBlanc, M., & Barling, J. (2005).  Understanding the many faces of workplace violence.  In. P. Spector and S. Fox (Eds_.).  Counterproductive behavior at work:  Investigations of actors and targets_ (pp. 41-64)  Washington, DC:  American Psychological Association.
Sivanathan, N., Arnold, K.A., Turner, N., & Barling, J. (2004).  Leading well: Transformational leadership and well-being.  In P.A. Linley and S. Joseph (Eds.) _Positive psychology in practice_ (pp. 241-255).  NY. Wiley. (Reprinted in Polish in: J. Czapinski (Ed.) (2007). _Psychologia_ _pozytywna w praktyce_. Warsaw, Poland: Polish Scientific Publishers PWN)
Kelloway, E.K., Gallagher, D.G., & Barling, J. (2004).  Work, employment and the individual.  In B.E. Kaufman (Ed.) _Theoretical perspectives on work and the employment relationship_ (pp. 105-131) Champaign, IL:  Industrial Relations Research Association.
Zacharatos, A., & Barling, J. (2004).  Human resource management and occupational safety.  In J. Barling and M. Frone (Eds).  _The psychology of workplace safety_ (pp. 203-222) American Psychological Association:  Washington, DC.
Arnold, K.A. & Barling J. (2003). Prostitution: An illustration of occupational stress in 'dirty' work. In M. Dollard, A. Winefield & H. Winefield (Eds), _Occupational Stress in the Service Professions_. Taylor and Francis.
Dupré, K., & Barling, J. (2003) Workplace aggression.  In A. Sagie., S. Stashevsky & M. Koslowsky (Eds.) _Misbehaviour and dysfunctional attitudes in organizations_. (pp. 13-32)  NY:  Palgrave MacMillan.
Barling, J., Inness, M., & Gallagher, D.G. (2002).  Alternative work arrangements and employee-well-being.  In P. Perrewe and D.C. Ganster (Eds.) _Research in Occupational Stress and Well-being_ (pp. 183-216).  NY:  JAI Press.
Barling, J., & Griffiths, A. (2002).  The history of occupational health psychology.  In L.E. Tetrick & J.C. Quick (Eds.) _Handbook of occupational health psychology_ (pp.  19-33). American Psychological Association:  Washington, DC.
Kelloway, E.K., Barling, J., & Weber, C. (2002).  Smoking and absence at work:  A quantitative review.  In M. Koslowsky and M. Krausz (eds.) _Voluntary employee withdrawal and inattendance:  A current perspective_ (pp. 167-178).  NY:  Plenum Publishing.
Barling, J., Kelloway, E.K., & Zacharatos, A. (2002).  Occupational safety.  In P.B. Warr (Ed).  _Psychology in the workplace_. (pp. 253-275)  London:  Penguin Books.
Turner, N., Barling, J., & Zacharatos, A. (2002).  Positive psychology at work.  In C.R Snyder & S. Lopez. (Eds.)  _The handbook of positive psychology_ (pp. 715-730)  Oxford: Oxford University Press.
Barling, J. (2000). Unions.  In A.E. Kazdin (Ed.) _Encyclopedia of Psychology_ (pp. 138-140).  Washington, DC:  American Psychological Association.
Loughlin, C.A., & Barling, J. (2000).  Coping with acute disasters at work.  In P. Dewe, T. Cox & M. Leiter (Eds.) _Coping and health in organizations_ (pp. 71-86).  London:  Taylor & Francis.
Barling, J. (1999).  Changing employment relations:  Empirical data, social perspectives and policy options.  In D.B. Knight & A. Joseph (Eds.) _Restructuring societies:  Insights from the social sciences_ (pp. 59-82).  Ottawa, Ontario:  Carlton University Press.
Barling, J. (1998).  Workplace violence.  In J.M. Stellman (Ed.).  _ILO Encyclopaedia of Occupational Health and Safety_ (4th ed.) (pp. 34:39-34:30)  Geneva:  International Labor Organization.
Hartley, J., & Barling, J. (1998).  The use of employee attitude surveys in organizational research.  In K. Whitfield & G. Strauss (Eds.) _Researching the world of work:  Strategies and methods in studying industrial relations_ (pp. 1157-170) Ithaca, NY: Cornell University Press.
Barling, J. & Sorenson, D. (1997).  Work and family:  In search of a relevant research agenda.  In S. Jackson & C.L. Cooper (Eds.). _Creating tomorrow’s organizations: A Handbook for future research in organizational behaviour_ (pp. 159-170).  NY: Wiley.
Hepburn, C.G., Loughlin, C., & Barling, J. (1997).  Abstaining from voting in union certification elections.  In M. Sverke _The future of trade unionism: International perspectives on emerging union structures_ (pp. 249-262).  London: Ashgate Publishing.
Kelloway, E.K., Barling, J., & Catano, V. (1997).  Union attitudes as a perceptual filter.  In M. Sverke _The future of trade unionism: International perspectives on emerging union structures_ (pp. 225-234).  London: Ashgate Publishing.
Hepburn, C.G., Loughlin, C., & Barling, J. (1997).  Coping with chronic work stress.  In B. Gottlieb (Ed.)  _Coping and health in organizations_.  London:  Taylor & Francis.
Barling, J. & Gallagher, D.G. (1996).  Part-time employment.  In C.L. Cooper and I.T. Robertson (Eds.) _International Review of Industrial and Organizational Psychology_ (pp. 243-277) (Vol. II).  London: Wiley and Sons.
Barling, J. (1996).  The prediction, psychological experience and consequences of workplace violence.  In G. VandenBos & E.G. Bulatao (Ed.) _Violence on the job:  Identifying risks and developing solutions_ (pp. 29-49) Washington, DC: American Psychological Association.
Greenberg, L., & Barling, J. (1996).  Employee theft.  In C.L. Cooper and D.L. Rousseau (Eds.) _Trends in organizational Behaviour_ (pp. 49-64) (Vol.3.).  London: Wiley and Sons.
Adams-Roy, J.E., Knap, M.A., & Barling, J.  (1995). The role of occupational health and safety education university level management programs.  In L.E. Tetrick and J. Barling (Eds.) _Behavioural and social perspectives on changing employment relations_ (pp. 133-144).  Washington, D.C.:  American Psychological Association.
Loughlin, C.A., Hepburn, C.G., & Barling, J. (1995).  Changing future managers’ attitudes towards occupational health and safety.  In L.E. Tetrick and J. Barling (Eds.) _Behavioural and social perspectives on changing employment relations_ (pp. 145-162).  Washington, DC: American Psychological Association.
Gordon, M.E., Barling, J. & Tetrick, L.E. (1995).  Some remaining challenges in a time of changing employment relations. In L.E. Tetrick and J. Barling (Eds.) _Behavioural and social perspectives on changing employment relations_ (pp. 349-366).  Washington, DC: American Psychological Association.
Barling, J. (1994). Work and Family:  In search of more effective intervention strategies.  In C.L. Cooper & D. Rousseau (Eds.) _Trends in Organizational Behaviour, Vol. 1_ (pp. 63-73). London: Wiley.
Kelloway, E.K., & Barling, J. (1994). Stress control, well-being and marital satisfaction:  A  causal correlational analysis.  In G.P. Keita & J.R. Hurrell (Eds.) _Job stress in a changing workforce:  Investigating gender, diversity and family_  (pp. 241-251).  Washington, D.C.:  American Psychological Association.
Grant, S., & Barling, J.  (1994). Linking unemployment experiences and marital functioning.  In G.P. Keita & J.R. Hurrell (Eds.). _Job stress in a changing workforce:  Investigating gender, diversity and family_ (pp. 311-327).  Washington, DC:  American Psychological Association.
Barling, J. (1991). Fathers’ employment, unemployment and their children’s behaviour.  In J.V. Lerner & N. Galambos (Eds.) _The employment of mothers during the child rearing years_ (181-209). N.Y.:  Garland
Barling, J. (1990).  Employment stressors and marital functioning.  In F.D. Fincham and T. Bradbury (Eds.). _The Psychology of Marriage_ (201-225). N.Y:  Praeger.
Bluen, S.D., & Barling, J. (1988).  Psychological stressors associated with the industrial relations process.  In C.L. Cooper & R. Payne (Eds.) _Causes, coping and consequences of stress at work_ (2nd ed.) pp. 175-205 London: Wiley.
Pratt, L., & Barling, J. (1988).  Differentiating daily hassles, acute and chronic stressors:  A framework and its implications.  In J.R. Hurrell, L.R. Murphy, S.L. Sauter & C.L. Cooper (Eds.), _Occupational Stress:  Issues and Developments in Research_.  (41-53) London:  Taylor & Francis.
Fullagar, C., & Barling, J. (1987).  Toward a model of union commitment.  In D. Lewin, D.B. Lipsky & D. Sockell (Eds.) _Advances in Industrial and Labor Relations_ pp. 43-78. Greenwich, CT:  JAI Press.
Barling, J. (1986).  Some psychosocial consequences of paid employment.  In J. Barling, C.  Fullagar & S.D. Bluen (Eds.), _Behaviour in organizations:  South African perspectives_ pp.  147-175 (2nd ed.).  Johannesburg:  McGraw Hill.
Barling, J. (1986). Work motivation. In J. Barling, C. Fullagar & S.D. Bluen (Eds.)  _Behaviour in organizations: South African perspectives_ pp. 495-531 (2nd ed.).  Johannesburg:  McGraw Hill.
Barling, J. (1983).  Work motivation.  In J. Barling (Ed.), _Behaviour in organizations:  South African perspectives._  pp. 341-370.  Johannesburg: McGraw-Hill.
#### In the Media
Good leaders mentor, not monitor. _Globe and Mail_, October 6, 2011.  
[http://www.theglobeandmail.com/report-on-business/careers/careers-leadership/barling-good-leaders-mentor-not-monitor/article556906/?page=all](http://www.theglobeandmail.com/report-on-business/careers/careers-leadership/barling-good-leaders-mentor-not-monitor/article556906/?page=all)
True leaders, like Mandela, change minds. Ottawa Citizen, January 9, 2014.  
[http://ottawacitizen.com/opinion/columnists/true-leaders-like-mandela-change-minds](http://ottawacitizen.com/opinion/columnists/true-leaders-like-mandela-change-minds)
[](http://ottawacitizen.com/opinion/columnists/true-leaders-like-mandela-change-minds)Nature or nurture: How is a leader produced? _Globe and Mail_, March 28, 2014.  
[http://www.theglobeandmail.com/report-on-business/careers/business-education/nature-or-nurture-how-is-a-leader-produced/article17721385/](http://www.theglobeandmail.com/report-on-business/careers/business-education/nature-or-nurture-how-is-a-leader-produced/article17721385/)
What Manchester United’s meltdown can teach us about succession. _Globe and Mail_, April 23, 2014.  
[http://www.theglobeandmail.com/report-on-business/careers/leadership-lab/what-manchester-uniteds-meltdown-can-teach-us-about-succession/article18130887/](http://www.theglobeandmail.com/report-on-business/careers/leadership-lab/what-manchester-uniteds-meltdown-can-teach-us-about-succession/article18130887/)
Sleep well, you’ll lead well. _Globe and Mail_, August 11, 2014.  
[http://www.theglobeandmail.com/report-on-business/careers/leadership-lab/sleep-well-youll-lead-well/article19971919/](http://www.theglobeandmail.com/report-on-business/careers/leadership-lab/sleep-well-youll-lead-well/article19971919/)
Ask the expert: Something’s missing from our understanding of leadership— followership!  **ON**Board, Summer 2014, p.14  
[http://onboard.trbot.ca/archive/OnBoardSummer2014.pdf](http://onboard.trbot.ca/archive/OnBoardSummer2014.pdf)
Genders and leadership. TheCannon.ca. 
Memo to Brian Williams: A true apology is both art and science. _Globe and Mail_, February 19, 2015.  
[http://www.theglobeandmail.com/report-on-business/careers/leadership-lab/memo-to-brian-williams-a-true-apology-is-both-art-and-science/article22900808/](http://www.theglobeandmail.com/report-on-business/careers/leadership-lab/memo-to-brian-williams-a-true-apology-is-both-art-and-science/article22900808/)
Science says: Girls are as predisposed to be leaders as boys. _Minerva_, March 18, 2015.
How leaders should apologize without making things worse. _Forbes_, April 3, 2015.  
[http://www.forbes.com/sites/shelliekarabell/2015/04/03/how-leaders-should-apologize-without-making-things-worse/?&article\_id=20924708992](http://www.forbes.com/sites/shelliekarabell/2015/04/03/how-leaders-should-apologize-without-making-things-worse/?&article_id=20924708992)
Why we have to pay more attention to managers’ mental health. _Canadian Business_, April 20, 2015. 
Too little attention paid to managers’ mental health. _HRM Online_, August 27, 2015.  
[http://www.hrmonline.ca/hr-news/too-little-attention-paid-to-managers-mental-health-190639.aspx](http://www.hrmonline.ca/hr-news/too-little-attention-paid-to-managers-mental-health-190639.aspx)
A bad economy means more reasons to watch our mental health at work. _Globe and Mail_, September 16, 2015. (op-ed)  
[http://www.theglobeandmail.com/report-on-business/rob-commentary/a-bad-economy-means-more-reasons-to-watch-our-mental-health-at-work/article26373227/](http://www.theglobeandmail.com/report-on-business/rob-commentary/a-bad-economy-means-more-reasons-to-watch-our-mental-health-at-work/article26373227/)
Open letter to Prime Minister Stephen Harper on the Eve of the 2015 Federal Election. October 15, 2015.  
[https://www.linkedin.com/pulse/open-letter-prime-minister-stephen-harper-eve-2015-federal-barling](https://www.linkedin.com/pulse/open-letter-prime-minister-stephen-harper-eve-2015-federal-barling)
Investment in leadership training pays dividends. _The Star_, October 23, 2015. 
[How Passive Leaders Undermine Employee Well-Being.](https://smith.queensu.ca/insight/content/research-brief-the-adhd-to-zzzs-of-passive-leadership.php) _Smith Insight,_ October 11, 2016
Passive Leadership and the Damage: Done How the passive boss can be just a toxic as an abusive boss. _IEDP Developing Leaders_, November 10, 2016  
[http://iedp.com/articles/passive-leadership-and-the-damage-done/#sthash.wFb9hW2T.dpuf](http://iedp.com/articles/passive-leadership-and-the-damage-done/#sthash.wFb9hW2T.dpuf)
[Nasty coaches and the damage done](https://smith.queensu.ca/insight/content/research-brief-nasty-coaches-and-the-damage-done.php). _Smith Insight_, January 12, 2017.
Does a Woman’s High-Status Career Hurt Her Marriage? Not If Her Husband Does the Laundry. _Harvard Business Review_ May 2, 2017.  
[https://hbr.org/2017/05/does-a-womans-high-status-career-hurt-her-marriage-not-if-her-husband-does-the-laundry](https://hbr.org/2017/05/does-a-womans-high-status-career-hurt-her-marriage-not-if-her-husband-does-the-laundry)
High-status women are happier when their husbands pitch in at home: study. Arti Patel, May 3, 2017. 
Lost leaders: How poverty erodes professional development. _Globe and Mail_, May 25, 2017.  
[https://www.theglobeandmail.com/report-on-business/rob-commentary/lost-leaders-how-poverty-erodes-professional-development/article35102368/](https://www.theglobeandmail.com/report-on-business/rob-commentary/lost-leaders-how-poverty-erodes-professional-development/article35102368/)
Female breadwinners pay a cost for career success – marital stress  
[https://beta.theglobeandmail.com/report-on-business/careers/business-education/female-breadwinners-pay-a-cost-for-career-success-marital-stress/article35306676/?ref=https://www.theglobeandmail.com&service=mobile](https://beta.theglobeandmail.com/report-on-business/careers/business-education/female-breadwinners-pay-a-cost-for-career-success-marital-stress/article35306676/?ref=https://www.theglobeandmail.com&service=mobile)
[Taking the pulse of surgical teams](https://smith.queensu.ca/insight/content/taking-the-pulse-of-surgical-teams.php). _Smith Insight,_ November 1, 2017.
For surgeons, their leadership style can be as important as their scalpel skills. _Globe and Mail_, January 17, 2018.  
[https://www.theglobeandmail.com/report-on-business/careers/business-education/why-a-surgeons-leadership-style-can-be-as-important-as-his-scalpel-skills/article37643494/](https://www.theglobeandmail.com/report-on-business/careers/business-education/why-a-surgeons-leadership-style-can-be-as-important-as-his-scalpel-skills/article37643494/)
[Troubled at Home, Leaders Lash Out or Withdraw](https://smith.queensu.ca/insight/content/troubled-at-home-leaders-lash-out-or-withdraw.php). _Smith Insight_, June 26, 2019.
[Forget Heroes. We Need Our Leaders to Act Small](https://smith.queensu.ca/insight/content/forget-heroes-we-need-our-leaders-to-act-small.php). _Smith Insight_, May 26, 2020.
[Why Lockouts Are Tough on Mental Health](https://smith.queensu.ca/insight/content/why-lockouts-are-tough-on-mental-health.php). _Smith Insight_, October 21, 2020
[Leadership lessons from the Great Pandemic](https://smith.queensu.ca/magazine/issues/fall-2020/features/great-pandemic.php). _Smith Magazine_, Fall, 2020.
[Managers Don’t Treat All Disabled Workers Alike](https://smith.queensu.ca/insight/content/managers-dont-treat-all-disabled-workers-alike.php). _Smith Insight_, January 4, 2021
### Teaching
#### Graduate Supervision (1985 onwards)
**PhD**
* Trivisonno, M. (2020). _A passion for leadership: Three studies_.
* Cloutier, A. (2020). _Romantic Relationships and Leadership: Three Studies._
* Suurd Ralph, C. (2019). _Leader Inconsistency, Subjective Attitude Ambivalence and Follower Outcomes._
* Weatherhead, J.G. (2019). _Revisiting the Nature of Transformational Leadership: How Followers’ Affect Matters._
* Carleton, E.L. (2016). _Sleep well, work well: Three Studies_.
* Akers, A.L. (2015). _The influence of leadership and extreme contexts on physical and psychological outcomes_.
* Dionisi, A. (2014). _Vicarious exposure to male sexual harassment: Correlates, perceived motives and ethical evaluations, and behavioral responses_
* Robertson, J. (2014). _Greening organizations: The roles of leadership and organizational citizenship behaviors_.
* Byrne, A. (2013). _Three studies of counterintuitive effects of organizational status._
* Hoption, C.B. (2009). _Toward a relational and dynamic perspective of leadership_.
* LeBlanc, M.M. (2009). _The effects of partner aggression on women’s work_.
* Christie, A.M. (2008). _Status, relatively speaking: Extending the organizational focus on status and status inequality_.
* Hershcovis, M.S. (2006). _The prediction and consequences of workplace aggression: A meta-analytic approach_.
* Inness, M. (2006). _The person and the situation: Predicting well-being outcomes at work_.
* Mendelson, M.B. (2005). _The nature of high involvement work systems: A test of competing models_.
* Dupré, K.E. (2004). _Beating up the boss: The prediction and prevention of interpersonal aggression targeting workplace supervisors_.
* Arnold, K.A. (2003). _Dirty work and well-being_.
* Zacharatos, A. (2001). _An organization and employee level investigation of the relationship between high performance work systems and workplace safety_.
* Wright, B. (1999). _An empirical examination of the outcome effects of downsizing on decision makers_.
* Loughlin, C.A. (1998). _Toward a model of healthy work for full-time, part-time and contract employment_.
* Hepburn, C.G. (1997). _Voting and abstaining from voting in union representation elections_.
* Stewart, W.E. (1992). _Fathers’ work experiences and their children’s social behaviors and school competencies_.
* Grant, S.A. (1991). _Linking unemployment and marital functioning: A meditational model_.
* Higginbottom, S.F. (1991). _Linking the quality of the retirement experience to marital satisfaction: A meditational model_.
* Kelloway, E.K. (1991). _Members’ participation in local union activities: Measurement, prediction and replication_.
* MacEwen, K.E. (1991). _A social learning approach to refining the link between family of origin aggression and current relationship aggression_.
* Kryl, I.P. (1990). _Causal modeling of predictors and outcomes of trade union participation_.
* Bluen, S.D. (1986). _Consequences and moderators of industrial relations stressors_.
* Fullagar, C.J.A. (1986). _Causes, correlates, and outcomes of union commitment._
**Masters**
* Pupco, S. (2019). _The Effects of Parental Leave on Parents’ Leadership Emergence_.
* Weatherhead, J. (2014). _What does it take to become a leader? Externalizing and internalizing childhood behavior problems and early leadership emergence._
* Tulloch, K. (2013). _On the court: Investigating destructive leadership outcomes in the NBA._
* Guberinic, M. (2010). _Transformational leadership: Four parts or one?_
* Lys, M. (2009). _Leaders’ mental health moderates the relationship between transformational leadership and employee counterproductive behaviors_.
* Robertson, J. (2009). _Do as I say and as I do: Environmentally-specific transformational leadership, modeling and employees’ pro-environmental behaviors_.
* Byrne, A. (2008). Who’s laughing now? The impacts of leadership and humor style on relationship outcomes.
* Byrne, S. (2008). _Contrasting the effects of supervisory over-control and autonomy_.
* Carson, J. (2007). _Jump and java to higher performance: The effect of nutrition and exercise on work_.
* Dezan, H. (2006). _Leader apologies and employee health: The nature and effects of leader apologies on employee health_.
* Reid, E. (2003). _Building perceptions of transformational leadership: the role of apologies and gender_.
* Desaulniers, M.S. (2002). _Single mothers, work-family conflict and children’s behavior._
* Sivanathan, N. (2002). _Effects of transformational leadership training on occupational safety_.
* Williams, A. (2002). _Commitment and control: New perspectives on high performance work systems_.
* Rowbotham, K. (2001). _Exploring the relationship between alternative work arrangements and industrial relations climate._
* Comtois, J. (2000). _The influence of transformational leadership on electronic communication_.
* Lawson, K. (1999). _The effects of back-to-work legislation on industrial relations climate, attitudinal factors and stressors within the teaching community_.
* Turner, N. (1998). _An exploratory study of moral reasoning and transformational leadership_.
* Zacharatos, A. (1998). _Development and effects of transformational leadership in adolescents_.
* Adams-Roy, J.E. (1994). _Will she or won’t she? Factors influencing the likelihood that women will confront or report sexual harassment_.
* Dekker, I. (1994). _Personal and organizational predictors of self-reported sexual harassment in the workplace._
* Greenberg, L. (1993). _Predicting employee aggression: The roles of personal behaviors and workplace factors_.
* Loughlin, C.A. (1993). _Part-time employment and adolescents’ well-related attitudes, beliefs and aspirations._
* Hepburn, C.G. (1993). _Eldercare, employee absence, and interrole conflict: A daily study_.
* Sandys-Wunsch, H. (1991). _Context-specific and context-free mental health as mediators in the student role experience-performance relationship_.
* Boswell, R. (1990). _Noneffective attention as a mediator in the relationships between achievement strivings and performance and impatience-irritability_.
* Stewart, W. (1990). _The effect of daily work stressors on the interpersonal effectiveness of health care professionals working in outpatient cancer clinics_.
* MacIntyre, A.T. (1989). _Some effects of daily work role stress on same day and next day emotional exhaustion_.
* Marks, M.P. (1986). _Fathers’ job stress and children’s behaviour_.
* Pratt, L.I. (1986). _An investigation of the effects of supervisor support on the role stressor/burnout relationship: A moderated meditational model_.
* MacEwen, K.E. (1985). _Some effects of interrole conflict, social support and personality hardiness on the marital adjustment of employed mothers_.
* Beattie, R. (1981). _Self-efficacy beliefs as determinants of motivation and performance: An industrial environment._
**Leadership Development Workshops for Queen's Executive Education**
* Alberta WCB
* Armour Transportation Systems
* Bell
* Birchcliffe Energy
* BluEra
* BMW
* Canada Post
* CIBC
* Collahausi (Chile)
* Correctional Services Canada 
 Deloitte (Australia)
* Enbridge
* Encana
* Federal Departments (Canadian Forces, Fisheries and Oceans, Revenue Canada)
* FEI Canada
* Goodman Carr LLP
* Infrastructure Ontario
* Jacques Whitford Environment Ltd
* LifeMark Health
* Miller Thompson LLP
* Niagara Casinos
* PowerStream
* Provincial Governments (Manitoba, New Brunswick, Nova Scotia, Ontario)
* Public Safety Canada
* Right Management Consultants, Copenhagen, Denmark
* Royal Sun Alliance
* SABMiller (South Africa)
* Saskatchewan Workers’ Compensation Board
* Scott Builders
* Shopper’s Drug Mart
* Spring Manufacturer’s Association (Hawaii)
* St Patrick’s Mercy Home
* Telus
* Thunder Bay District Health Council
* Toronto CFA
* Urban Systems
#### Visiting Positions
**Visiting Professor** 
Dept. of Psychology, State University of New York at Stony Brook 
1982-1983
**Annual Visiting Scholar** 
James Madison University 
2000
#### Ph.D/M.Sc Committees
* Ingrid Chadwick (Smith School of Business)
* Jennifer Turnridge (Kinesiology, Queen’s)
* Rebecca Stead (Psychology, Queen’s)
* Susan Myrden (Business, St. Mary’s University)
* Kyle Brykman  (Smith School of Business)
* Sean Tucker (Smith School of Business)
* Ana d’Orana (Smith School of Business)
#### Ph.D External Examiner (selected list)
* Carlton University
* Dalhousie University
* St Mary’s University (Halifax)
* University of Bergen (Norway)
* University of Cape Town (South Africa)
* University of Guelph
* University of Melbourne (Australia)
* University of Stockholm
* University of the Witwatersrand (South Africa)
* University of Toronto (Industrial Relations)
* University of Toronto (Rotman School of Management)
* University of Waterloo
* University of Western Ontario
### Presentations
#### Conference Presentations (2000 onwards)
Scanlon, M., & Barling, J. (2023) Mental illness stigma towards leaders: Consequences for 
followers’ performance and motivation. Presented at the 82ⁿᵈ Annual Meeting of the Academy of Management, Boston, MA.
Cloutier, A. & Barling, J. (2021, April). Mental illness and perceptions of leader suitability. In 
D. B. Facteau & L. T. Eby (Chairs), Advancing Our Understanding of Mental Illness at Work. To be 
presented at the 36ᵗʰ Society of Industrial and Organizational Psychology Conference. Held Virtually.
Byrne, A. Cloutier, A., & Barling, J. (2020, August). Relative subjective spousal status: How 
spouses impact leadership role occupancy. In D. Mercer (Chair), Broadening our Sight: Integrating Methods 
to Mitigate the Dichotomy of Women and Leadership. Presented online at the 80ᵗʰ Annual Meeting of 
the Academy of Management, Vancouver, BC.
Inness, M., Biricik Gulseren, D., Turner, N., & Barling, J. (2020, April). Transformational 
leadership and love of one’s job: A within-person, between-jobs design. In A. Day (Chair). Leading 
the way to health & happiness? Leadership, innovation, social relationships, and wellbeing. 
Symposium to be presented at the 14th European Academy of Occupational Health Psychology 
Conference, Nicosia, Cyprus.
Nguyen, Q., Turner, N., Barling, J., Axtell, C.M., & Davies, S. (2020, April). Generalized and 
safety-specific transformational leadership: Examining incremental validity of competing leadership 
behaviors. Paper to be presented at the 14th European Academy of Occupational Health Psychology 
Conference, Nicosia, Cyprus.
Turner, N., Deng, C., Barling, J., & Spencer, K. (2019). Differential mental health consequences of 
strikes and lockouts. Postern presented at the American Psychological Association “Work, Stress and 
Health” conference, Philadelphia, PA.
Driver, H., Carleton, E., Fitzpatrick, M., & Barling, J. (2019). Therapy for obstructive sleep 
apnea (OSA) improved the ratings of refreshing sleep, leading to less daytime sleepiness, reduced 
cognitive difficulties and work-related burnout. Poster presented at the conference of the World 
Sleep Society, Vancouver, September 2019.
Carleton, E., Mcevoy, A., Trivisonno, M., Barling, K., & Dupre, K. (2019). The health, affective 
and cognitive predictors of passive leadership. Canadian Psychological Association, Halifax Nova 
Scotia (May, 2019).
Barling, J. (2019). Leaders’ mental health at work. Invited Keynote address at the EAWOP Small 
Group Meeting, “Leadership and Health/Well-being”, University of Exeter, June 20, 2019.
Cloutier, A., & Barling, J. (2019, June). Does a history of domestic violence affect leader 
emergence? Paper in the symposium entitled “Antecedents to Leader Emergence and Leadership 
Behaviors”. Bi- annual conference of the European Association of Work and Organizational 
Psychology, Turin, Italy.
Weatherhead, J., Barling, J., Turner, N., & Montgomery, W. (2019, June). Assessing applicants’ 
leadership potential: Indicators of motivation to lead. Paper in the symposium entitled “Antecedents to Leader Emergence and Leadership Behaviors”. Bi-annual conference of the European Association of Work and Organizational Psychology, Turin, Italy.
Barling, J. (2018, June). Leaders’ mental health at work. Invited keynote address, the 60ᵗʰ 
International Military Testing Association, Kingston, Ontario, October 2018.
Barling, J. (2018, June). Leaders’ mental health at work. Invited keynote address. 28ᵗʰ Annual 
Meeting of the International Congress on Applied Psychology, Montreal.
Cloutier, A., & Barling, (2018, May). Interpartner Victimization and Work Outcomes: The Moderating 
Role of Instrumental and Emotional Support. Association for Psychological Sciences, San Francisco.
Weatherhead, J., & Barling, J. (2018, May). Followers can differentiate the dimensions of 
transformational leadership. The role of follower emotional recognition. Association for 
Psychological Sciences, San Francisco.
Robertson, J.L., Dionisi, A.M., & Barling, J. (2018, April). Linking attachment theory to abusive 
supervision. Poster presented at the Society for Industrial and Organizational Psychology, Chicago.
Barling, J. (2017, October). From transformational leadership to … your leadership. Distinguished 
Speaker, Northwestern Section of the American Urological Association, Savannah, GA.
Weatherhead, J., Barling, J., & Turner, N. (2017, August). Growing up poor limits later leaders. 
Presented in the symposium “Examining the unexamined: How economic status, social class and low 
wages impact employees (Organizers: Purvanoa, R., & Bono, J.), Academy of Management, Atlanta.
Cloutier, A., & Barling, J. (2017, August). Perceptions, expectations and realities of leaders’ 
mental and physical health. Presented in the symposium “Leaders’ physical and mental well-being: 
Antecedents, expectations and outcomes” (Organizer: A. Cloutier). Academy of Management, Atlanta.
Dionisi, A., & Barling, J. (2017, August). What happens at home doesn’t stay at home: Family 
demands predict poor leadership quality. Presented in the symposium “Leaders’ physical and mental 
well-being: Antecedents, expectations and outcomes” (Organizer: A. Cloutier). Academy of 
Management, Atlanta.
Turner, N., Reich, T.C., Barling, J., & Batten, S. (2017, June). Employee disability and managerial 
prejudices in accommodating graduated return to work. Poster to be presented at the 12th 
International Conference on Occupational Stress and Health, "Work, Stress and Health 2017: 
Contemporary Challenges and Opportunities”, Minneapolis, MN.
Byrne, A., & Barling, J. (2017, May). Bend it like Beckham: The influence of star performers on 
non-star performers. Presented at the European Association of Work and Organizational Psychology 
Congress, Dublin, Ireland.
Carleton, E. L. & Barling, J. (2017, May). New Directions in Leadership Research: Extending our 
understanding of the antecedents and consequences of leadership. Symposium accepted at the European 
Association of Work and Organizational Psychology Conference, Dublin, Ireland.
Carleton, E. L. & Barling, J. (2017, May). Daytime sleepiness mediates the effects of leaders’ ADHD 
on laissez-faire leadership. Presented at the European Association of Work and Organizational 
Psychology Conference, Dublin, Ireland.
Weatherhead, J. G., Barling, J., Cloutier, A. E. & Carleton, E. L. (2017, May). Testing mediators 
of the negative effects of passive leadership on mental health and work attitudes. Presented at the 
European Association of Work and Organizational Psychology Conference, Dublin, Ireland.
Robertson, J., Carleton, E. L., & Barling, J. (2016, August). Linking leadership to green behaviors 
through 
pro-environmental work climate. Presented at the Academy of Management, Anaheim, CA.
Barling, J. (2016). Leaders’ mental health at work. Keynote Plenary Session, Canadian Psychological 
Association, Victoria, BC.
Barling. J. (2016). Leaders’ mental health at work. Symposium on “Mental health at work”, 
Association of Psychological Sciences, Chicago, IL.
Byrne, A., & Barling, J. (2016). Your status makes me feel envious and alone. Paper presented in 
the symposium “Refusing to see me: The contours, causes and consequences of invisibility at work” at 
the Academy of Management meeting, Los Angeles, CA.
Carleton, E., & Barling, J. (2016). Reciprocal effects of work stress and sleep problems: A 
five-wave longitudinal study. Paper presented in the symposium “Physical, emotional and biological 
aspects of behavior” at the Academy of Management meeting, Los Angeles, CA.
Weatherhead, J., Carleton, E.L., Barling, J. & Dupré, K.E. (2016). Alcohol as the problem or 
alcohol as the solution? The cyclical nature of workplace injuries, alcohol use and employee mental 
health. Paper presented at the European Academy of Occupational Health Psychology, Athens, Greece.
Barling, J. (2015). Environmental leadership. Symposium Discussant. Presented at the Academy of 
Management meeting, Vancouver, BC.
Carleton, E., Barling, J., Christie, A., Trivisonno, M., Tulloch, K., & Beachamp, M. (2015). 
Long-term effects of abusive supervision on workplace aggression and task performance. Paper 
presented in the symposium “Consequences of Abusive Supervision”. Presented at the Academy of 
Management meeting, Vancouver, BC.
McEvoy, A., MacIsaac, C., Dupré, K.E., & Barling, J. (2015). Towards a broader understanding of 
workplace injuries. Platform paper presented at American Psychological Association “Work, Stress 
and Health” conference, Atlanta, GA.
Trivisonno, M., Carleton, E., Vogel, S., & Barling, J. (2015, May). “Examining the structure of 
grit and its influence on leadership behaviors.” Presented at the Association for Psychological 
Science, New York, NY.
Barling, J. (2015). Invited participant in the symposium “Me-Search: How life experience IGNITE 
your research”. Society for Industrial and Organizational Psychology, Philadelphia, PA.
Barling, J., & Weatherhead, J. (2015). Early childhood behavior problems predict leadership 
emergence— but gender matters! Society for Industrial and Organizational Psychology, Philadelphia, 
PA.
Barling, J. (2015). New developments in abusive supervision research. Symposium Discussant. Society 
for Industrial and Organizational Psychology, Philadelphia, PA.
Barling, J. (2014). Answering the call: New directions in the study of workplace interactions. 
Symposium Discussant. Academy of Management Conference, Philadelphia, August.
Byrne, A., & Barling, J. (2014). When wives bring home the job status: The effect of job status 
leakage on marital instability. Presentation at the Academy of Management Conference, Philadelphia, August.
Byrne, A., & Barling, J. (2014). A little status goes a long way: Envy mediates the effect of 
status dispersion on ostracism. Presentation at the Academy of Management Conference, Philadelphia, 
August
Carleton, E., Barling, J., Dupre, K. (2014). A longitudinal investigation of the cross-over of 
injuries from work to home. Poster Presentation at the Work Family Research Network Conference, New 
York, NY June 2014.
Carleton, E., Barling, J. (2014, June). “The role of family stress in understanding the effects of 
workplace injuries on sleep.” Presented at the Smith School of Business Conference on Sleep and 
Work, Kingston, ON.
Robertson, J., & Barling, J. (2014). Environmentally-specific transformational leadership and 
employees’ environmental performance. 28ᵗʰ International Congress of Applied Psychology, Paris, July.
Barling, J. (2013). Discussant for symposium entitled “A love/hate relationship with the job”. 10ᵗʰ 
Work, Stress and health Conference, American Psychological Association, Los Angeles.
Barling, J. (2013). Discussant for symposium entitled “Fresh perspectives on workplace aggression”. 
10ᵗʰ Work, Stress and health Conference, American Psychological Association, Los Angeles.
Dionisi, A.M., & Barling, J. (2013). Spillover and crossover of sex-based harassment from work to 
home: Supervisor gender harassment affects marital functioning via targets’ anger. Paper presented 
at the Academy of Management 2013 Annual Meeting, Lake Buena Vista, FL.
Barling, J. (2012). Being well, leading well: Leaders’ psychological distress predicts leadership 
behaviors. (Keynote address). Canadian Psychological Association, Halifax, June.
Barling, J. (2012). Followership. Canadian Society for Psychomotor Learning and Sport Psychology 
(SCAPPS). (Keynote address.) Halifax, November.
Barling, J. (2012). Advancing dignity and safety at work. Chair, invited symposium, International 
Congress of Psychology, Cape Town, South Africa.
Barling, J. (2012). New developments in transformational leadership. Invited talk, International 
Congress of Psychology, Cape Town, South Africa.
Dionisi, A.M., Dupre, K., & Barling, J. (2012). To voice or not to voice: An examination of the 
willingness to report workplace aggression. Invited paper, International Congress of Psychology, 
Cape Town, South Africa.
Barling, J. (2012) The Family-Supportive Workplace: Understanding Supervisor and Organizational 
Support for Family. Discussant for symposium presented at the Academy of Management, Boston, MA.
Byrne, A., Barling, J., & Dupre, K. (2012). Leaders' Apologies: Understanding and Mitigating 
Negative Outcomes for Leaders and Subordinates. Paper presented at the Academy of Management, 
Boston, MA
Barling, J. (2012). Leaders’ mental health and their leadership behaviors. Invited speaker, 
Canadian Psychological Association, Halifax, NS.
Christie, A., Dionisi, A., & Barling, J. (2012). Gaining power, reactive egoism, and 
self-interested behavior. Presented at the Canadian Psychological Association, Halifax, NS.
Bergenwall, A., Barling, J., et al. (2012). Being well, leading well: Leaders’ psychological 
well-being predicts leadership behaviors. Presented at the Society for Industrial and 
Organizational Psychology, San Diego, CA.
Bergenwall, A., Barling, J., & Kelloway, E.K. (2012). Odd jobs and bad habits: Smoking-related 
outcomes of children’s employment. Presented at the Society for Industrial and Organizational 
Psychology, San Diego, CA.
Byrne, A., Dupré, K.E., & Barling, J. (2011). The Relationship between apologies and well-being 
among leaders in organizations. Presented at APA and NIOSH interdisciplinary conference on 
occupational stress and health (Work, Stress, and Health: Work and Well-Being in an Economic 
Context), Orlando, FL.
Dupré, K.E., Barling, J., & Dawe, K. (2011). Outcomes of vicarious workplace aggression. Presented 
at APA and NIOSH interdisciplinary conference on occupational stress and health (Work, Stress, and 
Health: Work and Well-Being in an Economic Context), Orlando, Fl.
Beauchamp, M.R., Barling, J., Li, Z.., Morton, K. L., Keith, S. E., & Zumbo, B. D. (2010). 
Reliability and validity of the transformational teaching questionnaire (TTQ). Paper presented at 
the annual conference of the Society of Behavioral Medicine, Seattle, WA, USA .(Annals of 
Behavioral Medicine, S138.)
Beauchamp, M.R., Barling, J., & Morton, K. L. (2010). Effects of a transformational teaching 
intervention on adolescent self-determined motivation: A randomized controlled feasibility trial. 
Paper presented at the annual conference of the Society of Behavioral Medicine, Seattle, WA, USA. 
(Annals of Behavioral Medicine, S212)
Hershcovis, M. S. & Barling, J. (2010). Comparing the outcomes of sexual harassment and workplace 
aggression: A meta-analysis to guide future research. Presented at the Society of Industrial and 
Organizational Psychology Conference, Atlanta, GA.
Hoption, C., Christie, A.M., & Barling, J. (2010). There's no 'leader' in 'follower', is there? 
Implicit followership theories. Presented at the 2010 Association of Psychological Science Annual 
Convention, Boston, MA.
Inness, M., Turner, N., Barling, J., & Stride, C.B. (2010). Transformational leadership and 
employee safety performance: A within-person, between-job design. In E.K. Kelloway (Chair). 
Leadership and well-being. Paper presented at the 70th Annual Meeting of the Academy of Management, 
Montréal, Canada.
Lys, R. E. & Barling, J.(2010). Leadership and employee counterproductive work behaviors: The 
moderating role of leader mental health. Academy of Management, Montreal, Canada.
Morton, K. L., Barling, J., Mâsse, L., Rhodes, R., Zumbo, B. D., & Beauchamp, M. R. (2010). The 
application of transformational leadership theory to parenting and adolescent health and 
well-being.
Paper presented at the annual conference of the Canadian Society for Psychomotor Learning and 
Sports Psychology (SCAPPS), Ottawa, Ontario.
Robertson, J.L., & Barling, J. (2010). Do as I Say and as I Do: Environmentally-Specific 
Transformational Leadership, Modeling and Employees’ Pro-Environmental Behaviors. Poster 
Presentation at the Society for Industrial and Organizational Psychology Annual Conference, 
Atlanta, GA.
Robertson, J.L., & Barling, J. (2010). Organizational Citizenship Behaviors (OCBs) and the 
Collective: An Extension on the Different Forms of OCBs. Paper Presentation at Symposium, Green 
Shoots: New Directions and Opportunities for Workplace Pro-Environmental Behavior Research, at the 
Academy of Management Annual Conference, Montreal Quebec.
Simola, S.K., Barling, J., & Turner, N. (2010). Transformational leadership and level of care 
reasoning. In J. Crotty (Chair). Ethical climate and ethical leadership. Paper presented at the 
70th Annual Meeting of the Academy of Management, Montréal, Canada.
Turner, N., Barling, J., Dawson, J.F., Stride, C.B., Wall, T.D., Parker, S.K., Patterson, M.G., & 
West, M.A. (2010). Human resource management practices and workplace injury rates. In Y. Yanadori 
(Chair).
Management of the employment relationship. Paper presented at 53rd Annual Conference of the 
Administrative Sciences Association of Canada, Regina, SK.
Byrne, A., Barling, J., & Hoption, C. (2009). Who’s laughing now? How leadership and humor impact 
relationship outcomes. Paper presented at the Society for Industrial and Organizational Psychology, 
New Orleans, LA.
Christie, A., & Barling, J. (2009). Pay dispersion and health: The moderating role of individual 
relational models. Paper presented at the Work, Stress, and Health Conference, San Juan, Puerto 
Rico.
Christie, A., & Barling, J. (2009). Disentangling the indirect link between SES and health: The 
dynamic role of work stressors and personal control. Paper presented at the Administrative Sciences 
Association of Canada Conference, Niagara Falls, ON.
Hoption, C., Christie, A., & Barling, J (2009). The F-Word: The follower label, work attitudes, 
well-being, and performance. Paper presented at the European Association of Work and Organizational 
Psychology Congress, Santiago de Compostela, Spain.
Hoption, C., Christie, A., & Barling, J (2009). The F-Word: Effects of the Follower Label. Paper 
presented at the Society for Industrial and Organizational Psychology Conference, New Orleans, LA.
Inness, M., Barling, J., & Turner, N. (2009). Transformational leadership and employee safety 
performance: Context specificity or spillover? In S. Nichols (Chair). Predicting safety outcomes. 
Paper presented at the 117th Annual Convention of the American Psychological Association, Toronto, 
Canada.
Turner, N., Barling, J., Reich, T.C., & Batten, S. (2009). Managerial prejudices against type of 
employee disability in return-to-work accommodation. Poster presented at Work, Stress, and Health: 
Global Concerns and Approaches, San Juan, PR.
Turner, N., Bruning, P.F., Hershcovis, M.S., Sung, F., Li, C., & Chen, K. (2009). Adding insult to 
injury: Experience of workplace injury, lack of interpersonal support, and subsequent psychological 
distress. Poster presented at Work, Stress, and Health: Global Concerns and Approaches, San Juan, PR.
Barling, J., Turner, N., Dezan, H., & Carroll, A.E. (2009). Structure and correlates of apologies 
from leaders in organizations. In L. Erskine (Chair). Leader behaviors. Paper presented at the 68th 
Annual Meeting of the Academy of Management, Anaheim, CA.
Barling, J., Turner, N., Kelloway, E.K., Sivanathan, N., Arnold, K.A., & Loughlin, C.A. (2008). 
Transformational leadership and employee well-being. In J. Barling (Chair) New Directions in Work 
and Well-Being. Paper presented at the British Psychological Society’s Division of Occupational 
Psychology Conference, Stratford-Upon-Avon, UK.
Carson, J., & Barling, J. (2008). Health behaviors and work performance: The mediating effects of 
mood and cognitive function. Paper presented in poster session at the Association of Psychological 
Science. Annual Meeting. Chicago, U.S.
Christie, A.M., Barling, J., & Turner, N. (2008). Attitudinal and behavioral outcomes of pseudo- 
transformational leadership. Paper presented at the Association of Psychological Science Annual 
Convention, Chicago, IL.
Christie, A.M. & Barling, J. (2008). Exploring the social gradient in health: How work experiences 
and resources spiral. Paper presented at the Work, Stress, and Health Conference, Washington, DC.
Christie, A.M. & Barling, J. (2008). Beyond status: The effects of status inequality on well-being 
in organizations. Paper presented at the British Psychological Society’s Division of Occupational 
Psychology Conference, Stratford, UK.
Christie, A.M. & Barling, J. (2008). The effects of status inequality on performance, absences, and 
thriving within teams. In K. Bettenhausen (Chair) Predicting Team Performance. Paper presented at 
the Academy of Management Annual Meeting, Anaheim, CA.
Christie, A.M., Barling, J., & Turner, N. (2008). Attitudinal and behavioral outcomes of pseudo- 
transformational leadership. Poster presented at the 20th Annual Convention of the Association for 
Psychological Science, Chicago, IL.
Hershcovis, M.S., & Barling, J. (2008). Outcomes of workplace aggression and sexual harassment: A 
meta-analytic comparison. Presented at the 7ᵗʰ Annual Work, Stress, & Health Conference, 
Washington, DC.
Inness, M., Barling, J., & Turner, N. (2008). Transformational leadership and safety performance: 
The mediating role of meaningful work. Poster presented at the 8th European Academy of Occupational 
Health Psychology, Valencia, Spain.
Teed, M.C., Kelloway, E.K. & Barling, J. (2008). Incidents and Predictors of Workplace Violence and 
Aggression. Paper accepted for presentation at the biannual conference of the European Academy for 
Occupational Health Psychology, Valencia, Spain.
Barling, J. & Carson, J. (2007). Toward an agenda for research on work and well-being. Paper 
presented 
in symposium at the European Congress of Work and Organizational Psychology (EAWOP). Stockholm, 
Sweden.
Christie, A.M. & Barling, J. (2007). Toward a relational model of status inequality. In K. 
Bettenhausen (Chair). Power in Organizations. Paper presented at the 2007 Academy of Management 
Annual Meeting, Philadelphia, PA.
Christie, A.M. & Barling, J. (2007). Status inequality and well-being. In J. Barling (Chair). New 
developments in work and well-being. Paper presented at the 13th European Congress of Work and 
Organizational Psychology, Stockholm, Sweden.
Dawe, K., Dupré, K.E. & Barling, J. (2007). Harming those who serve: Direct and indirect customer 
initiated violence. Poster presented at annual SIOP Conference, New York, NY.
Hershcovis, M.S. & Barling, J. (2007). Towards a relational model of workplace aggression: Some 
meta- analytic evidence. Paper presented at the 22nd Annual Society for Industrial Organizational 
Psychology Conference, New York, NY.
Hoption, C.B., Barling, J., & Turner, N. (2007). Transformational leadership and humor. Poster 
presented at the 19th Annual Convention of the Association for Psychological Science, Washington, 
DC.
Inness, M., Barling, J., & Turner, N. (2007). Situation and person predictors of workplace safety 
behaviors: A within-person, between-jobs design. In S. Ohly & C. Fritz (Chairs). Job demands and 
performance: Examining creativity, innovation and initiative. Paper presented at the 21st Annual 
Society for Industrial and Organizational Psychology meetings, New York, NY.
Simola, S.K., Barling, J., & Turner, N. (2007). Relationship between transformational leadership 
and moral problem solving orientation. In D.M. Mayer (Chair). New developments in ethical 
leadership: Multilevel and international perspectives. Paper presented at the 67th Annual Meeting 
of the Academy of Management, Philadelphia, PA.
Turner, N., Barling, J., Kelloway, E.K., Sivanathan, N., & Loughlin, C.A. (2007). Leading others to 
well- being: Direct and indirect effects of transformational leadership. In J. Barling (Chair). New 
developments in work and well-being. Paper presented at the 13th European Congress of Work and 
Organizational Psychology, Stockholm, Sweden.
Arnold, K.A., Barling, J. & Turner, N. (2006). Transformational leadership and context-free 
well-being:The mediating role of meaning at work. Paper presented at Work, Stress and Health: 
Making a Difference in the Workplace – The Sixth APA and NIOSH Interdisciplinary Conference on 
Occupational Stress and Health, Miami, Florida, March 2-4, 2006.
Arnold, K.A., Barling, J., & Turner, N. (2006). Transformational leadership and psychological 
well-being: The mediating role of meaningful work. In P. L. Perrewé (Chair). Transformational 
leadership and 
occupational health. Paper presented at the 6th Work, Stress, and Health conference, Miami, FL.
Carson, J., Barling, J., & Turner, N. (2006). Group alcohol climate, alcohol consumption, and 
student 
performance. Poster presented at the 18th Annual Convention of the Association for Psychological 
Science, New York, NY.
Carson, J., & Barling, J. (2006). Romantic Relationships at work: Old issues, new challenges. Paper 
presented in poster session at the European Academy of Occupational Health Psychology (EA-OHP) 
Conference. Dublin, Ireland.
Christie, A.M., Barling, J., & Turner, N. (2006). Pseudo-transformational leadership: Towards the 
development and test of a model. In K. Campbell (Chair). Understanding transformational leadership. 
Paper presented at the Academy of Management Annual Meeting, Atlanta, GA.
Christie, A.M., Barling, J., & Turner, N. (2006). A model of pseudo transformational leadership. 
Paper presented at the Association of Psychological Science Annual Convention, New York City, NY.
Dupré, K.E., Barling, J., & Hershcovis, M.S. (2006). Comparing supervisor- and coworker-targeted 
aggression. Poster presented at the 7th Conference of the European Academy of Occupational Health 
Psychology, Dublin, Ireland.
Dupré, K.E., Barling, J., & Hershcovis, M.S. (2006). Target-specific nature of workplace 
aggression. Poster presented at the Canadian Association for Research on Work and Health Joint 
International Conference, St. John’s, Newfoundland.
Dupré, K.E., Barling, J. & Turner, N. (2006). Anger, injustice and the target of aggression. Poster 
resented at the 7th full conference of the European Academy of Occupational Health Psychology, 
Dublin, Ireland.
Dupré, K.E., Barling, J. & Turner, N. (2006). The progression of aggression: A longitudinal 
analysis of aggression directed at workplace supervisors. Poster presented at SafetyNet and the 
Canadian Association for Research on Work and Health (CARWH) joint international conference 
(Research on Workplace Health and Safety: From the Core to the Margins), St. John’s, NL.
Dupré, K.E., Barling, J. & Herschovis, M.S. (2006). Supervisor versus coworker target specificity 
in the prediction of workplace aggression. Poster presented at SafetyNet and the Canadian 
Association for Research on Work and Health (CARWH) joint international conference (Research on 
Workplace Health and Safety: From the Core to the Margins), St. John’s, NL.
Dupré, K.E., Barling, J., & Turner, N. (2006). The role of perceptions of organizational sanctions 
in the prevention of aggression. Poster presented at the 18th Annual Convention of the Association 
for Psychological Science, New York, NY.
Hershcovis, M.S. & Barling, J. (2006). Towards a relational model of workplace aggression: Some 
meta- analytic evidence. Presented at the 7th Conference of the European Academy of Occupational 
Health Psychology, Dublin, Ireland.
Inness, M., Barling, J., & Turner, N. (2006). Predicting workplace safety behaviors: A 
within-person, between-jobs design. Poster presented at the 7th European Academy of Occupational 
Health 
Psychology, Dublin, Ireland.
Inness, M.L., Barling, J., Rogers, K., & Turner, N. (2006). The impact of tobacco tax changes on attempts 
to quit smoking. Poster presented at the 18th Annual Convention of the Association for Psychological 
Science, New York, NY.
Turner, N., Barling, J., Dawson, J.F., Stride, C.B., Wall, T.D., Parker, S.K., Patterson, M.G. & West, M.A. 
(2006). Human resource practices and safety performance. Poster presented at the SafetyNet/Canadian 
Association for Research on Work and Health Conference (“Research on Workplace Health and Safety: 
From the core to the margins), St. John’s, Newfoundland.
Tucker, S., Turner, N., Barling, J., & McEvoy, M. (2006). Interpersonal influences on teenagers’ hostile 
aggression: A prospective study of ice hockey. Poster presented at the 18th Annual Convention of the 
Association for Psychological Science, New York, NY.
Barling, J., Kelloway, E.K., Turner, N., Sivanathan, N., & Loughlin, C.A. (2005). Leading others to wellbeing: 
Direct and indirect effects of transformational leadership. In C. Mason, S.K. Parker, & M.A. Griffin 
(Chairs). Transformational leadership: From leader interventions to team outcomes. Paper presented at 
the 65th Annual Meeting of the Academy of Management, Honolulu, HI.
Dupré, K.E., Barling, J. & Turner, N. (2005). Personal and situational predictors of aggression: A within person analysis. Paper presented at the Annual Meeting of the Academy of Management, Honolulu, HI, 
Organizational Behavior and Human Resource Management Divisions.
Hershcovis, M.S., & Barling, J. (2005). Adding insult to injury: A meta-analysis on the outcomes of 
workplace aggression. Paper presented at the Annual Academy of Management Conference, Honolulu, 
HI.
Inness, M., LeBlanc, M., & Barling. J. (2005) The specificity of predictors of Types II and III workplace 
aggression. Paper presented at the 65th Annual Meeting of the Academy of Management, Honolulu, HI.
Sivanathan, N., Turner, N., & Barling, J. (2005). Effects of transformational leadership training on 
employee safety performance: A quasi-experiment. In J. Cordery (Chair). Health, safety, and well-being in 
the workplace. Paper presented at the 65th Annual Meeting of the Academy of Management, Honolulu, 
HI. (In Best Paper proceedings)
Tucker, S., Barling, J., & Turner, N. (2005). Tough calls: Apologies and transformational leadership. Poster 
presented at the 19th Annual Society for Industrial and Organizational Psychology meetings, Los 
Angeles, CA.
Arnold, K.A., Barling, J. & Iverson, R.D. (2004). Dirty work and well-being: The roles of occupational 
identification, passing and choice. Paper presented at Academy of Management Conference, New 
Orleans, Louisiana.
Dupré, K.E. & Barling, J. (2004). The escalation of workplace aggression. Paper presented at the Annual 
Meeting of the Academy of Management, New Orleans, LA, Organizational Behavior Division.
Dupré, K.E., Inness, M., Connelly, C.E., Barling, J. & Hoption, C. (2004). On the importance of reasons for 
workplace aggression among teenage employees. Paper presented at the Administrative Sciences Association of Canada Conference, Quebec City, QC, Organizational Behavior Division.
Dupre, K, Inness, M., Connelly, C., Barling, J, & Hoption, C. (2004). Adolescent antagonism: Predicting 
workplace aggression in part-time teenage employees. Paper presented at the annual meeting of the 
Administrative Sciences Association of Canada, Quebec City.
Hershcovis, S., Turner, N., Barling, J., Arnold, K., Dupre, K., Inness, M., LeBlanc, M., & Sivanathan, N. 
(2004). A Meta-Analysis of Workplace Violence. Paper presented at the 64th Annual Meeting of the 
Academy of Management, New Orleans.
Hershcovis, M.S., Turner, N., Barling, J., Arnold, K.A., Dupré, K.E., Inness, M., LeBlanc, M.M., Sivanathan, 
N. (2004). Right on target. A meta-analysis of the predictors of insider-initiated workplace aggression. 
Paper presented at the Annual Academy of Management Conference, New Orleans, LA.
Hershcovis, S.M., Turner, N., Barling, J., Arnold, K.A., Dupré, K.E., Inness, M., LeBlanc, M.M. & 
Sivanathan, N. (2004). Predictors of workplace aggression: A meta-analysis. Paper presented at the 
Annual Meeting of the Academy of Management, New Orleans, LA, Organizational Behavior Division.
Sivanathan, N., Barling, J., & Turner, N. (2004). Transformational leadership and employee safety: A 
quasi-experiment. In N. Turner (Chair). Seeking safety with others: An international symposium on the 
psychology of workplace safety. Invited symposium at the British Psychological Society’s Occupational 
Psychology Conference, Stratford, UK.
Arnold, K.A. & Barling, J.(2003). Well-being of dirty workers: The role of meaningful work. Poster 
presented at Work, Stress and Health: New Challenges in a Changing Workplace – The Fifth APA and 
NIOSH Interdisciplinary Conference on Occupational Stress and Health, Toronto, ON.
Dupré, K.E. & Barling, J. (2003). A cross-situational examination of aggression. Paper presented at APA 
and NIOSH interdisciplinary conference on occupational stress and health (Work, Stress, and Health: 
New Challenges in a Changing Workplace), Toronto, ON.
Francis, L., Kelloway, E.K & Barling, J. (2003). Justice as a stressor. Paper presented at the conference 
Work, Stress & Health, Toronto, ON.
Inness, M., & Barling, J. (2003). Situational specificity and individual differences in the prediction of 
workplace aggression. Poster presented at the Fifth Interdisciplinary Conference on Occupational Stress 
and Health, Toronto.
Inness, M., & Barling, J. (2003). Putting ‘health’ back into occupational health psychology. Paper 
presented at the Annual Convention of the British Psychological Society, Bournemouth, England.
Sivanathan, N., Arnold, K. A., Turner, N., & Barling. J. (2003). Lead well to be well: Transformational 
leadership & well-being. Poster presented at the International Positive Psychology Summit; Washington, 
DC. USA.
Sivanathan, N., Barling, J., Loughlin, C., & Kelloway, K. (2003). Leading others to well-being: 
Transformational leadership and employee well-being. Paper presented at the Industrial Organizational 
Psychology meetings; Orlando, FL. USA.
Sivanathan, N., & Barling, J., Loughlin, C., & Kelloway, K. (2003). Transformational leadership and 
employee well-being. Paper presented at the APA/NIOSH Work, Stress, and Health Conference, Toronto, 
Canada.
Sivanathan, N., Barling, J., Loughlin, C. & Kelloway, E.K. (2003). Leading others to wellbeing: 
Transformational Leadership and wellbeing. Paper presented at the conference Work, Stress & Health, 
Toronto, ON.
Dupré, K.E., Inness, M., Barling, J., Connelly, C. & Hoption, C. (2002) Adolescent antagonism: Predicting 
workplace aggression in part-time teenage employees. Poster presented at the Annual Meeting of the 
Society for Industrial and Organizational Psychology, Toronto, ON.
Iverson, R. Barling, J., Kelloway, E.K. (2002). High quality work, morale, and occupational injuries. Paper 
presented as part of the symposium entitled, Safety in the New Millennium: Multi-level examination of 
safety in organization at the annual meeting of the Academy of Management, Denver CO.
Kelloway, E.K., Kelley, E., Gatien, B. & Barling, J. (2002). Remote transformational leadership. Paper 
presented at the annual meeting of the Society for Industrial and Organizational Psychology, Toronto, 
ON
Dupré, K.E. & Barling, J. (2001). The prediction and prevention of workplace aggression and violence. 
Paper presented at the Annual Meeting of the Academy of Management, Washington, DC, 
Organizational Behavior Division.
Inness, M., Gallagher, D.G., Barling, J., & Iverson, R. (2001). The relationship between ‘non-standard’ 
employment status, health and safety training, and work-related injury or illness. Paper presented at the 
VII European Conference of Organizational Psychology and Health Care, Stockholm.
Kelloway, E.K., Barling, J. & Fowkes, E.K. (2001). Maintaining career motivation following downsizing. 
Paper presented at the annual meeting of the European Association for Work /Organizational 
Psychology, Prague, Czech. Republic.
Loughlin, C., Kelloway, E.K., Barling, J. & Nault, A. (2001). OCBs and CPBs: Separate but related 
constructs. Paper presented at the annual meeting of the Society for Industrial and Organizational 
Psychology, San Diego, CA
Wood, S.J., Turner, N., Lasaosa, A., Barling, J., & Parker, S.K. (2000). Organizational practices and safety 
performance: An exploratory study. In N. Turner & J. Barling (Chairs), New perspectives on HRM and 
performance. Symposium at the 60th Annual Meeting of the Academy of Management, Toronto.
Wood, S.J., Turner, N., Lasaosa, A., Barling, J., & Parker, S.K. (2000). HRM and safety. In T. Keenoy 
(Chair), “What about the workers?” Employee perspectives on HRM. Symposium at BUIRA HRM Study 
Group Conference, London, UK.
#### **Invited Talks (selected list, 1985 onwards)**
Albert Einstein College of Medicine, New York 
Bar Ilan University (Israel) 
Ben Gurion University (Israel) 
Carleton University 
Clark University (Mass.) 
Colorado State University 
Dan Management & Organization Studies, Western University 
Drexel University (Philadelphia) 
Hebrew University of Jerusalem (Israel) 
HEC, Montreal 
James Madison University 
Kansas State University 
Memorial University of Newfoundland 
Portland State University 
St. Mary’s University (Halifax) 
State University of New York at Binghamton 
State University of New York at Stony Brook 
Technion University (Israel) 
University of Alberta 
University of Bergen (Norway) 
University of British Columbia 
University of Calgary (Haskayne) 
University of Cape Town (South Africa) 
University of Exeter (UK) 
University of Georgia (USA) 
University of Guelph 
University of Michigan 
University of Murcia (Spain) 
University of Ottawa 
University of Porto (Portugal) 
University of Sheffield (UK) 
University of South Florida 
University of Stockholm (Sweden) 
University of Toronto (Rotman School) 
University of Victoria (Australia) 
University of Waterloo 
University of Western Ontario 
University of Witwatersrand (South Africa) 
Wilfrid Laurier University
#### **Invited Keynote Talks at Conferences (selected list)**
7th European Conference on Organizational Psychology for Human Service Work (Stockholm) 
American Psychological Association (Toronto) 
Association of Psychological Sciences Conference (Washington DC) 
_British Psychological Society's_ Annual Occupational _Psychology Conference_ 
CRITEOS, Centre de Recherche et d’Intervention pour le Travail, l’Efficacité Organisationnelle et la Santé, Porto Elgre, Brazil 
European Academy of Occupational Health Psychology (Barcelona) 
European Work and Organizational Psychology Conference (Stockholm) 
International Conference on Work Values (Jerusalem) 
North American Society for the Psychology of Sport and Physical Activity 
Northeastern Section of the American Urological Association (Savannah, GA) 
Brinkley Smithers Symposium on Alcohol in the Workplace (New York) 
Society for Industrial and Organizational Psychology (Chicago) 
Society for Industrial and Organizational Psychology (South Africa) 
Third International Positive Psychology Conference (Washington DC) 
EAWOP Small Group Meeting “Leadership and health/well-being”, University of Exeter, UK
#### **Keynote Speaker for Companies on Leadership, Safety and Employee Well-Being (selected list)**
Algonquin College 
Association of Professional Executives of the Public Service of Canada (APEX) 
Association of Workers’ Compensation Boards of Canada 
BluEra 
British Columbia Workers’ Compensation Board 
Canadian Centre for Occupational Health and Safety 
Canadian Association of University Teachers 
Centre for Health Promotion, University of Toronto 
CFA Vancouver – Women’s Symposium 
Copenhagen Hospital Corporation, Denmark 
Count of Lambton Community Health Services Department 
Healthy Outcomes Conference, BC 
Industrial Accident Prevention Association (Ontario, multiple talks) 
Human Resource Professional Association of Ontario 
Safe Communities Foundation (multiple talks) 
Nova Scotia Safety Council 
Psychologically Healthy Workplace Awards (Nova Scotia; Ontario) 
Saskatchewan Association of Health Organization 
Saskatchewan Workers’ compensation Board 
BC Mental Health and Addiction Services 
Kawartha District School Board 
York Catholic District School Board
### Awards
#### Fellowships
Canadian Psychological Association (2012)
European Academy of Occupational Health Psychology (2008)
Society of International and Organizational Psychology (2008)
Association for Psychological Science (2008)
Royal Society of Canada (2002)
#### Research Awards
Listed in the top 2% of world’s most cited scientists, 2020 
[https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000918](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000918)
Distinguished University Professor, Queen’s University, 2020 -
Top 100 authors in the field of industrial/organizational psychology (total N = 8,603), rank .72%) in terms of influence on education, based on citations in textbooks
Lifetime Career Achievement in Research Award, American Psychological Association, NIOSH, and Society for Occupational Health Psychology (2017)
Top 100 authors in the field of organizational behavior (total N = 16,289, rank .6%) in terms of influence on education, based on citations in textbooks 
[https://journals.aom.org/doi/10.5465/amle.2017.0488](https://journals.aom.org/doi/10.5465/amle.2017.0488))
Member, Society for Organizational Behavior (by invitation only) (2017)
Distinguished Scientific Contribution, Canadian Society for Industrial & Organizational Psychology (C-SIOP) (2016)
Queen’s School of Business “Award for Research Excellence” (2016)
Borden Chair of Leadership, Queen’s University, 2012-2017 (2012)
Outstanding Career Contribution in Occupational Health Psychology, European Association for Occupational Health Psychology (2008)
Queen’s Research Chair (renewed 2007-2012)
Honorary Professor, University of the Witwatersrand (2008-2011; renewed 2011-2014)
Queen’s University’s, Queen’s Research Chair (2002-2007)
Annual Visiting Scholar, James Madison University (2000)
Weingarten Scholar-in-Residence, University of Guelph (1997)
Queen’s University Prize for “Excellence in Research” (1997)
Queen’s School of Business “Award for Research Excellence” (1995)
Scholar-in-Residence, University of Georgia, Athens GA (1991)
#### Teaching Awards
Smith School of Business, Award for Excellence in Graduate Student Supervision (2019)
Queen’s University Award for Excellence in Graduate Student Supervision (2008)
National Post’s “Leaders in Business Education” (2001)
One-week Executive Development Program in Leadership that I co-developed was ranked as one of the top ten international programs in _Business Week_ annual survey. The program is still running four times a year.
Named in MacLean’s Annual Survey as one of Queen’s University’s “Most Popular Professors” (1996)
#### Grants & Funding
**Principal Investigator**
Early socioeconomic adversity and the development of later formal leadership (2018-2023) 
SSHRC | $209,000
Growing up poor limits the development of later leadership (2016-2020) 
Monieson Center | $59,400
Leaders’ psychological well-being and leadership behaviours (2012-2017) 
SSHRC | $251,000
Transformational leadership and humility (2007-2010) 
SSHRC | $100,000
The development of leadership: Multidisciplinary perspectives (2007-2010) 
SSHRC | $100,000
Leadership and HR in the auto sector (2001-2004) 
Center for Automotive Materials and Manufacturing | $210,000
Financial performance and safety performance (2001-2003) 
Industrial Accident Prevention Association | $10,000       
Take this job and love it (2004-2007) 
SSHRC | $110,000
Some effects of the new employment relationship on employees and their families (1999-2002) 
SSHRC | $61,000
The nature and consequences of parents’ employment role experiences (1986-1992) 
Imperial Oil | $42,000
The nature and consequences of contingent employment (1995-1998) 
Imperial Oil | $30,000
Training shop stewards to enhance union commitment (1992-1995) 
SSJRC | $66,000
Causes and consequences of different patterns of organizational and union commitment (1989-1992) 
SSHRC | $50,000
Work and Family (1986-1992) 
SSHRC | $50,000
**Co-investigator**
Does employee mental health affect leader role occupancy? PI: Anika Cloutier 
SSHRC-IDG | $55,124
Understanding the experience and widespread consequences of job-status leakage in traditional and non-traditional families PI: Alyson Byrne 
SSHRC | $143,857
Personal and family consequences of injuries at work PI: Kate Dupre 
SSHRC | $190,000
Transformational teaching and adolescent physical activity promotion: Adolescence-in-Motion (AIM) Trial. PI: Mark Beauchamp 
CIHR | $180,000              
A dynamic exploration of status attainment, maintenance and abuse. PI: Amy Christie 
SSHRC | $100,000             
Individual outcomes of vicarious exposure to aggression, sexual harassment, and injuries at work. PI: Kate Dupre 
SSHRC | $125,000
Transformational teaching and adolescent physical activity promotion: Advance in motion. PI: Mark Beauchamp 
SSHRC | $100,000
What we know about the health and organizational costs of smoking. PI: Caroline Weber 
Marion Merrill Dow | $55,000
International conference on the psychology of labor relations. PI: Lois Tetrick  
American Psychological Association | $17,000
### Service
#### University Service (Major Responsibilities)
* Associate Dean, Research, PhD & Programs, Smith School of Business, 1999-2011
* Chair, Research, PhD & Programs, 1997-1999
* Director, Executive MBA Program, Smith School of Business, 1995-6
* Chair, Graduate Program, Dept. of Psychology, Queen’s University, 1988-1991
* Head, Division of Industrial Psychology, University of the Witwatersrand, 1979-1984
#### Association & Government Responsibilities
* Chair, Taskforce on Workplace Violence, American Psychological Association, 2000-2002
* Chair, Ontario Council for Occupational Health and Safety, 1989-1991
#### Association Responsibilities
* Scientific Committee, 8th International Conference on “Work, stress and health”, American Psychological Association, Orlando, FL. - 2011
* Scientific Committee, 7th International Conference on “Work, stress and health”, American Psychological Association, Puerto Rico - 2009
* Scientific Committee, 6th International Conference on “Work, stress and health”, American Psychological Association, Washington, DC - 2008
* Scientific Committee, 5th International Conference on “Work, stress and health”, American Psychological Association, Miami - 2006
* Scientific Committee, 2nd International Conference of the International Commission on Occupational Health, Tokyo - 2005
* Co-chair, 4th International Conference on “Work, stress and health”, American Psychological Association, Toronto - 2003
* Member, Board of Minerva Canada - 2001-2003
* Chair, Task Force on Workplace Violence, American Psychological Association - 2000-2002
* Member, Board of the Ontario Pulp and Paper Health and Safety Association - 1999-2001
* Member, External Advisory Panel, APA/NIOSH Occupational Health Psychology Training Program - 1998-2000
* Member, Work and Family Committee: Child, Youth and Family Policy Research Centre, Toronto - 1990-1992
* Chair, Task Force on Occupational Stress, Advisory Council to the Minister of Labour on Occupational Health and Safety - 1989-1991
* Member, Advisory Council to the Minister of Labour on Occupational Health and Occupational Safety - 1988-1989
* Member, Board of Alternatives (a treatment centre for men who abuse their wives) - 1988-1989
#### Association Memberships
Academy of Management 
American Psychological Association 
Association for Psychological Sciences (Fellow) 
Canadian Psychological Association (Fellow) 
European Academy of Occupational Health Psychology (Fellow) 
Royal Society of Canada (Fellow) 
Society for Industrial and Organizational Psychology (Fellow)
#### Reviewer for Tenure, Promotion, Distinguished Professorship Positions (selected list)
ALBA – American College of Greece, Greece 
Association for Psychological Sciences (Fellowships for APS) 
Australian Research Council Federation Fellowship 
Bar Ilan University (Israel) 
Clemson University 
Drexel University 
George Washington University 
Georgetown University 
Kansas State University 
Manchester School of Management 
Penn State University 
Portland State University 
Royal Society of Canada 
Seattle University 
Simon Fraser University 
Society for Industrial and Organizational Psychology (Fellowships for SIOP) 
Tel Aviv University 
UBC (Sauder School of Management) 
University of Alberta 
University of Calgary (Haskayne) 
University of Connecticut 
University of Georgia 
University of Illinois at Chicago 
University of Manitoba 
University of Michigan 
University of Minnesota (Carlson School of Management) 
University of Oregon 
University of South Florida 
University of Texas at El Paso 
University of Toronto (Rotman) 
University of Western Ontario 
Washington State University 
Wilfrid Laurier University
#### AD HOC Reviewer (partial list)
Academy of Management Journal 
Canadian Journal of Administrative Science. 
Canadian Journal of Behavioral Science 
Developmental Psychology 
Human Relations 
Journal of Applied Psychology 
Journal of Occupational and Organizational Psychology 
Journal of Occupational Health Psychology 
Journal of Organizational Behavior 
Leadership and Organizational Development Journal 
Leadership Quarterly 
South African Journal of Psychology 
Stress and Health 
Work and Stress
#### Editorial Activities
**Guest Editor:** _Journal of Occupational Health Psychology_ (2016 - ).
**Editor:** _Journal of Occupational Health Psychology_ (2000-2005)
**Co-Editor:** Sage Publications Series “_Advanced Topics in Organizational Behavior_” (19962003)
**Consulting Editor:** _Journal of Organizational Behavior_ (1997-2000)
**Editorial Boards:**
* _Leadership Quarterly (2017- ) Journal of Applied Psychology_, (2002-2007)
* _Journal of Occupational Health Psychology,_ (1996-1999)
* _Leadership and Organizational Development Journal_ (2003-2011)
* _Stress Medicine_ (2003-2007).

# [Marketing Evolution: A Fireside Chat with Ken Wong | Smith Business Insight](https://smith.queensu.ca/insight/content/Marketing-Evolution-A-Fireside-Chat-with-Ken-Wong.php) 
 _https://smith.queensu.ca/insight/content/Marketing-Evolution-A-Fireside-Chat-with-Ken-Wong.php_

**Ken Wong is one of Canada’s** undisputed marketing and brand experts. As a member of the faculty at Smith School of Business, he has taught many of today’s marketing leaders and is frequently quoted by the media on marketing and brand strategy issues. 
Marketing and branding have never been as tough as they are today. Consumers have high expectations, and many companies simply aren’t meeting their needs. Technology, the economy and a fragmented media landscape are making it even harder for brands to connect. 
Join Smith Business Insight for an intimate and interactive fireside chat with Ken Wong. This webinar looks at the challenges and opportunities that marketers face in today’s fast-paced, technology-driven world and explore what consumers care about most now (and why). You’ll come away with practical insights that can be applied to your own work. 
**Participants  learn:** 
* What’s motivating consumers and how the economy has changed their relationship with brands
* What issues brands must overcome to win with customers
* How artificial intelligence may disrupt the marketing world
* The role of social impact and purpose for companies today
* Timeless advice every marketer can use
* As Ken nears retirement, lessons from his 40-plus-year career in marketing 
This webinar was recorded live on Thursday, March 30.
## Session Participants
### Ken Wong
Associate Professor of Marketing
Ken Wong is an associate professor of marketing at Smith School of Business, where he has held both teaching and administrative positions. He was the principal architect of the first full-time degree program in Canada to operate completely outside of government subsidy: a distinction that earned him the cover of _Canadian Business_ in April 1994. Ken also sits on several advisory boards and boards of directors. He was named an inductee into the Canadian Marketing Hall of Legends and, in 1998, won the _Financial Post_’s Leaders in Management Education award, a lifetime achievement award for his work in undergraduate, MBA and executive development programs. Ken’s work has been featured in numerous media and he frequently is asked to address global audiences on business strategy, branding, pricing and retail practice.
### Meredith Dault
Moderator
Meredith Dault is a journalist and communications specialist. She has worked as a reporter and producer with CBC Radio in Ottawa and Halifax, and her work has been published widely, including in the Ottawa Citizen, the Globe and Mail, Kingston Life and online at Reader’s Digest Canada. She is the manager, content and media production in the Centre for Content Development at Smith School of Business and is the regular host of Smith Business Insight webinars.
Tags:

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=202403) 
 _https://smith.queensu.ca/news_blog/archive.php?a=202403_

The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.

# [Eddy Ng](https://smith.queensu.ca/faculty_and_research/faculty_list/ng-eddy.php) 
 _https://smith.queensu.ca/faculty_and_research/faculty_list/ng-eddy.php_

Professor & Smith Professor of Equity & Inclusion
## Overview
Eddy Ng is the Smith Professor of Equity & Inclusion in Business at Queen’s University. He was previously the James & Elizabeth Freeman Professor of Management and DEI Faculty Fellow at Bucknell University, and the F.C. Manning Chair in Economics and Business at Dalhousie University.
[Download Full CV _​_](https://smith.queensu.ca/faculty_and_research/faculty_list/CVs/Eddy-Ng-CV.pdf) [Download Image _​_](https://smith.queensu.ca/faculty_and_research/faculty_list/download_images/ng-eddy.jpg)
### Academic Area
* Organizational Behaviour
### Interest Topics
* Diversity Management
* Human Resources Management
## Faculty Details
### Profile
#### Full Bio
Eddy Ng is Professor of Organizational Behaviour and the Smith Professor of Equity & Inclusion in Business at Queen’s University. He was previously the James & Elizabeth Freeman Professor of Management and DEI Faculty Fellow at Bucknell University, and the F.C. Manning Chair in Economics and Business at Dalhousie University.
His research focuses on managing diversity for organizational competitiveness, the future of work, and managing across generations. His work has been funded by the Social Sciences and Humanities Research Council of Canada grants. He has edited and published 8 books and more than 100 peer-reviewed journal articles and book chapters. According to a recent Stanford study, he is identified in the top 2% of highly cited scientists in Economics & Business.
He has been featured in popular media outlets in Canada and the U.S. such as the CBC, CTV, Global News, the Globe and Mail, the Financial Post, ABC News, BBC Worklife, CBS News, NPR, Vox, and the Wall Street Journal. He is the Editor-in-Chief of Equality, Diversity and Inclusion and Co-Editor of Personnel Review. He is Past Chair of the Diversity, Equity and Inclusion (previously Gender and Diversity in Organizations) division of the Academy of Management.
Prior to academia, he worked for the TD Bank Financial Group in Commercial Banking, Domestic Planning, Corporate Audit, and Group Human Resources at the headoffice in Toronto.
#### Academic Degrees
**PhD** 
McMaster University
**MBA** 
Simon Fraser University
**BCom** 
The University of British Columbia
#### Academic Experience
**Smith School of Business, Queen's University** 
Professor 
Smith Professorship in Equity and Inclusion in Business 
Associate Professor
**Bucknell University** 
James and Elizabeth Professor of Management 
DEI Faculty Fellow
**Dalhousie University 
**Professor 
F.C. Manning Chair in Economics and Business 
Associate Professor
### Publications
#### **Journal Articles**
Ng, E.S., Sears, G.J., & Arnold, K.A. (forthcoming). Who does diversity better? The role of servant leaders in promoting diversity management across public and private sector organizations. _Public Administration Quarterly._
Ng, E.S., Shen, W., Lewis, A., & Bonner, R. (forthcoming). Critical issues facing Asian Americans and Pacific Islanders (AAPIs) in organizations and society. _American Behavioral Scientist_.
King, E., Hebl, M., Corrington, A., Holmes IV, O., Lindsay, A.P., Madera, J., Martinez, L., Ng, E.S., Nittrouer, C., Sabat, I., Sawyer, K., & Thoroughgood, C. (2024). Understanding and addressing the health implications of anti-LGBTQ+ legislation. _Occupational Health Science, 8_(1), 1-41.
Ayoobzadeh, M., Schweitzer, L., Lyons, S., & Ng, E.S. (2024). A tale of two generations: A time-lag study of career expectations. _Personnel Review._
Case, P., Wood, J., & Ng, E. (2024). Introducing the Journal of Tropical Futures: Sustainable business, governance and development. _Journal of Tropical Futures, 1_(1), 3-11.
Stanton, P., & Ng, E.S. (2023). Job crafting: Relevance to human resource management. _Personnel Review, 52_(8) 1953-1956.
Mohammadi, Z., Bhati, A., & Ng, E.S. (2023). Twenty years of workplace diversity research in hospitality and tourism: A bibliometric analysis. _Equality, Diversity and Inclusion: An International Journal, 42_(4) 551-571.
Ng, E.S. & McGowan, R.A. (2023). Breaking the glass ceiling: Women of the second wave feminist movement in Canada. _Canadian Journal of Administrative Sciences,_ _40(2), 173-187._
Ng, E.S., Rajendren, D. & Waheduzzaman, W., (2023). Promoting workplace inclusion and self-efficacy among skilled migrant workers in Australia. _International Journal of Manpower,_ _44(2) 267-282_
Ng, E.S., & Stanton, P. (2023). The Great Resignation: Managing People in a Post COVID-19 Pandemic World. Personnel Review, 52(1), 401-407
Ng, E.S., Posch, A., Köllen, T., Kraiczy, N., & Thom, N. (forthcoming). Do “one size” employment policies fit all young workers? Heterogeneity in work attribute preferences among the Millennial generation. _Business Research Quarterly_
Dahms, S., Kingkaew, S., & Ng, E.S. (2022). The effects of top management team national diversity and institutional uncertainty on subsidiary CSR focus and performance. _Journal of Business Ethics, 173(3)_ 699-715.
Metz, I., Stamper, C, & Ng, E.S. (2022). Feeling included and excluded in organizations: The role of human and social capital. _Journal of Business Research, 142_, 122-137.
Ng, E.S., & Stanton, P. (2022). Editorial: Personnel Review after 50: The next chapter. _Personnel Review, 51_(1) 2-3_._
Saba, T., Ozbilgin, M., Ng, E. and Cachat-Rosset, G. (2021), Ineffectiveness of diversity management: lack of knowledge, lack of interest or resistance?, _Equality, Diversity and Inclusion, 40_(7), 765-769.
Ng, E.S., Sears, G.J., & Arnold, K. (2021). Exploring the Influence of CEO and Chief Diversity Officers’ Relational Demography on Organizational Diversity Management: An Identity-based Perspective. _Management Decision, 59_(11), 2583-2605.
Ng, E.S., & Sears, G.J., & Bakkaloglu, M. (2021). White and minority employee reactions to perceived discrimination at work: Evidence of White fragility?  _International Journal of Manpower,_ 42(4), 661-682. 
Bates, K., & Ng, E.S. (2021) Whiteness in academia, time to listen, and moving beyond White fragility. _Equality, Diversity and Inclusion,_ 40(1), 1-7. 
Ng, E.S. & Lam, A. (2020). Black lives matter: On the denial of systemic racism, White liberals, and polite racism. _Equality, Diversity and Inclusion,_ 37(1), 729-739. 
Ng, E.S., & Sears. G. (2020). Walking the talk on diversity: CEO beliefs, moral values, and the implementation of workplace diversity practices. _Journal of Business Ethics,_ 164(3), 437-450.
Ng, E.S., & McGinnis Johnson, J. (2020).  Game of loans: The relationship between education debt and making a career choice in the public, private, and nonprofit sectors. _Nonprofit and Voluntary Sector Quarterly,_ 49(2), 292-315.
Sobral, F., Ng, E.S., Castanheira, F., Chambel, M.J., & Koene, B. (2020). Dealing with temporariness: Generational effects on temporary agency workers’ employment relations. _Personnel Review,_ 49(2), 406-424.
Thompson, C., Kuah, A., Foong, R, & Ng, E. (2020). The Development of Emotional Intelligence, Self-Efficacy and Locus of Control in MBA Students. _Human Resource Development Quarterly,_ 31(1), 113-131.
Rajendran, D., Ng, E.S., Sears, G., & Ayub, N. (2020). Determinants of migrant career success: A study of recent skilled migrants in Australia.  _International Migration,_ 58(2), 30-51.
Ng, E.S., & Stamper, C. (2018).  A Trump presidency and the prospect for equality and diversity. _Equality, Diversity and Inclusion,_ 37(1), 2-13.
Rajani, N., Ng, E.S., & Groutsis, D. (2018).  From India to Canada: An autoethnographic account of an international student’s transition to a self-initiated expatriate. _Canadian Ethnic Studies_ 50(1), 129-148.
Alhejji, H., Ng, E.S., Garavan, T., & Carbery, R. (2018).  The impact of formal and informal distance on gender equality approaches:  The case of a British MNC in Saudi Arabia.  _Thunderbird International Business Review,_ 60(2), 147-159.
Ng, E.S., & Rumens, N. (2017).  Diversity and inclusion for LGBT workers: Current issues and new horizons for research.  _Canadian Journal of Administrative Sciences,_ 34(2), 109-120.
Ng, E.S. & Sears, G.J. (2017).  The glass ceiling in context: The influence of CEO gender, recruitment practices, and firm internationalization on the representation of women in management.  _Human Resource Management Journal,_ 27(1), 133-151.
Ng, E. S. (2017). Editorial statement regarding recent policies from the Trump Administration.  _Equality, Diversity and Inclusion,_ 36(2), 110.
Kuron, L., Schweitzer, L., Lyons, S., & Ng, E.S. (2016).  Career profiles in the “new career:” Evidence of their prevalence and correlates.  _Career Development International,_ 21(4), 355-377.
Ng, E.S., Gossett, C.W., Chinyoka, S., & Obasi, I. (2016).  Public vs. private sector management: An exploratory study of career choice among graduate management students in Botswana.  _Personnel Review,_ 45(6), 1367-1385.
Ng, E.S.W., Gossett, C.W., & Winter, R. (2016).  Millennials and public service renewal: Introduction on Millennials and public service motivation.  _Public Administration Quarterly,_ 40(3), 1-16.
Klarsfeld, A., Ng, E.S., Booysen, L.A.E., Castro-Christiansen, L., & Kuvaas, B. (2016).  Comparative equality and diversity: Main findings and research gaps.  _Cross-cultural and Strategic Management,_ 23(3), 1-19.
McGowan, R.A., & Ng, E.S.W. (2016).  Employment equity in Canada: Making sense of employee discourses of misunderstanding, resistance, and support.  _Canadian Public Administration,_ 59(2), 310-329.
Burke, R.J., Ng, E.S., & Wolpin, J. (2016).  Effects of hospital restructuring and downsizing on nursing staff: The role of union support.  _Journal of Health Management,_ 18(3). 1-16.
Kwok, C., Bates, K., & Ng, E.S. (2016).  Managing and sustaining an aging nursing workforce: Identifying opportunities and best practices in collective agreements.  _Journal of Nursing Management,_ 24(4), 500-511.
McGinnis Johnson, J., & Ng, E.S. (2016). Money talks or millennials walk: The effect of competitive compensation on millennial worker nonprofit sector-switching behaviors.  _Review of Public Personnel Administration,_ 36(3), 283-305_._
Ng. E.S. (2016).  Editorial: Introducing a new editorial team.  _Equality, Diversity and Inclusion,_ 35(7/8), 394-396. 
Ng, E.S., & Sears, G.J. (2015).  Toward representative bureaucracy: Predicting public service attraction among underrepresented groups in Canada.  _Review of Public Personnel Administration,_ 35(4), 367-385.
Kuron, L., Lyons, S., Schweitzer, L., & Ng, E.S. (2015).  Millennials’ work values: Differences across the school to work transition.  _Personnel Review,_ 44(6), 991-1009.
Lyons, S., Schweitzer, L., & Ng, E.S. (2015).  Resilience in the modern career.  _Career Development International,_ 20(4) 363-383.
Wazed, S., & Ng, E.S. (2015).  College recruiting using social media: How to increase applicant reach and reduce college recruiting costs.  _Strategic HR Review,_ 14(4) 1325-141.
Ng, E.S., & Bloemraad, I. (2015).  A SWOT analysis of multiculturalism in Canada, Europe, Mauritius, and South Korea.  _American Behavioral Scientist,_ 59(6), 619-636. 
Ng, E.S. & Metz, I. (2015).  Multiculturalism as a strategy for national competitiveness: The case for Canada and Australia.  _Journal of Business Ethics,_ 128(2), 253-266_._ 
Lyons, S., Schweitzer, L., & Ng, E.S. (2015).  How have careers changed?  An investigation of changing career patterns across four generations.  _Journal of Managerial Psychology,_ 30(1), 8-21.
Burke, R.J., Ng, E.S., & Wolpin, J. (2015).  Economic austerity and healthcare restructuring: Correlates and consequences of nursing staff job insecurity.  _International Journal of Human Resource Management,_ 26(5), 640-656
Schweitzer, L., Lyons, S., Kuron, K.J., & Ng, E.S.W. (2014).  The gender gap in pre-career salary expectations: A test of five explanations.  _Career Development International,_ 19(4), 404-425.
Ng, E.S. (2014).  Relative deprivation, self-interest and social justice: Why I do research on in-equality.  _Equality, Diversity and Inclusion,_ 33(5), 429-441.
Lyons, S.T., Ng, E.S., Schweitzer, L. (2014). Changing demographics and the shifting nature of careers: Implications for research and human resource development.  _Human Resource Development Review,_ 13(2), 180-205.
Sur, S. & Ng, E.S. (2014).  Extending theory on job stress: The interaction between the ‘other 3’ and ‘big 5’ personality traits on job stress.  _Human Resource Development Review,_ 13(1), 79-101.
Ng, E.S.W., & Law, A. (2014).  Keeping up! Older workers’ adaptation in the workplace after age 55.  _Canadian Journal on Aging,_ 33(1), 1-14. 
Lewis, G.B., & Ng, E.S. (2013).  Sexual orientation, work values, pay, and preference for public and nonprofit employment: Evidence from Canadian postsecondary students.  _Canadian Public Administration,_ 56(4), 541-562.
Ng, E.S.W., & Gossett, C.W. (2013).  Career choice in Canadian public service: An exploration of fit with the millennial generation.  _Public Personnel Management,_ 42(3), 337-358.
Konrad, A.M., Moore, M.E., Ng, E.S.W., Doherty, A.J., & Breward, K. (2013).  Temporary work, underemployment, and workplace accommodations:  Relationship to well-being for workers with disabilities.  _British Journal of Management,_ 24(3), 367-382.
Klarsfeld, A., Ng, E.S., & Tatli, A. (2012).  Social regulation and diversity management: A Comparative study of France, Canada and the UK.  _European Journal of Industrial Relations,_ 18(4), 309-327.
Hyman, R., Klarsfeld, A., Ng, E., & Haq, R. (2012).  Introduction: Social regulation of diversity and equality.  _European Journal of Industrial Relations,_ 18(4), 279-292.
Ng, E.S.W., Schweitzer, L., & Lyons, S.T. (2012).   Anticipated discrimination and career choice among stigmatized individuals: A study of early career lesbian, gay, bisexual, and transgendered (LGBT) job seekers.  _Review of Public Personnel Administration,_ 32(4), 332-352_._
Lyons, S.T., Schweitzer, L., Ng, E.S.W., & Kuron, L. (2012).  Comparing apples to apples: A qualitative investigation of career mobility patterns across four generations. _Career Development International,_ 17(4), 333-357.
Konrad, A.M., Moore, M.E., Doherty, A.J., Ng, E.S.W., & Breward, K. (2012). Vocational status and perceived well-being of workers with disabilities.  _Equality, Diversity and Inclusion,_ 31(2), 100-123.
* Reprinted in: _Sport Management: Critical Concepts in Sports Studies_, Taylor & Francis (July 2013).
Ng, E.S., & Sears, G.J. (2012).  CEO leadership styles and the adoption of organizational diversity practices: Moderating effects of social values and age.  _Journal of Business Ethics,_ 105(1), 41-52.
Moore, M.E., Konrad, A.M., Yang, Y., Ng, E.S.W., & Doherty, A.J. (2011).  The vocational wellbeing of workers with childhood onset disability: Life satisfaction and perceived workplace discrimination.  _Journal of Vocational Behavior,_ 79(3), 681-698.
Ng, E.S.W., & Wyrick, C.R. (2011).  Motivational bases for managing diversity: A model of leadership commitment.  _Human Resource Management Review,_ 21(4), 368-376.
Schweitzer, L., Ng, E., Lyons, S., & Kuron, L. (2011).  Exploring the career pipeline: Gender differences in pre-career expectations.  _Relations Industrielles/Industrial Relations,_ 66(3), 374-396.
Burke, R.J., Ng, E.S.W., & Wolpin, J. (2011).  Nursing staff work experiences, work outcomes and psychological well-being in difficult times: Implications for improving nursing staff quality of work life and hospital functioning.  _Journal of Industrial Relations and Human Resources,_ 13(2), 9-22.
Burke, R.J., Ng, E.S.W., & Wolpin, J. (2011).  Hospital restructuring and downsizing: Effects on nursing staff well-being and perceived hospital functioning.  _Europe’s Journal of Psychology,_ 7(1), 81-98.
Burke, R.J., Ng, E.S.W., & Wolpin, J. (2011).   Hospital restructuring and downsizing processes and nurses satisfactions well-being and perceived hospital functioning: What seems to be helpful? _A Journal of Indian Society of Management Development & Research,_ 1(1), 30-42.
Burke, R.J., Ng, E.S.W., & Wolpin, J. (February, 2011).  Hospital downsizing: A breach of trust?  _Effective Executive,_ 38-42.
Ng, E.S.W. (2011).  Book review: Cross-Cultural Management: Essential Concepts (2E) by D.C. Thomas. _Cross-cultural Management: An International Journal,_ 18(1), 122-124.
Ng, E.S.W., & Burke, R.J. (2010).  A comparison of the legislated employment equity program, federal contractors program and financial post 500 firms.  _Canadian Journal of Administrative Sciences,_ 27(3), 224-235.
Ng, E.S.W., & Sears, G.J. (2010).  The effect of adverse impact in selection practices on organizational diversity outcomes: A field study.  _International Journal of Human Resource Management,_ 21(9), 1454-1471.
Ng, E.S., & Burke, R.J. (2010).  Predictors of business students’ attitudes toward sustainable business practices.  _Journal of Business Ethics,_ 95(4), 603-615.
Ng, E.S.W., Schweitzer, L., & Lyons, S.T. (2010).  New generation, great expectations: A field study of the millennial generation in Canada.  _Journal of Business and Psychology,_ 25(2), 281-292.
Ng, E.S.W., & Sears, G.J. (2010).  What women and ethnic minorities want: Work values and labour market confidence.  A self-determination perspective.  _International Journal of Human Resource Management,_ 21(5), 677-699.
Burke, R.J., Ng, E.S.W., & Fiksenbaum, L. (2009).  Virtues, work satisfactions, and psychological well-being among nurses.  _International Journal of Workplace Health Management, 2_(3), 202-219.
Ng, E.S.W., Burke, R.J., & Fiksenbaum, L. (2008).  Career choice in management: Findings from U.S. MBA students.  _Career Development International_, _13_(4), 346-361.
Ng, E.S.W. (2008).  Why organizations choose to manage diversity?  Toward a leadership-based theoretical framework.  _Human Resource Development Review, 7_(1), 58-78.
Ng, E.S., & Wiesner, W.H. (2007).  Are men always picked over women?  The effects of employment equity directives on selection decisions.  _Journal of Business Ethics, 76_(2), 177-187.
Burke, R.J., & Ng, E.S.W. (2007).  Workaholic behaviours: Do colleagues agree? _International Journal of Stress Management, 14_(3), 312-320.
Ng, E.S.W. (2007).  Reaching new heights: Findings from the summit of Banff on the progress of gender and diversity in Canada.  _Equal Opportunities International, 26_(1), 71-76.
Ng, E.S.W., & Burke, R.J. (2006).  The next generation at work: Business students’ views, values and job search strategy.  _Education and Training, 48_(7), 478-492. 
* Slightly revised version reprinted as: Burke, R.J., & Ng, E.S.W. (2007).  Business students’ views on jobs, careers and the job search process: Implications for employers and universities.  In A. Malach-Pines & M. Özbilgin (Eds.), _Career Choice in Entrepreneurship and Management: A Research Companion_. Cheltenham: Edward Elgar.
Burke, R.J., & Ng, E. (2006).  The changing nature of work and organizations: Implications for human resource management.  _Human Resource Management Review, 16_(2), 86-94.
Ng, E.S.W., & Burke, R.J. (2005).  Person-organization fit and the war for talent: Does diversity management make a difference?  _International Journal of Human Resource Management, 16_(7), 1195-1210.
Ng, E.S.W., & Burke, R.J. (2004).  Cultural values as predictors of attitudes towards equality and diversity: A Canadian experience.  _Women in Management Review, 19_(6), 317-324.
Ng, E.S.W., & Tung, R.L. (1998).  Ethnocultural diversity and organizational effectiveness: A field study.  _International Journal of Human Resource Management, 9_(6), 980-995.  
#### **Book**
Ng, E.S., Lyons, S.T., & Schweitzer, L. (2018).  _Generational Career Shifts: How Veterans, Boomers, Gen Xers, and Millennials View Work_.  Bingley: Emerald.
#### **Edited Books**
Ng, E.S., Ramsay, J., Wood, J., & Thirumaran, K. (Eds.) (2023). _Elgar Companion to Managing People Across the Asia-Pacific. An Organizational Psychology Approach._ Cheltenham: Edward Elgar
Klarsfeld, A., Knappert, L., Nornau, A., Ng, E.S., & Ngunjiri, F. (Eds.) (2022). _International Handbook on New Frontiers of Diversity and Equality at Work Inclusion._ Cheltenham: Edward Elgar
Ng, E.S., Stamper, C.L., & Klarsfeld, A. (Eds.) (2021). _Handbook on Diversity and Equity Indices: A Research Compendium._ Cheltenham: Edward Elgar
Klarsfeld, A., Ng, E., Booysen, L.A.E., Castro-Christiansen, L., & Kuvaas, B. (Eds.) (2016).  _Research Handbook of International and Comparative Perspectives on Diversity Management._  Cheltenham: Edward Elgar.
Klarsfeld, A., Booysen, L., Ng, E., Roper, I., & Tatli A. (Eds.) (2014). _International Handbook on Diversity Management at Work: Second Edition Country Perspectives on Diversity and Equal Treatment_. Cheltenham: Edward Elgar.
Ng, E.S.W., Lyons, S.T., & Schweitzer, L. (Eds.) (2012). _Managing the New Workforce: International Perspectives on the Millennial Generation._ Cheltenham: Edward Elgar.
#### **Book Chapters**
Ng., E.S. (2023). Not all white supremacists wear robes and hoods. In E. King, M. Hebl, & Q. Roberson (Eds.), _Perspectives on Race in Organizations._ Charlotte, NC: IAP
Tsang, D., Barzantny, C., & Ng, E.S. (2023). Age of perfection: An integrated perspective of employee longevity advantages in the global aerospace industry. In T. Melaku, A. Beeman, & C. Winkler (Eds.). _Handbook on Workplace Diversity and Stratification._ Rowman & Littlefield.
Lam, A., & Ng, E.S. Multiculturalism Policy Index (2021).  In E. Ng, A. Klarsfeld, and C. Stamper (Eds.) _Handbook on Diversity and Inclusion Indices: A Research Compendium_. Edward Elgar
Lam, A. & Ng, E.S. (2021). Representative bureaucracy in Canada: Multiculturalism in the public service.  In H. Sullivan and H. Dickinson (Eds.), _The Palgrave Handbook of the Public Servant._  McMillan Palgrave.
Lam, A. & Ng, E.S. (2020).  Progress in Affirmative Action: How backlash is holding us back. In E. King, M. Hebl, & Q. Roberson (Eds.), _Research on Social Issues in Management_.  Charlotte, NC: IAP
Ng, E.S., & French, E. (2018).  Are we there yet? - Advancing women in Canada and Australia: Similar goals, different policies.  In M. Reimer (Ed.), _Women and Careers: Transnational Studies in Public Policy and Employment Equity._  Taylor & Francis.
Ng, E.S., & Klarsfeld, A. (2018).  Comparative and multi-country research in equality, diversity, and inclusion.  In R. Bendl, L. Booysen, & J. Pringle (Eds.).  _Handbook of Research Methods on Diversity Management, Equality and Inclusion at Work._  Edward Elgar.
McGinnis Johnson, J., Piatek, J., & Ng, E.S. (2017).  Managing generational differences in nonprofit organizations.  In J. Sowa (Ed.), _The Nonprofit Human Resource Management Handbook: From Theory to Practice._  Blackwell
Ng, E.S., Lyons, S., & Schweitzer, L. (2017).  Millennials in Canada: Young workers in a challenging labour market.  In E. Parry and J. McCarthy (Eds.), _Handbook on Age Diversity and Work_. Palgrave-Macmillan.
Ng, E.S. & Lillevik, W. (2017).  Intercultural communication in the world of business.  In L. Chen (Ed.), _Handbook of Communication Science_. Berlin: Mouton de Gruyter
Lyons, S.T., Schweitzer, L., & Ng, E. (2016).  Generational differences in work values: Evidence from Canada.  In M. Shrabi (Ed.), Generational differences in work values and work ethic: An international perspective, Commack, NY: Nova Science Publishers.
Ng, E.S., & Parry, E. (2016).  Multigenerational research in human resource management.  _Research in Personnel and Human Resource Management, 33_, 1-41. Routledge
Metz, I., Ng, E.S., Nkomo, S., Cornellius, N., & Hoobler, J.  (2016). A comparative review of multiculturalism in Australia, Canada, South Africa, the UK, and the US.  In A. Klarsfeld, E. Ng, L. Booysen, L. Castro-Christensen, B. Kuvaas, & E. Ng (Eds.), _Research Handbook of International and Comparative Perspectives on Diversity Management._  Cheltenham: Edward Elgar.
Ng, E.S. & Stephenson, J. (2015).  Individuals, teams, and organizational benefits of diversity: An evidence-based approach.  In R. Bendl, I. Bleijenberg, E. Hentonnen, & A. Mills (Eds.), _The Oxford Handbook of Diversity in Organizations_.  Oxford
Ng, E.S.W., & McGinnis-Johnson, J. (2015).  Millennials: Who are they, how are they different, and why should we care?  In R.J. Burke, C. Cooper and A. Antoniou (Eds.), _The Multigenerational Workforce: Challenges and Opportunities for Organisations_.  Cheltenham: Edward Elgar
Ng, E.S., Haq, R., & Tremblay, D.G. (2014). A review of two decades of Employment Equity in Canada: Progress and propositions.  In A. Klarsfeld, L. Booysen, G. Combs, E. Ng, I. Roper, & A. Tatli (Eds.), _International Handbook on Diversity Management at Work: Second Edition Country Perspectives on Diversity and Equal Treatment_.  Cheltenham: Edward Elgar.
Lyons, S., Ng, E.S., & Schweitzer, L. (2014). Launching a career: Inter-generational differences in the early career stage.  In E. Parry (Ed.), _Generational Diversity at Work: New Research Perspectives._ Palgrave Macmillan.
Groutsis, D., Ng, E.S., & Ozturk, M. (2014). Cross-cultural management and diversity management intersections – lessons for attracting and retaining international assignees.  In M. Özbilgin, D. Groutsis, & W. Harvey (Eds.), _International Human Resource Management_.  Cambridge University Press.
Ng, E.S., & Barker, J.R. (2014). Managing diversity through effective communication.  In V.D. Miller & M.E. Gordon (Eds.), _Meeting the Challenges of Human Resource Management: A Communication Perspective_. London, UK: Routlege.
Lyons, S.T., Ng, E.S.W., & Schweitzer, L.  (2012). Generational career shift: Millennials and the changing nature of careers in Canada.  In E. Ng, S. Lyons, & L. Schweitzer (Eds.), Managing the New Workforce: International Perspectives on the Millennial Generation.  Cheltenham: Edward Elgar.
Haq, R., & Ng, E.S.W. (2010).  Employment equity and workplace diversity in Canada.  In A. Klarsfeld (Ed.), _International Handbook on Diversity Management at Work: Country Perspectives on Diversity and Equal Treatment_.  Cheltenhem: Edward Elgar.
Gossett, C.W., & Ng, E.S.W. (2008).  Domestic partnership benefits.  In C.G. Reddick & J.D. Coggburn (Eds.), _Handbook of Employee Benefits and Administration_.  Boca Raton, FL: CRC Press/Taylor & Francis.
Ng, E.S.W. (2001).  Human resource planning for international assignments: Leveraging Canada’s bicultural workforce.  In _Human Resources Management in Canada_, 20599-20604.  Toronto: Carswell.
### Teaching
#### Graduate Studies
**PhD Supervision**
* Brandon Legacy (in progress)
**MSc Supervision**
* Brandon Legacy (2023)
* Jessie Kim (2022)
**Committee Member**
* Michaela Scanlon (PhD in progress) – Queen’s University
* Shengwen Li (PhD in progress) – Queen’s University
* Julie Lalande (PhD in progress) – Dalhousie University
**External Examination (Doctoral Dissertations)**
* Alanood Khalifa AlKaabi – Abu Dhabi University
* Angel Myeza – University of Cape Town
* Ying Zhou – University of Cape Town
* Juliana Mutum – Deakin University
* Cara-Lynn Scheuer – Saint Mary’s University
* Gordana Abramovic – Norwegian Business School
#### Visiting Position
Professor, James Cook University, Singapore Campus, 2018 - Present
### Presentations
#### **Invited Presentations (Selected)**
* Dalhousie University - _[2019 Spring Convocation Address](https://www.youtube.com/watch?v=vTjjy03MB0k)_
* Herriot Watt University
* James Cook University - _[JCU 50 Professorial Lecture](https://www.jcu.edu.sg/news/releases/packing-a-professorial-punch-for-jcus-50th-anniversary)_
* Melbourne Business School
* Memorial University
* Monash University
* Queen Mary, University of London
* RMIT University
* Tilburg University
* Toronto Metropolitan University (Diversity Institute)
* Toulouse Business School
* University of Cape Town
* University of Malaya
* University of Otago
* University of Stirling
* University of Sydney
* WU Vienna University of Economics and Business
* Association to Advance Collegiate Schools of Business (AACSB)
* Canadian Institutes of Health Research (CIHR)
* Canadian Mortgage and Housing Corporation (CMHC)
* Department of National Defense
* Engineers Nova Scotia
* National Research Council of Canada
* Ontario Chamber of Commerce
* Private Foundation
* Public Policy Forum
* Public Service Commission of Nova Scotia
### Awards
#### **Awards and Honours**
MED Global Forum Best Symposium Award, Academy of Management (2023)
Conference Best Paper, 16th Equality, Diversity and Inclusion Conference, London, UK (2023) – _declined_
Top 2% of highly cited scientists in Economics and Business (2022, 2020)
Nominated for “That’s Interesting” Paper Award, Academy of International Business, 2022
Honorable Mention, PNP Best Journal Article, Academy of Management, 2021
President’s Diversity, Equity & Inclusion Award (Faculty), $500, 2021
University of Bath (CBOS)’s ＃ThinklistAmplify – list of influential scholars on social media around issues of responsible business, 2020
Stream Best Paper, 12th Equality, Diversity and Inclusion Conference, Rotterdam, 2019
Gender, Diversity and Indigeneity Best Paper Award, Australian and New Zealand Academy of Management, AUD $500, 2018
Faculty of Management Research Star Award, $1,000, 2018
Nominated Emerald Best International Symposium Award, Academy of Management, 2017
Emerald Outstanding Paper Award, Journal of Managerial Psychology, 2016
Faculty of Management Research Star Award, $1,000, 2015
Emerald Literati Highly Commended Award, Career Development International, 2015
HCM Best Paper Award, Administrative Sciences Association of Canada, 2015
Elwood F. Holton, III Research Excellence Award, Academy of Human Resource Development, USD $1,000, 2015
HR Best Paper Award, Administrative Sciences Association of Canada, 2014
Emerald Literati Highly Commended Award, Career Development International, 2013
Emerald Literati Highly Commended Award, Equality, Diversity and Inclusion, 2013
HR Best Paper Award, Administrative Sciences Association of Canada, 2013
Faculty of Management Teaching Excellence Award, $10,000, 2013
Best Stream Paper Award, 5th Equality, Diversity and Inclusion Conference, 2012
Nominated Best Applied Paper, Careers Division, Academy of Management, 2012
RSB Tenured Researcher of the Year Award, $1,000, 2011-2012
GDO Best Paper Award, Administrative Sciences Association of Canada, 2010
GDO Best Paper Award, Administrative Sciences Association of Canada, 2009
Best International Symposium Award, Academy of Management, 2008
GDO Honourable Mention Paper, Administrative Sciences Association of Canada, 2008
Emerald Literati Highly Commended Award, Education and Training, 2007
Finalist, Human Resources and Skills Development Canada (HRSDC/IAHRR) Best Dissertation Award, 2006
Dr. Robert C. Joyner Doctoral Publication Prize, $1,000, 2001
#### Grants & Funding
SSHRC Insight Grant (Co-P.I. with G. Sears, D. Gulanowski, and Y. Han), $173,311, 2022-2026
SSHRC Insight Development Grant (Co-P.I. with D. Gulanowski and G. Sears), $57,603, 2022-2024
SSHRC Partnership Grant (Co-Applicant with W. Cukier), $2,446,979, 2020-2026
L’OBVIA (International Observatory on the Societal Impacts of Artificial Intelligence and Digital Technology) (Collaborator with T. Saba), $150,000, 2020-2023
Lazaridis Institute Research Seed Grant (Co-P.I. with R. McGowan), $10,000, 2017
SSHRC Insight Grant (P.I. with G. Sears and K. Arnold), $123,060, 2016-2019 (extended)
SSHRC Strategic Research Grant (Co-P.I. with S. Lyons and L. Schweitzer), $158,400, 2008-2011
Canadian Studies Research Grant (Co-P.I. with M. Moore, A. Doherty, A. Konrad), USD $3,959, 2008-2009
### Service
#### Professional Service
**External**
* Proctor, Mensa Canada, 2021-Present
* Board Member, Pride at Work Canada, 2021-2022
* Chair WG 5, International Organization for Standardization/International Electrotechnical Commission (ISO/IEC) Joint Strategic Advisory Group (JSAG) on Gender and Gender Responsive Standards, 2020-
* Expert Panelist, Global Diversity and Inclusion Benchmarking (GDIB), Center for Global Inclusion, 2020-
* Consultation (Input Interview for diversity platform) for national leadership candidate, Conservative Party of Canada, 2020
* CCIP Exam Committee, Canadian Centre for Diversity and Inclusion (CCDI), 2017
* Judge, 2017 National HR Awards, Technology and Innovation Category, 2017
* Key Informant (Input Interview), Evaluation of Employment Equity Programs, Employment and Social Development Canada (ESDC), 2017
* Board Member, Mensa Canada Society, 2017-2019
* Panelist at Canada’s Fundamental Science Review Panel, 2016
* UN Global Compact Canada Network Working Group on Long-termism, 2014-2019
* Academic Observer, UN Committee of Experts in Public Administration, NY, 2013
* Atlantic Advisory Board, Ballet Jörgen Canada, 2012-2019
* Local Secretary, Halifax-Dartmouth, Mensa Canada, 2012-2017
**Professional Associations**
* Division Chair Elect, GDO Division, Academy of Management, 2019-
* Scientific Committee, Equality, Diversity and Inclusion Conference, 2012-
* Executive Committee, GDO Division, Academy of Management, 2016-2019
* Treasurer, Academy of International Business, Canada Chapter, 2016-2019
* Chair, Diversity & Inclusion Theme Committee (D&ITC), Academy of Management, 2012-2015
* Chair, GDO Division, Administrative Sciences Association of Canada, 2005-2008
**Journals**
* Co-Editor, Personnel Review, 2022-
* Series Editor, Palgrave Studies in Equity, Diversity, Inclusion and Indigenization, 2022-
* Editor-in-Chief, Equality, Diversity and Inclusion, 2016-
* Associate Editor, Personnel Review, 2013-2021
* Editor-in-Chief, Equality, Diversity and Inclusion, 2016-
* Book Review Editor, Equality, Diversity and Inclusion, 2012-2016
* Editorial Board, Palgrave Studies in Leadership and Followership (Book Series), 2017-
* Editorial Advisory Board, Gender in Management, 2016-
* Editorial Board, Zeitschrift für Personalforschung, 2016-
* Editorial Review Board, Cross-cultural and Strategic Management, 2015-
* Editorial Advisory Board, Employee Relations, 2013-
* Editorial Board, Public Personnel Management, 2013-
* Editorial Board, Management Communication Quarterly, 2010-
#### University Service
**Queen’s University**
* General Research Ethics Board (GREB)
* EDII Committee
**Bucknell University**
* Bucknell Futures (Discussion Group)
* Chair, Freeman College of Management DEI Committee
* Committee on Academic Freedom and Tenure (CAFT)
* MLK Week Committee
* Advisory Board, Bucknell Global Ambassador Program (GAP)
* Advisory Board, Center for the Study of Race, Ethnicity and Gender (CSREG)
* Faculty Liaison, Global and Off Campus Education
* Facilitator, Transforming Community Initiatives (TCI) Community Dialogues
* Faculty Advisor, American Mental Wellness Association Club of Bucknell

# [Home office solution wins 2022 Kinnear New Venture Competition](https://smith.queensu.ca/news_blog/2022/2022_Home_office_solution_wins_2022_Kinnear_New_Venture_Competition.php) 
 _https://smith.queensu.ca/news_blog/2022/2022_Home_office_solution_wins_2022_Kinnear_New_Venture_Competition.php_

Nikola Cugalj, Comm’22, founder of EcoPod, and a design rendering of the company's four-season backyard studio.
**Kingston, Ont. –** A Smith Commerce student’s space solution for the remote workforce has won this year’s [Paul and Tom Kinnear New Venture Competition](https://smith.queensu.ca/centres/ceisi/events/kinnear/index.php), hosted by the Centre for Business Venturing (CBV) at Smith.
Nikola Cugalj, Comm’22, has received $10,000 to develop his business, [EcoPod](https://www.myecopod.ca/), which designs and builds four-season backyard studios that can be used as home offices, workout spaces, music studios and more. The idea was born out of the course Comm 405 and developed into a minimum viable product before the first model was sold. EcoPod already has approximately 10 orders in its pipeline.
“We will use the money to create new and beautiful designs, market our product and brand, and invest in our e-commerce capabilities,” Cugalj says. The Ottawa-based company currently offers three customizable models, and another two are coming soon.
Since its creation in 2008, the Kinnear New Venture Competition has supported 18 Smith undergraduates and their entrepreneurial ventures. These funds are critical at the early stage of business and increase the odds of success.
“I am always humbled and motivated by the talent of the entrepreneurs coming out of the Smith Commerce program,” says JP Shearer, associate director for the CBV.  “I am grateful to Paul and Tom for their dedicated support, and I look forward to continuing to coach these ventures in the future.” 
The other three finalists were Calin Ranger, Comm’22, founder of Chaordinem Consulting; Abby Brewer, Comm’24, founder of Sew Brew; and Jay Lee, Comm’22, co-founder of Pally. Students who did not receive funding were offered invaluable feedback and mentoring from the judges.
On the panel of judges to determine this year’s winner were Mark Balovnev, BCom’19, co-founder and vice-president of operations, [Educhain](https://educhain.io/) (acquired); Adrien Bettio, BCom’17, co-founder of swim and activewear brand [437](https://shop437.com/) (former winner of the Kinnear New Venture Competition); Kelly Thomson, BCom’16, co-founder of reusable e-commerce packaging company [QUIL](https://shopquil.com/); and Arnon Vered, AMBA’09, entrepreneur, investor and management consultant at Vered Management Services.
**About the CBV**
The [Centre for Entrepreneurship, Innovation & Social Impact](https://smith.queensu.ca/centres/ceisi/index.php) ('Centre for Business Venturing' – at publication) at Smith School of Business is committed to being the leading and definitive source of knowledge and expertise in the creation, leadership and management of new ventures. Its purpose is to support research that will enable an understanding of the key success factors for entrepreneurial ventures, and translate and make this information available to the new venture community for long-term sustainability and growth, and to afford students the opportunity to gain invaluable business venturing experience.

# [Helping the next generation](https://smith.queensu.ca/invest/impact-of-giving/chip-mccrimmon.php) 
 _https://smith.queensu.ca/invest/impact-of-giving/chip-mccrimmon.php_

As an entrepreneur, **Chipewyan McCrimmon, MMIE’19,** wants to make the world a better place. His first venture, HeroHub, is an online platform that connects individuals wishing to donate their time with local non-profits and charities. The idea for the company came about a few years ago when Chip was looking to volunteer. But he found little information online about which charities in his community needed help.
His newest venture, Falc0n-X, aims to help landfills reduce their pollution with technology that captures, separates and purifies greenhouse gas emissions. Landfills are responsible for 20 per cent of Canada’s methane emissions, Chip points out. “So it’s a big problem we’re looking to solve.”
Growing up, Chip didn’t intend to become an entrepreneur. A Treaty 8 band member of the Deninu K’ue First Nation in the Northwest Territories, he grew up in Saskatchewan, hunting, fishing and trapping in the bush, and playing lacrosse. He played lacrosse in high school and at university.
But eventually he found himself drawn to business. Wishing to develop HeroHub as a social enterprise, he decided that he needed additional skills and expertise. So he enrolled in the Master of Management Innovation & Entrepreneurship program at Smith. “It changed my life,” he says now. “Everything I learned in the program, I have applied to my businesses.”
As a student, Chip received support from Smith. In the MMIE program, he was the recipient of the **Catherine Bell & Kent Brown Awakened Company Award**. Established by **Catherine Bell, EMBA’02,** and Kent Brown, the award is meant to advance entrepreneurship in society. Chip also got support through pitch competitions at Queen’s.
Now, as a graduate, Chip is looking to give back. He’s one of a number of entrepreneur-alumni to sign up for the [Smith Founders’ Pledge.](https://smith.queensu.ca/centres/ceisi/founders-pledge/index.php)
Launched in 2018, the pledge is a way for alumni who have launched businesses to support the next generation by making a financial commitment to Smith once their business takes off or they’ve made a successful exit. “I love creating a business and seeing it grow,” says Chip. “And I want to do my part to support future Smith students to do the same.”

# [Our Insight Topics | Smith Business Insight](https://smith.queensu.ca/insight/tag.php?tid=Equity) 
 _https://smith.queensu.ca/insight/tag.php?tid=Equity_

 Smith Business Insight - Our Insight Topics 
[Skip to main content](#main-content)
Smith  
* [About](#)
 
 [Smith Home](/index.php)[Profile](/about/index.php)[News](/news_blog/index.php)[The Dean](/about/dean.php)[Strategic Plan](/about/strategic-plan.php)[Equity, Diversity, Inclusion & Indigenization](/about/EDII/index.php)[Learning Environment](/about/learning_environment.php)[Partnerships](/about/partners/index.php) [Services](/about/services.php) [SmithStore _​_](http://smithqueens.com/smithstore) [Queen's University _​_](https://queensu.ca)
 
* [Learning](#)
 
 [Explore Our Programs](/academic_programs/index.php)[Undergraduate Programs](/academic_programs/undergraduate.php) [MBA Programs](/mba_programs/index.php) [Graduate Programs](/grad_studies/index.php) [Executive Education](/executiveeducation/index.php)[Certificates](/academic_programs/certificates.php)[International](/international/index.php)[SmithEdge](/smithedge/index.php)[Academic Integrity](/about/academic_integrity/index.php)
 
* [Insights & Research](#)
 
 [Smith Business Insight](/insight/index.php) [Research](/research/index.php) [Publications](/about/publications.php) [Centres](/centres/index.php)
 
* [Faculty](#)
 
 [Meet Our Faculty](/faculty_and_research/faculty.php) [Join Our Ranks](/faculty_and_research/Join_Our_Ranks.php)
 
* [Alumni & Giving](#)
 
 [Give to Smith](https://smith.queensu.ca/invest/) [Alumni](/alumni/index.php)
 
* [Recruit & Engage](#)
 
 [Recruiting](/recruiting/index.php) [Partnerships](/about/partners/index.php) [Work with Students](/engage/index.php) [Smith Business Consulting](/centres/business-consulting/index.php)
 
Fresh ideas from [Smith School of Business](/index.php)
* [Topics](#)
 
 ### Categories
 
 * [Leadership](/insight/sections.php?sid=Leadership)
 * [Teams](/insight/sections.php?sid=Teams)
 * [Diversity](/insight/sections.php?sid=Diversity)
 * [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
 * [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
 * [Social Impact](/insight/sections.php?sid=Social%20Impact)
 * [Marketing](/insight/sections.php?sid=Marketing)
 * [Strategy](/insight/sections.php?sid=Strategy)
 * [Finance](/insight/sections.php?sid=Finance)
 
 ### Collections
 
 * [Our Emotions at Work](/insight/collection/Our-Emotions-at-Work.php)
 * [Speaking of Economics](/insight/collection/Speaking-of-Economics.php)
 * [The Age of Corporate Purpose](/insight/collection/the-age-of-corporate-purpose.php)
 * [How To Make Hybrid Work](/insight/collection/how-to-make-hybrid-work.php)
 * [All Collections](/insight/collections.php)
 
 ### Subscribe to Our Newsletter
 
 Cutting-edge research and expert advice delivered straight to your inbox.
 
 [Subscribe](/insight/newsletter.php)
 
* [Webinars](/insight/webinars.php)
* [Podcast](/insight/podcast/index.php)
* [Videos](/insight/video.php)
* [About](/insight/about.php)
Search
# Equity
## [Why Is the Public Sector a DEI Laggard?](/insight/content/Why-Is-the-Public-Sector-a-DEI-Laggard.php)
Servant leaders are champions of inclusion. But they also face institutional barriers in the public service
## [How to Be an Equity, Diversity, Inclusion and Indigenization Leader](/insight/content/How-to-Be-an-Equity-Diversity-Inclusion-and-Indigenization-Leader.php)
CEOs play a critical role in ensuring that EDII initiatives are taken seriously. Discover why HR policies and mandatory training can fall short in efforts to increase inclusion within organizations.
## [Inclusion in the Post-Pandemic World](/insight/content/Future-of-Work-Inclusion.php)
Now is the time for organizations to take meaningful action on inclusive workforces and address systemic racism in business
[Load More](#)
## Editor’s Picks
1. [The New Rules of Public Speaking](/insight/content/The-New-Rules-of-Public-Speaking.php)
2. [The Untapped Potential of Customer Loyalty Plans](/insight/content/The-Untapped-Potential-of-Customer-Loyalty-Plans.php)
3. [How to Build Trusted Brands](/insight/content/How-to-Build-Trusted-Brands.php)
4. [How Catfish Effects Drive Stock Market Reform](/insight/content/How-Catfish-Effects-Drive-Stock-Market-Reform.php)
[Topics](#nav-menu-topics)
* [Leadership](/insight/sections.php?sid=Leadership)
* [Teams](/insight/sections.php?sid=Teams)
* [Diversity](/insight/sections.php?sid=Diversity)
* [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
* [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
* [Social Impact](/insight/sections.php?sid=Social%20Impact)
* [Marketing](/insight/sections.php?sid=Marketing)
* [Strategy](/insight/sections.php?sid=Strategy)
* [Finance](/insight/sections.php?sid=Finance)
[Collections](/insight/collections.php)
[Webinars](/insight/webinars.php)
[Podcast](/insight/podcast/index.php)
[Videos](/insight/video.php)
[About](/insight/about.php)
## Kingston
Goodes Hall 
Queen's University 
Kingston, Ontario 
Canada K7L 3N6
[1.877.533.2330](tel:+18775332330)
## Toronto
Simcoe Place 
200 Front Street West 
30th Floor
[416.365.7141](tel:+14163657141)
## Smith Programs
* [Undergraduate Programs](/academic_programs/undergraduate.php)
* [MBA Programs](/mba_programs/index.php)
* [Graduate Programs](/grad_studies/index.php)
* [Executive Education](/executiveeducation/index.php)
## Directories
* [Contact Us](/about/contact.php)
* [Smith Centres](/centres/index.php)
* [Smith Services](/about/services.php)
## Connect with Smith
* [Facebook](https://www.facebook.com/smithbusiness)
* [Instagram](https://www.instagram.com/smithbusiness/)
* [Twitter X](https://twitter.com/smithbusiness)
* [Linkedin](https://www.linkedin.com/company/smith-school-of-business-at-queen's-university)
* [WeChat](https://mp.weixin.qq.com/s/SoosIZFmLD0D01aSGJzgLw)
The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.
* [Give to Smith](/invest/ "Give to Smith")
* [Careers](/about/careers/ "Careers at Smith")
* [Program Portals](/academic_programs/student-portals.php "Program Portals")
* [Privacy](http://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy")
© Smith School of Business

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=201908) 
 _https://smith.queensu.ca/news_blog/archive.php?a=201908_

[## Scotiabank Centre for Customer Analytics at Smith School of Business celebrates success
](https://smith.queensu.ca/news_blog/2019/2019_Scotiabank_Centre_Success.php)
August 21, 2019
Kingston, Ont. – Established with an initial gift of $2.2 million from Scotiabank, the SCCA has seen a number of successes since its start, including research advances in the areas of pricing, revenue management, loyalty programs, adaptable database management systems, analytics and decision making, and ethics and AI. In July, Scotiabank reaffirmed its commitment to the centre’s mission and success with $2 million in additional funding, supporting the centre through to 2025.
[## Remembering Kristian Palda
](https://smith.queensu.ca/news_blog/2019/2019_Remembering_Kristian_Palda.php)
August 7, 2019
Kingston, Ont. – From fleeing communism to winning Queen’s University’s highest award for research excellence, Smith Professor Emeritus Kristian Palda, BCom’56, lived a storied life. A revered professor and prolific researcher, Palda passed away peacefully at home in Kingston on July 26, surrounded by family. He was 91.

# [StartUps | Smith Magazine](https://smith.queensu.ca/magazine/startups-index.php?c=Consumer%20Products) 
 _https://smith.queensu.ca/magazine/startups-index.php?c=Consumer%20Products_

In third-year Commerce, Hyla Nayeri and Adrien Bettio both went on exchange to Europe. There, they loved exploring out-of-the-way beaches.
We distributes and retail electric bikes & scooters that require no insurance, licence or parking fees.
Beekeeper's Naturals produces sustainable all-natural superfoods from the bee hive.
A women’s lingerie and swimwear store specializing in perfectly fitted foundation garments and swimwear. 
**My company,** Carmody, is a Canadian luxury statement knitwear brand for women.
Innovative products and solutions that increase the activity levels of busy people both at work and at home.
The Good Hood Club is a charitable loungewear company that is committed to championing the fight against childhood cancer by donating 50 per cent of our profits to the Pediatric Oncology Group of Ontario (POGO).
**My company,** Ioffe Biotechnologies, was created to optimize human health and performance.
**My company,** Iris Technologies, is a Canadian health-care technology company.
Lloyd & Co. Bespoke Tailoring offers custom-made suits and shirts for both men and women.
LowestRates.ca showcases rates from Canada’s leading financial institutions and allows Canadians to compare offers and find the best financial solution for their unique needs.
A stand-alone accessory for single-colour 3-D printers that enables them to print multiple colours.

# [Smith Dare to Dream supports four new ventures with impact](https://smith.queensu.ca/news_blog/2024/2024-Dare-to-Dream-Winners.php) 
 _https://smith.queensu.ca/news_blog/2024/2024-Dare-to-Dream-Winners.php_

**Kingston, Ont.** – Four soon-to-be graduates of Smith School of Business have secured funding through the [Centre for Entrepreneurship, Innovation & Social Impact](https://smith.queensu.ca/centres/ceisi/index.php) (CEISI) to help them realize their entrepreneurial dreams.
Samuel Bakiika, MMA’24; Waqar Qadir, MMA’24; Iuliana Calin, MMIE’24; and Ali Zayden, MMIE’24; have each received up to $15,000 and access to critical resources through the centre’s donor-funded Dare to Dream program.
“Each of the recipients this year has taken the bold step to start a venture that solves a problem and creates impact in their chosen market,” says CEISI Associate Director JP Shearer.
The new ventures led by these aspiring entrepreneurs are:
* **CoHome Canada (Samuel Bakiika) 
 **A comprehensive home co-ownership solution to the housing affordability crisis that uses advanced AI technology to match buyers and provide access to legal and financial support. 
 **Donor: Dany Battat, BCom’78, and the late Gia Steffensen, BCom’78**
* **EndoBio AI (Waqar Qadir) 
 **An AI solution that helps mitigate high costs and complexity within the agriculture sector, harnessing the power of genomics and multiomics datasets to unlock novel insights and drive efficiency. 
 **Donor: CIBC**
* **MaraAI (Iuliana Calin) 
 **An early detection dyslexia screening solution that leverages digital assessments to streamline evaluation, psychologist referral and individual education plan development and provide personalized learning plans for students.  
 **Donor: RSL Foundation**
* [**Drivista**](https://drivisa.com/) **(Ali Zayden)**A marketplace connecting new drivers with licensed driving instructors. The app allows driving students and their parents to choose their preferred time and instructor and arrange convenient pickup and drop-off locations. 
 **Donor: Sinkinson Family Dare to Dream Award**
The recipients will not only benefit from critical funding but will also get access to bookable workspace, coaching and mentorship through CEISI and the wider Queen’s University network. Combined, these resources will enable them to focus on moving their new ventures from late-stage ideation to early-stage startup, or from side hustle to full-time business.
“The mission is to create change, and each one of these Dare to Dream recipients has demonstrated perseverance to overcome barriers toward this goal,” Shearer says.
## About Dare to Dream
Dare to Dream is an annual program at Smith that is designed to enable entrepreneurs to launch their new ventures. Many students create startups while in their program, yet upon graduation they often have to put their entrepreneurial dreams aside to take full-time jobs. Dare to Dream gives Smith graduates the opportunity to bring their business to fruition by providing them with funding, resources and access to the invaluable Queen’s network of contacts.

# [Dare to Dream: 2023 winners announced, plus a new award](https://smith.queensu.ca/news_blog/2023/Dare-to-Dream-2023-winners-announced-plus-a-new-award.php) 
 _https://smith.queensu.ca/news_blog/2023/Dare-to-Dream-2023-winners-announced-plus-a-new-award.php_

**Kingston, Ont.** – Five startups led by Smith School of Business students have received a boost in funding from the Dare to Dream program. Two Master of Management Innovation & Entrepreneurship students, as well as students from Smith’s Master of Financial Innovation & Technology, Full-time MBA and Master of Management Analytics programs, were awarded a total of $70,000, along with access to critical resources for the development of their businesses.
This year’s winners and their businesses are: 
* [**Active Learning**](https://activelearn.ca/), $15,000 award 
 A tutoring centre creating a mobile and virtual educational escape room that prepares kids for the future through collaboration, ideation, leadership, empathy and innovation at school and at home. 
 **Founder:** Leila Seyidova, MMIE’23 
 **Donor:** Valerie Mann (BCom'86) 
* **Carbon Trace**, $10,000 award 
 An AI-focused SaaS solution that helps businesses optimize carbon emissions using advanced machine learning techniques to bring efficiency to the supply chain. 
 **Founder:** Lisa Anchalia, MBA’23 
 **Donors:** Dany Battat (BCom'78) and the late Gia Steffensen (BCom'78)  
* [**Good Weather**](https://shopgoodweather.com/), $15,000 award 
 A Black-owned sneaker boutique in Toronto that offers a diverse selection of streetwear and vintage clothing. 
 **Founder:** Malaika Thompson, MMA’24 
 **Donor:** RLS Foundation 
* **Pulse Financial**, $15,000 award 
 An AI "CFO companion" that helps businesses make the best decisions while teaching corporate finance and cash management. 
 **Founder:** Nick Ponari, MFIT’23 
 **Donor:** CIBC 
* [**SnapSmile**](https://www.snapsmile.ai/), $15,000 award 
 An app that helps dentists stay engaged with their patients' oral care journey by delivering personalized content, the ability to schedule appointments and access to oral health records. 
 **Founder:** Kartik Balasundaram, MMIE’23 
 **Donor:** The Sinkinson Family Dare to Dream Award
The Sinkinson Family Dare to Dream Award is a new addition to the annual program that encourages and supports new graduates in their entrepreneurial pursuits. Prior Dare to Dream award recipients, David Sinkinson, MBA'13, Artsci’11, Chris Sinkinson, MBA’11**,** Comp’02, founders of AppArmor, wanted to pay it forward and help the next generation of student entrepreneurs.
Chris explains that despite being a small amount of money in the larger scheme of things, the $15,000 they received from Dare to Dream in 2013 and what it enabled them to do in growing their business was of significant importance.
“I didn’t imagine that in 10 years we were going to have the success that we had,” says Chris, looking back on the company’s remarkable growth.
For SnapSmile founder Kartik Balasundaram, the news of the award came just when it was needed. "The Dare to Dream program's support is going to help us get out of a stagnated position we were in due to our limited funding. We can use this funding to make a short-term hire to build out the newest version of our product to scale to thousands of dental clinics."
In addition to funding, recipients have access to space, coaching and mentorship through the donor-funded program that is run annually through [Centre for Entrepreneurship, Innovation & Social Impact](https://smith.queensu.ca/centres/ceisi/index.php).  
"The Smith Centre for Business Venturing (CBV) plays a critical role in fostering a vibrant entrepreneurial ecosystem, providing aspiring founders with the knowledge, skills and networks necessary to transform their ideas into successful ventures,” says JP Shearer, Associate Director of The Centre for Business Venturing at Smith. “By supporting entrepreneurship, CBV is not only helping individual entrepreneurs achieve their goals, but also contributing to the social and economic well-being of communities."

# [Our Top 10 Stories of 2024 | Smith Business Insight](https://smith.queensu.ca/insight/content/Top-stories-of-2024.php) 
 _https://smith.queensu.ca/insight/content/Top-stories-of-2024.php_

**In today’s world**, challenges are becoming more complex and how we tackle them—whether alone, as a team or as an organization—has never been more important.
As 2024 comes to a close, we’re taking a look back at some of Smith Business Insight’s top stories that have hopefully helped you lead, innovate and succeed in this topsy turvy world.
This year, we explored key strategies around making mentorship meaningful, working alongside AI assistants, setting tough goals and easing the burden on middle managers. We also examined some bold questions: Does doing less sometimes lead to more success? Is nature a hidden advantage for business? Are false beliefs holding your startup back?
As you revisit these stories, we hope they spark new ideas and provide inspiration to carry forward into the New Year.
Tags:

# [Smith alumni named to Top 40 Under 40](https://smith.queensu.ca/news_blog/2019/2019_Top_40_Under_40.php) 
 _https://smith.queensu.ca/news_blog/2019/2019_Top_40_Under_40.php_

Top left, clockwise: Michele Romanow, Sc’07, MBA’08; Mustafa Humayun, BCom’07; Kyle MacDonald, BCom’11, GDA’11; Jeff Gallant, BCom’11.
**Toronto, Ont. –** Four Smith alumni were recognized last week at an event celebrating young Canadian business leaders. The four are among Canada’s Top 40 Under 40 for 2019. They are:
****• Michele Romanow,**** Sc’07, ****MBA’08,**** a tech titan and serial entrepreneur who started five companies before her 33rd birthday. Michele is co-founder and president of Clearbanc, which gave entrepreneurs more than $150 million in funding this year. She previously co-founded SnapSaves, which was acquired by American tech giant, Groupon in 2014. She is also well known as one of the “Dragons” on the CBC show _Dragons’ Den_.
**• Mustafa Humayun, BCom’07,** a partner at Sagard Holdings and the portfolio manager of its private credit business. Prior to this role, he led the Canada Pension Plan Investment Board’s energy credit team in North America as well as its Latin American credit investment platform.  
**• Jeff Gallant, BCom’11** and **Kyle MacDonald, BCom’11, GDA’11,** the co-founders of Capitalize for Kids (“C4K”), an organization striving to make Canada’s mental health system for youth the most efficient in the world. The pair are also portfolio managers with Gallant MacDonald, a specialized family wealth practice at CIBC Private Wealth Management. 
[Canada’s Top 40 Under 40](https://www.canadastop40under40.com/) was founded in 1995 to identify outstanding young achievers in Canadian business. Honourees are selected by an advisory board of business executives. The 2019 Top 40 Under 40 Awards Gala was hosted Nov. 6 by Caldwell Partners and MNP at the Metro Toronto Convention Centre.

# [CEISI - Make the Pledge](https://smith.queensu.ca/centres/ceisi/founders-pledge/pledge.php) 
 _https://smith.queensu.ca/centres/ceisi/founders-pledge/pledge.php_

## Pledge Your Support
Complete this brief form to confirm your interest and we’ll be in touch.
First name
Last name
Email
Phone (optional)
Smith or Queen’s degree
Job title
Company
Sector/Industry
Can we share your name and company name on the Founders’ Pledgers page?
Yes
No
Would you like your Founders’ Pledge to be anonymous?
Yes
No
Would you like to receive information and event invitations from CEISI?
Yes
No
Sign up for our Smith Business Insight Newsletter to stay up to date on cutting-edge thought leadership from Smith faculty and industry experts.
Yes
No
Provide a photo
Please submit as JPG format. File size must be less than 4MB.
Your Smith Founders’ Pledge is a commitment to give in the future and is non-binding.

# [CEISI - Overview](https://smith.queensu.ca/centres/ceisi/events/innovation-hackathon/index.php) 
 _https://smith.queensu.ca/centres/ceisi/events/innovation-hackathon/index.php_

The Social Innovation Hackathon is an engaging immersion into the world of social innovation and its implications for using business as a catalyst for social change. Participants will have the opportunity to work in teams to create innovative solutions for social impact challenges that growing dynamic organizations are facing today.
Teams will begin by reviewing a challenge provided by the organization participating in the event. They will have the day of the Hackathon to engage with the problem and brainstorm potential solutions. Teams will then provide a pitch deck presentation and pitch to a team of judges detailing their unique ideas and resolutions.
Participation is offered in-person and virtual, including Q&A sessions and final presentations.
This is an excellent opportunity to develop entrepreneurial skills and sharpen critical thinking in the context of the UN Sustainable Development Goals (SDGs).

# [Our Insight Topics | Smith Business Insight](https://smith.queensu.ca/insight/tag.php?tid=consumer%20psychology) 
 _https://smith.queensu.ca/insight/tag.php?tid=consumer%20psychology_

 Smith Business Insight - Our Insight Topics 
[Skip to main content](#main-content)
Smith  
* [About](#)
 
 [Smith Home](/index.php)[Profile](/about/index.php)[News](/news_blog/index.php)[The Dean](/about/dean.php)[Strategic Plan](/about/strategic-plan.php)[Equity, Diversity, Inclusion & Indigenization](/about/EDII/index.php)[Learning Environment](/about/learning_environment.php)[Partnerships](/about/partners/index.php) [Services](/about/services.php) [SmithStore _​_](http://smithqueens.com/smithstore) [Queen's University _​_](https://queensu.ca)
 
* [Learning](#)
 
 [Explore Our Programs](/academic_programs/index.php)[Undergraduate Programs](/academic_programs/undergraduate.php) [MBA Programs](/mba_programs/index.php) [Graduate Programs](/grad_studies/index.php) [Executive Education](/executiveeducation/index.php)[Certificates](/academic_programs/certificates.php)[International](/international/index.php)[SmithEdge](/smithedge/index.php)[Academic Integrity](/about/academic_integrity/index.php)
 
* [Insights & Research](#)
 
 [Smith Business Insight](/insight/index.php) [Research](/research/index.php) [Publications](/about/publications.php) [Centres](/centres/index.php)
 
* [Faculty](#)
 
 [Meet Our Faculty](/faculty_and_research/faculty.php) [Join Our Ranks](/faculty_and_research/Join_Our_Ranks.php)
 
* [Alumni & Giving](#)
 
 [Give to Smith](https://smith.queensu.ca/invest/) [Alumni](/alumni/index.php)
 
* [Recruit & Engage](#)
 
 [Recruiting](/recruiting/index.php) [Partnerships](/about/partners/index.php) [Work with Students](/engage/index.php) [Smith Business Consulting](/centres/business-consulting/index.php)
 
Fresh ideas from [Smith School of Business](/index.php)
* [Topics](#)
 
 ### Categories
 
 * [Leadership](/insight/sections.php?sid=Leadership)
 * [Teams](/insight/sections.php?sid=Teams)
 * [Diversity](/insight/sections.php?sid=Diversity)
 * [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
 * [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
 * [Social Impact](/insight/sections.php?sid=Social%20Impact)
 * [Marketing](/insight/sections.php?sid=Marketing)
 * [Strategy](/insight/sections.php?sid=Strategy)
 * [Finance](/insight/sections.php?sid=Finance)
 
 ### Collections
 
 * [Our Emotions at Work](/insight/collection/Our-Emotions-at-Work.php)
 * [Speaking of Economics](/insight/collection/Speaking-of-Economics.php)
 * [The Age of Corporate Purpose](/insight/collection/the-age-of-corporate-purpose.php)
 * [How To Make Hybrid Work](/insight/collection/how-to-make-hybrid-work.php)
 * [All Collections](/insight/collections.php)
 
 ### Subscribe to Our Newsletter
 
 Cutting-edge research and expert advice delivered straight to your inbox.
 
 [Subscribe](/insight/newsletter.php)
 
* [Webinars](/insight/webinars.php)
* [Podcast](/insight/podcast/index.php)
* [Videos](/insight/video.php)
* [About](/insight/about.php)
Search
# consumer psychology
## [Why You Shouldn’t Put a Price on a Great Gift](/insight/content/Why-You-Shouldnt-Put-a-Price-on-a-Great-Gift.php)
Those expensive gifts you like to give may be sowing the seeds of suspicion
[Load More](#)
## Editor’s Picks
1. [The New Rules of Public Speaking](/insight/content/The-New-Rules-of-Public-Speaking.php)
2. [The Untapped Potential of Customer Loyalty Plans](/insight/content/The-Untapped-Potential-of-Customer-Loyalty-Plans.php)
3. [How to Build Trusted Brands](/insight/content/How-to-Build-Trusted-Brands.php)
4. [How Catfish Effects Drive Stock Market Reform](/insight/content/How-Catfish-Effects-Drive-Stock-Market-Reform.php)
[Topics](#nav-menu-topics)
* [Leadership](/insight/sections.php?sid=Leadership)
* [Teams](/insight/sections.php?sid=Teams)
* [Diversity](/insight/sections.php?sid=Diversity)
* [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
* [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
* [Social Impact](/insight/sections.php?sid=Social%20Impact)
* [Marketing](/insight/sections.php?sid=Marketing)
* [Strategy](/insight/sections.php?sid=Strategy)
* [Finance](/insight/sections.php?sid=Finance)
[Collections](/insight/collections.php)
[Webinars](/insight/webinars.php)
[Podcast](/insight/podcast/index.php)
[Videos](/insight/video.php)
[About](/insight/about.php)
## Kingston
Goodes Hall 
Queen's University 
Kingston, Ontario 
Canada K7L 3N6
[1.877.533.2330](tel:+18775332330)
## Toronto
Simcoe Place 
200 Front Street West 
30th Floor
[416.365.7141](tel:+14163657141)
## Smith Programs
* [Undergraduate Programs](/academic_programs/undergraduate.php)
* [MBA Programs](/mba_programs/index.php)
* [Graduate Programs](/grad_studies/index.php)
* [Executive Education](/executiveeducation/index.php)
## Directories
* [Contact Us](/about/contact.php)
* [Smith Centres](/centres/index.php)
* [Smith Services](/about/services.php)
## Connect with Smith
* [Facebook](https://www.facebook.com/smithbusiness)
* [Instagram](https://www.instagram.com/smithbusiness/)
* [Twitter X](https://twitter.com/smithbusiness)
* [Linkedin](https://www.linkedin.com/company/smith-school-of-business-at-queen's-university)
* [WeChat](https://mp.weixin.qq.com/s/SoosIZFmLD0D01aSGJzgLw)
The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.
* [Give to Smith](/invest/ "Give to Smith")
* [Careers](/about/careers/ "Careers at Smith")
* [Program Portals](/academic_programs/student-portals.php "Program Portals")
* [Privacy](http://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy")
© Smith School of Business

# [How Not to Love Your Ideas to Death | Smith Business Insight](https://smith.queensu.ca/insight/content/How-Not-to-Love-Your-Ideas-to-Death.php) 
 _https://smith.queensu.ca/insight/content/How-Not-to-Love-Your-Ideas-to-Death.php_

**You’re sitting in a brainstorming session** and have just come up with a fabulous idea for a new product. You immediately fall in love with it and know others will too.   
Unfortunately, when you share this novel idea with your colleagues, they only point out the negatives and poke holes in the idea. Maybe it’s too expensive, unrealistic or doesn’t fully address market needs. Before you know it, the idea you’ve fallen in love with has lost all its attraction.   
What do you do next: Abandon your novel idea or stick with it, convinced that others will finally see the light?  
It could come down to personality. According to one [recent study](https://www.sciencedirect.com/science/article/abs/pii/S0749597822000528), those who see themselves as different from others and defined by independent characteristics (such as “I am smart” or “I am creative”) are more likely to feel attached to their ideas and persist in the face of resistance. Those who define themselves by the groups they belong to or their personal relationships (such as “I am on a sports team” or “I am a parent”) are less likely to become attached to their ideas. 
But personality is not the whole story, says Salman Mufti, associate professor of management information systems at Smith School of Business. Mufti has worked extensively in decision-making at the managerial level and has experienced first-hand the ideation process within organizations. From his own experience (and regardless of personality type), he has found that you don’t have to give up on ideas you love in the face of doubt. But you must be willing to consider others’ opinions to refine them.  
This balancing act involves many factors, including being open to constructive feedback, as well as some self-awareness and a willingness to change your mind.   
## **Love at first sight**  
Mufti says it’s always important to feel passion for an early idea. When people are emotionally attached to their idea, they’re more driven to bring it to fruition.  
“There’s a concept called anchoring, which means we give more weight to the very first piece of information we see, read or get,” Mufti says. “In some ways, I suspect you’re anchoring yourself with your own first idea. This makes you become more attached to it.” However, he adds, our initial inspiration is often incomplete and doesn’t fully address the problem at hand. It may be a simplified version of a solution that needs development. 
Mufti has noticed throughout his career that certain types of people do not give up easily on their early ideas. Often, he says, these individuals have achieved past success with them.  
“Sometimes, that causes people to become a bit overconfident. They’ve had such a great track record, and therefore have that credibility,” he says. “These individuals might consider themselves to be experts, but experts can be wrong, and it happens all the time.” 
Team leaders play an important role in managing different personalities and their attitudes toward their early ideas. Before a brainstorming session even begins, team leaders must inform team members that they will be challenged on their ideas, and then establish appropriate norms.  
“The team needs to know the reason they will be challenged,” Mufti says. “That reason is to make sure they collectively come to a good, strong conclusion on what needs to be done. Leaders must lay down some groundwork upfront.”  
## **Keep emotions in check**  
It might not be easy, but Mufti says people also need to set expectations for themselves. They must first accept they are in an organizational brainstorming setting that involves an iterative process. As part of that process, colleagues are expected to voice their doubts and test the strength of an initial idea.  
“This is a pretty big mindset change for all of us because whenever we come up with something and share it with others, the natural wish is to get praise,” he says.   
While it might be difficult to not take feedback personally — especially when you’re emotionally invested in your early idea — Mufti says it is better for creators to change their mindsets and to seek out critiques. If someone is emotionally attached to their early idea, they should view constructive criticism as an important step to helping improve it.  
Mufti says this shift in thinking — to be aware of your thoughts when your idea is being criticized — comes with experience. It takes practice. “Maybe start with smaller ideas first, so you get used to the process,” he says. “It will help you get used to this way of thinking, and you can graduate towards bigger ideas.”  
Additionally, Mufti says that workers are often encouraged in a brainstorming setting to develop multiple ideas. This may help prevent them from clinging to a single initial inspiration that may not be viable. Individuals can share their initial idea, he says, but then perhaps offer up a few more ideas for the group to refine.  
“Once you figure out which idea is better than the other, then you can test it,” Mufti says. “To me, that process is more creative than coming up with one single brilliant idea in the beginning.”  
## **Power of team input**  
Once brainstormers shift their mindset, their teams can play an important role in helping them decide if they should stick with their early idea.  
It’s tough to play devil’s advocate on your own, Mufti says, and a team that has diverse thinking styles can help someone decide if an idea is worth pursuing. “We unconsciously look for information or reasoning that supports the idea we have in our head,” Mufti says. “We need to involve others and have them challenge it.”  
He adds that individuals can manage their emotions by considering the early idea as the beginning of its evolution — which has the potential to further develop with the help of others through refining, reasoning and testing.  
“I like to think that in most cases,” says Mufti,” it’s more about collective brilliance rather than individual brilliance.”  
Tags:

# [Smith School of Business - Year in Review - Advancing Business Studies](https://smith.queensu.ca/yearinreview/2018-2019/stories/business-studies.php) 
 _https://smith.queensu.ca/yearinreview/2018-2019/stories/business-studies.php_

## Leading in professional knowledge
In a climate-change world, how do investors deal with carbon risk? It’s an important question because carbon risk considerations are changing the way investment decisions are made and how businesses attract capital.
Smith PhD candidate Neal Willcott is investigating. “Until recently, carbon risk wasn’t even priced into most stocks, so the chances are that we could still be living in a bit of a carbon bubble.” In the years ahead, he says, investment strategies will change as investors incorporate carbon risk into their strategies. “This means businesses will have to adapt because investors are a key source of capital for them.”
Neal was immediately impressed by the research culture at Smith when he arrived last year to focus on sustainable finance research. “You have so many top people in their fields,” he says. “Everyone wants to help you succeed.” Neal is especially thrilled to learn from some of the best sustainable finance researchers anywhere, including his supervisor, Professor Sean Cleary. He hopes the work he and others are doing eventually helps advise policymakers on climate change.
Smith researchers are known for their expertise worldwide.
### Research impact
The research undertaken at Smith covers important areas of business today, including analytics, artificial intelligence, social impact, entrepreneurship, leadership, digital innovation, resilience and accounting. Business ethics, corporate governance, finance, management information systems, marketing, operations management, organizational behaviour and strategy are also key areas.
The work being done at Smith has lessons for organizations, too. For instance, recent research by Jean-Baptiste Litrico, associate professor of strategy and organization, examined whether non-profits can pursue both social gains and business revenue without sacrificing their mission. The answer: Yes. Indeed, non-profits that developed commercial activities were able to successfully integrate them into their social goals.
Another example: Pam Murphy, associate professor of accounting, has done extensive research into workplace fraud. Recently, though, she looked at how companies can keep employees honest. “It's often easier and cheaper to try to keep people honest than try to catch dishonesty,” she says.
### Grants and recognition
Smith researchers are known for their expertise worldwide. During the 2018-2019 year, 44 articles by faculty were published in academic journals, including 14 in the Financial Times’ 50 top-tier journals. Faculty also received a combined total of $758,595 in research grants, including those from the Social Sciences and Humanities Research Council and the Natural Sciences and Engineering Research Council of Canada.
A number of faculty also received accolades. For example, Tina Dacin, professor of organizational behaviour, received the Best Symposium Award from the Organization and Management Theory division of the Academy of Management. Accounting professor Steven Salterio received the Lifetime Notable Contribution Award in the American Accounting Association's Behavior and Organizations Section.
In March, Associate Professor Ryan Riordan received the Bank of Canada Governor’s Award. The research grant goes to academics who study areas that the bank deems important. He is using the grant to further his research in climate change and the use and misuse of technologies in banking and financial markets. “This award,” he says, “is confirmation that our research is important to the overall economy.”

# [Research Brief: Nasty Coaches and the Damage Done | Smith Business Insight](https://smith.queensu.ca/insight/content/research-brief-nasty-coaches-and-the-damage-done.php) 
 _https://smith.queensu.ca/insight/content/research-brief-nasty-coaches-and-the-damage-done.php_

**What Did the Study Look At?**
We hear stories about transformational leaders or coaches having positive effects on their followers or players long after people have moved on. The same goes for abusive leaders or coaches and the lasting scars they leave on those with whom they work.
Organizational researchers, however, focus almost exclusively on how leadership behaviours affect current followers. And sports psychology researchers offer limited insights on the ill effects of abusive leadership (defined as sustained forms of nonphysical hostility — ridicule, blame, verbal threats, rudeness among others — intended to make a subordinate feel guilty, upset, or inadequate).
This research team tackles both challenges. Based on the contention that leadership has sustained effects on followers even after the leader-follower relationship has ended, the researchers investigated the career-long effects of abusive leadership by professional basketball coaches on players’ aggression and task performance.
**How Was the Study Designed?**
Data were obtained from NBA players and coaches between the 2000/2001 and 2005/2006 seasons; the information was based on external rather than self-reported sources.
The study focused on 57 coaches who held positions in the NBA for at least one full season during the study period. Researchers conducted a comprehensive search for biographical information on each NBA coach from archival sources, with a focus on news articles that contained references to the coaches’ leadership behaviours. From these biographies, abusive leadership ratings were established based on a previously developed 15-item scale (for example, “ridicules me”, “blames me”, “is rude to me”).
Players were matched with the coach they had in each year. Technical fouls — generally unsportsmanlike conduct penalties — served as a proxy for players’ psychological aggression. Player task performance measures were derived from objective performance data routinely used within the industry for major personnel decisions. 
**What Did the Study Find?**
* Abusive leadership was consistently associated with increased psychological aggression (technical fouls) over the course of the players’ career. Specifically, abusive leadership experienced at some point within the six years of the study shifted the players’ trajectory of psychological aggression upward across their career. 
* Abusive leadership significantly predicted lower task performance across players’ careers (as measured by the player efficiency score).
* While athletes displayed a downward shift in task performance over time, the strength of this effect did not change. 
**What Do I Need to Know?**
Why is exposure to abusive leadership so important? The researchers point to evidence that exposure to negative relationships has consistently stronger effects than similar exposure to positive relationships. Consider that transformational leadership has been shown to cast a glow on followers five years down the road; the fallout from an abusive leader presumably would last much longer.
In a sports environment, abusive leadership is often tolerated and seen as a way to drive players to a higher level of achievement. When NBA coaches are fired, the researchers say, “the reasons are similar to those involved in the firing of senior executives in traditional organizations, namely correcting poor selection decisions, coaches losing the respect of their team or significant players, organizational politics, and coaches not achieving performance targets. In contrast, any kind of formal discipline or firing of coaches for abusive leadership is rare.”
The message for organizations is that the negative effects of coaches’ and leaders’ abusive supervision continues well into the future. Early intervention is crucial.
**Title**: _“__Scarred for the Rest of my Career? Career-Long Effects of Abusive Leadership on Professional Athlete Aggression and Task Performance”_
**Authors**: Erica L. Carleton (Smith School of Business; now at the University of Saskatchewan), Julian Barling (Smith School of Business), Amy M. Christie (Wilfrid Laurier University), Melissa Trivisonno (Smith School of Business), Kelsey Tulloch (Smith School of Business), and Mark R. Beauchamp (University of British Columbia) 
**Published**: [_Journal of Sport and Exercise Psychology_](http://journals.humankinetics.com/doi/abs/10.1123/jsep.2015-0333) (vol. 38, issue 4, 409-422)
_— Alan Morantz_
Tags:

# [Smith MBA ranked among Top 100 in the world](https://smith.queensu.ca/news_blog/2022/Smith-MBA-ranked-among-Top-100-in-the-world-by-Financial-Times.php) 
 _https://smith.queensu.ca/news_blog/2022/Smith-MBA-ranked-among-Top-100-in-the-world-by-Financial-Times.php_

 #1 in Canada for career services,according to FTKingston, Ont. – The Financial Times has ranked the full-time MBA at Smith School of Business in the top 100 in its annual ranking of global MBA programs.For the second consecutive year, Smith was No. 1 in the country for overall satisfaction with the program, as rated by alumni three years post-graduation. Smith was also the top-ranked Canadian school for career services, which includes career coaching, personal development and other support for students to build their profile and network.“A great MBA experience goes beyond the classroom – to networking, personal growth and an exceptional support system,” said Elspeth Murray, associate dean, MBA and masters programs. “With the best career outcomes in Canada, clearly we are succeeding in helping students achieve their goals.”Smith’s MBA class of 2021 saw 98 per cent of students with an accepted job offer within three months of graduation. Alumni secured jobs with leading organizations in financial services, consulting, consumer goods and technology.The Financial Times Global MBA ranking is based on four categories of criteria: career progress; diversity; research; and environmental, social and governance (ESG). Data is collected from a survey of schools and a survey of alumni three years after graduation.Four Canadian programs made the 2022 ranking. View the full FT 2022 Global MBA ranking.

# [CPIA - Overview](https://smith.queensu.ca/centres/cpia/index.php) 
 _https://smith.queensu.ca/centres/cpia/index.php_

## Stand Out in the 
Fast-Growing Field 
of Impact Analysis
## Online Learning at Your Own Pace. Complete in 6 Months.
**Next program starts January 2025.** Space is limited.
## Certificate in Professional Impact Analysis
It's not enough to pursue impact and hope for the best. Businesses, governments, and organizations must measure and report the broader environmental, social, and economic impacts of their operations, investments, and policies.
While it's well-understood how to assess and report financial returns, few understand how to report their social impacts with similar rigour and credibility.
Learn how with the Certificate in Professional Impact Analysis. Distinguish yourself in this fast-emerging and important discipline. Learn the best practices, tools, and methods to define, quantify, and report impact across the lifecycle of organizations, projects, or policies.
Designed for private and public sector leaders, managers, analysts, financial professionals, and consultants.
Three online modules support learning at your own pace. Plus a live, full-day, virtual hands-on session with classmates, coaches and faculty instructors at the end of each module.
> “As our customers’ demand increases for ‘green steel’ and support of net-zero building, we must apply robust evidence-based measures and procurement processes. As we dig deeper into the future of construction, it will be crucial to have quantitative evidence to ensure we are hitting sustainability targets for years to come. The Certificate in Professional Impact Analysis will provide a basis for rigorous procurement processes.”
**Steven Kuysten, MBA** 
Ontario Senior Sales Executive and Business Development 
Ocean Steel (a division of OSCO Construction Group)
[More industry perspectives](https://smith.queensu.ca/centres/cpia/program-details/industry.php)  
## Program Content
You will learn about:
* Impact measurement and definition
* Impact assessment
* Impact management and accounting
* Impact evaluation
* Impact communication and reporting
[Learn more](https://smith.queensu.ca/centres/cpia/program-details/modules.php)
## Key Features
### 3 Learning Modules Over 6 Months
Learn essentials, best practices, and key techniques across three learning modules: Impact Assessment, Impact Accounting, and Evaluating and Learning. Complete in 6 months.
[Program details](https://smith.queensu.ca/centres/cpia/program-details/modules.php)  
### Online Learning at Your Own Pace
Each learning module is completed in 6 weeks at your own pace. Rich and engaging content, case studies, and exercises from expert faculty and instructors. Accessible online 24/7.
[Program format](https://smith.queensu.ca/centres/cpia/program-details/schedule-fees.php)  
#### Live Capstone Sessions in Each Module
Join fellow students, faculty and instructors in a live, online session at the end of each learning module. Includes an individual assignment and assessment to confirm learning, and progress toward the certificate.
[Explore program](https://smith.queensu.ca/centres/cpia/program-details/modules.php)  
### Team-based Capstone Project
Work with classmates on real-life impact analysis projects from public sector organizations and private industry around the globe.
[Find out more](https://smith.queensu.ca/centres/cpia/program-details/modules.php)  
### Rigour & Credibility
Benefit from years of real-world experience and rigorous academic expertise underpinning the program’s content. Learn from distinguished Queen’s University faculty members from Smith School of Business and the Economics Department.
[Meet the faculty](https://smith.queensu.ca/centres/cpia/program-details/faculty.php)  
#### Differentiate with a Certificate
Prove your expertise with the Certificate in Professional Impact Analysis from Smith School of Business at Queen’s University and stand out among your peers.
[Discover](https://smith.queensu.ca/centres/cpia/program-details/modules.php)  
## Who should take this program?
This versatile, practical program provides you with the expertise to best define, assess, and communicate your organization’s impact.
Whether you’re identifying, designing, financing, implementing, upgrading, monitoring, or evaluating operations, investments, or policies, the Certificate in Professional Impact Analysis can improve your effectiveness.
This program is for:
* Leaders who want to do more good … and know they truly are
* Policy specialists and social sector leaders seeking to improve impact and accountability
* Advocates who want evidence to drive change
* Investment professionals looking beyond the financial bottom line
* Social impact investors assessing areas to improve portfolio performance
* Accountants wanting to add impact assessment to your practice
* Corporate communications professional who need to better report your organization’s impact
* Anyone working in areas related to ESG and sustainability efforts

# [Overview](https://smith.queensu.ca/yearinreview/2021-2022/index.php) 
 _https://smith.queensu.ca/yearinreview/2021-2022/index.php_

### A focus on EDII
Equity, diversity, inclusion and Indigenization (EDII) are crucial to the success of Smith School of Business as we move forward. Last year, Smith unveiled a new EDII Strategy and Action Plan, developed with input from school alumni, students, faculty and staff. Read up on some of the work we’ve done around EDII in the past year, from supporting students to offering career development and more.
[Read more about EDII](https://smith.queensu.ca/yearinreview/2021-2022/edii.php)

# [StartUps | Smith Magazine](https://smith.queensu.ca/magazine/startups-index.php?c=Construction) 
 _https://smith.queensu.ca/magazine/startups-index.php?c=Construction_

**© Copyright, Queen’s University** 
Smith Magazine is published twice annually by 
The Stephen J.R. Smith School of Business 
at Queen’s University.

# [FTMBA - Our MBA Suite | Smith School of Business](https://smith.queensu.ca/mba_programs/index.php) 
 _https://smith.queensu.ca/mba_programs/index.php_

## Four Unique Ways to Earn your MBA Degree
## Find the Program That's Right for you
[Take our Quiz](#)
## Full-time MBA
An MBA program unlike any other. The Full-time MBA from Smith School of Business takes a flexible and highly personalized approach that allows you to build the right program for your career goals. The team-based program structure is designed to develop exceptional leaders, valuable team members, and highly effective managers.
## Executive MBA – The National Program
Offered anywhere in Canada, the Executive MBA has numerous optional features that can be personalized around your individual strengths and aspirations. Designed for working managers and executives, this 16-month program starting in August enables you to earn your MBA while you continue to work.
## Executive MBA Americas - a Cornell-Queen's Partnership
The Executive MBA Americas program is the only program of its kind in the world. Graduates earn two MBA degrees from two premier business schools — Smith School of Business at Queen’s University and the Johnson School of Management at Cornell University in New York. The classroom experience is shared by participants from Canada, the USA and Latin America.
## Accelerated MBA for Business Graduates
Available in major cities across Canada, the Accelerated MBA for Business Graduates is designed specifically for people with an undergraduate degree in business (or equivalent) and a minimum of two years relevant work experience, this 12-month program starting in January enables you to earn your MBA while you continue to work.

# [StartUps | Smith Magazine](https://smith.queensu.ca/magazine/startups-index.php) 
 _https://smith.queensu.ca/magazine/startups-index.php_

When Hakeem Subair co-founded 1 Million Teachers with fellow MMIE’17 grad Rizma Butt (left), he had a big goal: to improve the quality of teachers in sub-Saharan Africa.
Creators of CompTrak, an end-to-end compensation-management software that empowers companies of all sizes.
In third-year Commerce, Hyla Nayeri and Adrien Bettio both went on exchange to Europe. There, they loved exploring out-of-the-way beaches.
An ad agency with no employees. Instead, we have curated a global network of freelance professionals.
We distributes and retail electric bikes & scooters that require no insurance, licence or parking fees.
We develop custom mobile apps that provide tools to foster community safety for educational institutions. 
Beekeeper's Naturals produces sustainable all-natural superfoods from the bee hive.
A women’s lingerie and swimwear store specializing in perfectly fitted foundation garments and swimwear. 
**My company,** Carmody, is a Canadian luxury statement knitwear brand for women.
Meal-kit delivery service making easy and affordable to make delicious and nutritious meals.
A customized Coleman® cooler, ideal for camping trips or cottage weekends that people can personalize with a favourite picture, text, and/or flag via an easy-to-use website.
We design, license and manufacture products intended to improve wasteful food packaging.

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?c=Announcements) 
 _https://smith.queensu.ca/news_blog/archive.php?c=Announcements_

[## Certificate in Professional Impact Analysis addresses industry need for thorough impact measurement
](https://smith.queensu.ca/news_blog/2024/2024-CPIA-Addresses-Industry-Need.php)
November 6, 2024
Kingston, Ont. – In an era where businesses and governments are increasingly held accountable for their environmental, social and economic impacts, the need for accurate assessment and reporting has never been more critical. Smith's Centre for Entrepreneurship, Innovation & Social Impact (CEISI) is offering the Certificate in Professional Impact Analysis (CPIA) to equip professionals with the tools and knowledge needed to measure and communicate their organization's impact effectively.
[## Financial Times releases 2024 EMBA Rankings
](https://smith.queensu.ca/news_blog/2024/2024-Financial-Times-releases-2024-EMBA-Rankings.php)
October 15, 2024
Kingston, Ont. – Smith School of Business’ two Executive MBA programs have been ranked among the top 75 EMBA programs in the world by the Financial Times (FT).
[## The lasting legacy of Mel Goodes
](https://smith.queensu.ca/news_blog/2024/2024-Smith-remembers-Mel-Goodes-lasting-legacy.php)
October 7, 2024
Kingston, Ont. – Philanthropist, pharmaceutical pioneer, and business leader Melvin Goodes, BCom’57, LLD’94, is being remembered for his lasting impact on Smith and Queen’s, and the students and researchers who benefited from his generosity. Mel, the former chief executive officer of Warner-Lambert (now Pfizer) and director of both the Alzheimer’s Drug Discovery Foundation (ADDF) and the Melvin R. Goodes Family Foundation, passed away on Sept. 30 at the age of 89.
[## Wanda Costen to step down as Dean of Smith School of Business
](https://smith.queensu.ca/news_blog/2024/2024-Wanda-Costen-Stepping-Down-as-Dean-at-Smith-Business.php)
August 29, 2024
Kingston, Ont. – Principal and Vice-Chancellor Patrick Deane announced today that Dean Wanda Costen is stepping down to end her term as Dean of Smith School of Business as of December 31, 2024, to take on the role of Provost and Vice-Principal Academic at Dalhousie University, effective January 1, 2025. Lynnette Purda will serve as Smith’s Interim Dean as of January 1, 2025, for an 18-month appointmen

# [Smith School of Business - Year in Review - Overview](https://smith.queensu.ca/yearinreview/2018-2019/index.php) 
 _https://smith.queensu.ca/yearinreview/2018-2019/index.php_

Goodes Hall, Queen's University 
Kingston, Ontario 
Canada K7L 3N6
[1.877.533.2330](tel:1.877.533.2330)
The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.
[Privacy](https://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy") © Smith School of Business

# [Dean's Innovation Fund](https://smith.queensu.ca/invest/investment_priorities/deans-innovation-fund.php) 
 _https://smith.queensu.ca/invest/investment_priorities/deans-innovation-fund.php_

The Dean’s Innovation Fund enables the dean to flexibly support the greatest emerging priority areas of Smith School of Business in a timely manner. Those areas include awards and scholarships to draw outstanding students; named professorship and chairs to attract and retain outstanding faculty; support of centres and institutes; improvement and sustainability initiatives; and capital projects. Established and supported by the generosity of our alumni and friends, the Dean's Innovation Fund helps to ensure Smith School of Business students have the resources they need to achieve their full potential through exceptional experiences both inside and outside of the classroom.
Support our students by [donating now](https://www.givetoqueens.ca/project/view/428).
## Funds
### Dean's Innovation Fund

# [CPIA - Information Sessions](https://smith.queensu.ca/centres/cpia/program-details/info-sessions.php) 
 _https://smith.queensu.ca/centres/cpia/program-details/info-sessions.php_

The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.

# [CEISI - General Inquiries](https://smith.queensu.ca/centres/ceisi/contact/index.php) 
 _https://smith.queensu.ca/centres/ceisi/contact/index.php_

## Contact Us
Please feel free to contact us with any questions or comments.
First name
Last name
Email
Phone (optional)
Message
All information gathered by Smith School of Business is protected under the [Student and Applicant Record Policy](https://www.queensu.ca/registrar/resources/policies/access-privacy) as set by The Office of the University Registrar at Queen's University. Learn more about the [collection, use and disclosure of personal information](http://www.queensu.ca/accessandprivacy/privacy/notice-collection) at Queen’s University.

# [Beyond the Glass Ceiling | Smith Business Insight](https://smith.queensu.ca/insight/content/Beyond-the-Glass-Ceiling.php) 
 _https://smith.queensu.ca/insight/content/Beyond-the-Glass-Ceiling.php_

The concept of the glass ceiling was first coined in 1978, but women still find it tough to break through. While the share of women in senior leadership roles is increasing, women still face unique obstacles and challenges to growing their careers. 
And yet, change is happening. As the world faces unprecedented challenges including conflict, climate change, and poverty, more women are stepping forward to create the kinds of societies they want to see, even against the odds. What will it take to empower more women to step into the kinds of leadership roles that will enable them to make an even greater impact? 
Watch this free 60-minute webinar on what it takes to become a leader today and how to get there. The webinar was recorded on International Women’s Day, March 8, 2023.
How can you overcome the barriers to success? What steps should you take in your career journey that will help put you on the path to leadership positions? Panelists Wanda Costen, dean of Smith School of Business, Jane Philpott, dean of the Faculty of Health Sciences at Queen’s University, and leadership consultant Kim Fulton offer their insights and inspire you with stories of hard-won successes moving up the ladder and beyond the glass ceiling. 
**You learn:**
* What women can do to promote their own career advancement
* Common obstacles that get in the way of career growth (and how to get past them)
* Why too many women hold themselves back from chasing their dreams
* How to find a mentor and work with allies who can help you succeed
* Advice for women just starting out in their careers
* How to be an ally for women on their path to success
**Who should attend:** 
Leaders and managers in all disciplines, aspiring leaders, problem-solvers, and anyone wanting to make a difference through leadership. 
Check out [Jane Philpott's inspirational playlist](https://open.spotify.com/playlist/0Npp0z2SFo15CFuewnGPpa?si=5c-fnsQ_SrOqNT5HhW7Qcg&nd=1) on Spotify.
## Session Participants
### Dr. Wanda Costen
Dean, Smith School of Business
As Dean of Smith School of Business, Dr. Wanda Costen brings a unique combination of experience in academia and private and public sector management. Her passionate belief that businesses can drive positive social impact has made her a catalyst for partnerships between academia, business and public organizations on diversity initiatives and training programs throughout her career. With a research interest in strategic human resources, women in leadership and racial and gender inequality in organizations, she works to ensure business research and teaching at Smith are training emerging leaders to thrive within the changing aspects of society.
### Dr. Jane Philpott
Dean, Faculty of Health Sciences, Queen's University; CEO, SEAMO
Dr. Jane Philpott is the Dean of the Faculty of Health Sciences, Director of the School of Medicine at Queen's University, and CEO of the Southeastern Ontario Academic Medical Organization. She is a medical doctor, a Professor of Family Medicine, and former Member of Parliament. Prior to politics, Jane spent the first decade of her medical career in Niger, West Africa. She was a family doctor in Markham-Stouffville for 17 years and became Chief of Family Medicine at Markham Stouffville Hospital in 2008. From 2015 to 2019 she served as federal Minister of Health, Minister of Indigenous Services, President of the Treasury Board and Minister of Digital Government. She is currently the Chair of the Ontario Health Data Council and was recently appointed as a Commissioner to the Global Commission on Drug Policy.
### Kim Fulton
Coaching and Leadership Practice Lead
Kim Fulton is a leadership expert, facilitator, and strategic advisor to organizations ranging from global Fortune 500 companies to non-profits. Prior to joining Third Factor, Kim was a Principal at management consulting firm Kearney, where she led the firm’s thought leadership and client offerings on employee experience topics. Kim is a passionate advocate of diversity, equity, and inclusion (DEI) initiatives and was the leader of Kearney’s Women’s Network across North America and Latin America. She also completed a secondment with Catalyst, a global non-profit and leading voice on workplace gender equity.
### Meredith Dault
Moderator
Meredith Dault is a journalist and communications specialist. She has worked as a reporter and producer with CBC Radio in Ottawa and Halifax, and her work has been published widely, including in the Ottawa Citizen, the Globe and Mail, Kingston Life and online at Reader’s Digest Canada. She is the manager, content and media production in the Centre for Content Development at Smith School of Business and is the regular host of Smith Business Insight webinars.
Tags:

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=201712) 
 _https://smith.queensu.ca/news_blog/archive.php?a=201712_

[## UPstart Venture Challenge gives emerging startup a $30,000 boost
](https://smith.queensu.ca/news_blog/2017/2017_UPstart_Venture_Challenge.php)
December 20, 2017
Toronto, ON – On the evening of Dec. 7, eight emerging Queen’s startups pitched their businesses to a jury of angel investors during the second annual UPstart Venture Challenge. The event was organized by the Queen’s Venture Network and hosted at LoyaltyOne in Toronto.
[## Students look to solve global food security at Queen’s challenge
](https://smith.queensu.ca/news_blog/2017/2017_Innovation_Challenge.php)
December 12, 2017
Kingston, ON – The Queen’s International Innovation Challenge was recently held, with the finals in Toronto on Nov. 24. Teams came up with solutions for one of the world’s most pressing issues: food security. We spoke with Dean McKeown, Associate Director, Administration, at Smith School of Business’ Scotiabank Centre for Customer Analytics, about this year’s event.

# [BraTopia | Smith Magazine](https://smith.queensu.ca/magazine/startups/bratopia.php) 
 _https://smith.queensu.ca/magazine/startups/bratopia.php_

**My company,** BraTopia, is a women’s lingerie and swimwear store specializing in perfectly fitted foundation garments and swimwear. We fit women across the size spectrum, from petite to plus and everyone in between, in a comfortable, all-female environment. We also feature specialized products, for nursing mothers, cancer survivors, and athletes looking for the perfect sports bra.
**Scope:** Calgary store employs 9, and has revenues approaching $1 million
**My ‘aha moment’:** While looking for a proper-fitting sports bra in Calgary, I could not believe how challenging it was to find such a thing, especially in a city this size. When I finally did find one, it was at a store in an industrial area that operated by appointment only. That’s when I knew I wanted to make this process easier for women.
**The most important thing I’ve learned** about starting a business is that nothing is certain. Your best laid plan can get derailed, and your pay is typically unpredictable. You need to trust your gut instinct, and be firm when necessary. Nobody will care more about your business than you, the owner.
**The most fun I’ve had so far** was when I saw the elation that a properly fitting bra can bring to a woman. Some women have been reduced to tears of gratitude, so it’s been incredibly rewarding to be able to help them. I was also extremely gratified when I requested donations from my suppliers to help Calgary’s flood victims. I was amazed at how highly these women valued the donated bras, especially those who had lost so much.

# [Managing and Auditing Whistleblowing Systems | Smith Business Insight](https://smith.queensu.ca/insight/content/Managing-and-Auditing-Whistleblowing-Systems.php) 
 _https://smith.queensu.ca/insight/content/Managing-and-Auditing-Whistleblowing-Systems.php_

Financial accounting fraud in capital markets represents a grave threat to companies and the public interest. Whistleblowing can be an important deterrent to fraud. 
However, blowing the whistle is fraught with challenges and obstacles. How can organizations and, in particular, internal auditors design and manage effective whistleblowing mechanisms to increase accountability and trust and uncover misconduct? 
Watch this free 60-minute webinar about whistleblowing: the issues involved and how to manage internal systems. 
This webinar was presented on November 1, 2023, by Smith Business Insight and the CPA Ontario Centre for Corporate Reporting and Professionalism. Bertrand Malsch, associate professor of accounting at Smith, moderates a discussion with a panel of experts: Pamela Forward, president of the Whistleblowing Canada Research Society; Charles Cron, director of inspections at the Canadian Public Accountability Board; and Danny Weill, executive vice-president at ALIAS Solution. 
**Participants learn:** 
* Best practices of successful whistleblowing policies and implementation strategies
* How external auditors can effectively assess whistleblowing systems
* How to encourage whistleblowing and enable people to tell the truth
* What it means to be a whistleblower and the challenges with speaking up
* What to consider when launching whistleblowing investigations (including cultural and inclusion issues)
Following the presentation there is an audience Q&A with our speakers. 
**About the CPA Ontario Centre for Corporate Reporting and Professionalism**
The CPA Ontario Centre for Corporate Reporting and Professionalism at Smith School of Business was established in 2021 thanks to the generous financial support of CPA Ontario. The centre’s goal is to promote creative and innovative ideas around corporate reporting reforms and the development of new forms of professional expertise. The centre also advocates for inclusion and recognition of the diversity of stakeholders beyond shareholders in defining good corporate reporting and professionalism.
## Session Participants
### Dr. Bertrand Malsch
Professor & PWC/Tom O'Neill Professor of Accounting
Bertrand Malsch is an Associate Professor & PWC/Tom O'Neill Professor of Accounting at Smith School of Business and the 2020 recipient of the Award for Research Excellence. He is the author of numerous leading articles in international academic journals on the subject of auditing, accounting regulation and governance. His work has been presented in many scholarly and professional conferences around the world. He is a member of the Quebec Bar.
### Danny Weill
Executive Vice-president, ALIAS Solution
Danny Weill is executive vice-president of ALIAS Solution, a leading Canadian-based whistleblowing/reporting and case management platform. He joined ALIAS in 2022 and positions ALIAS as the go-to solution for North American organizations seeking to create a culture of transparency, openness and accountability among stakeholders. Prior to joining ALIAS, Danny spent nine years as part of the leadership team with LifeSpeak, a leading global mental health and well-being platform. In addition to speaking at conferences and business schools across North America, Danny recently appeared before the Canadian House of Commons Heritage Committee as an expert on safe sport.
### Pamela Forward
President, Whistleblowing Canada Research Society
Pamela Forward is a workplace mediator and researcher. Her experience includes both management and advisory positions at the national and international levels and her career includes working in government (federal public service and adviser to federal cabinet ministers), business and health care. Her interest in whistleblowing advocacy began in the 1990s when she joined with others to support whistleblowers in the federal public service.  She recently completed an in-depth, qualitative case study on whistleblowing regarding drug safety issues at Health Canada, which highlighted many system flaws resulting in reprisals against truth-tellers and impunity for wrongdoers.
### Charles Cron
Director of Inspections, Canadian Public Accountability Board
Charles Cron, CPA, CFE, is a director of inspections at the Canadian Public Accountability Board. In addition to performing inspections of audits, Charles works with the CPAB’s thought leadership group on its fraud initiative. Charles started his career at Deloitte focusing on financial statement audits of public companies. The CPAB oversees public accounting firms that audit Canadian reporting issuers. It promotes audit quality through proactive regulation, robust audit assessments, dialogue with domestic and international stakeholders and practicable insights that inform capital market participants and contribute to public confidence in the integrity of financial reporting.

# [Exploring the role of business now](https://smith.queensu.ca/yearinreview/features/business-now.php) 
 _https://smith.queensu.ca/yearinreview/features/business-now.php_

Feature
Should companies be responsible for making the world a better place? This year, Smith asked both consumers and business leaders for their ideas
What place does the corporate world have in society today? With big challenges like climate change, political instability, income inequality and the need for racial justice and Indigenous reconciliation, the role of businesses is certainly shifting. But how, and what should leaders be doing to effect meaningful change?
With those questions in mind, Smith this year explored corporate impact and the important position that companies have in society today. The result was “This is business now”, a website that included interviews with business leaders and a survey that gauged how Canadians want companies to contribute to society and the environment.
Among the leaders that Smith spoke with were alumni including Alvin Hew, BCom’86; Connie Lo, BCom’15, GDA’15; Colin Lynch, BCom’07, Artsci’07; Mounir Nasri, MMIE’20, Artsci’19; Meghan Roach, BCom’05; and Hakeem Subair, MMIE’17. They offered nuanced views on everything from the importance of taking care of employees and responsible leadership, to balancing profits with social good and the challenges of speaking out on contentious social issues.
From left: Connie Lo, BCom’15, GDA’15; Colin Lynch, BCom’07, Artsci’07, and Meghan Roach, BCom’05, were among business leaders who contributed their ideas for “This is business now.”
As Smith professor of organizational behaviour Julian Barling noted, “Business leaders now have a responsibility that extends beyond the organization, and—in the larger sense—beyond the present, into future generations. They occupy a pivotal place in society.”
Consumers seem to agree with those sentiments. The survey that Smith commissioned, conducted by Proof Strategies, put a battery of questions to Canadians 18 to 84 from across the country. To the question of whether businesses should do more than they do now to solve society’s problems and help meet the needs of people, 52 per cent of respondents agreed. (Another 32 per cent somewhat agreed.) On average, respondents said that businesses should dedicate 21 per cent of their profits to important social issues.
Those results do not surprise Jacob Brower, associate professor of marketing at Smith, who studies corporate social responsibility. “Corporations are the most powerful entities on earth,” he says, so people want more from them. “They see businesses as having the agility and speed to actually do something, and potentially that they hold some responsibility for some of the social ills that they see.”
Where do corporate leaders go from here in making a difference? “This is business now” highlighted the issues they face in balancing people and profit. Meant to spark a conversation in the corporate world, it delivered on that goal, with over 35 million impressions, 124,900 page views and over 3.3 million completed digital video views from January 30 to April 30 of this year.

# [Pilot project provides business training for First Nations community](https://smith.queensu.ca/news_blog/2020/2020_Pilot_project_provides_business_training_for_First_Nations_community.php) 
 _https://smith.queensu.ca/news_blog/2020/2020_Pilot_project_provides_business_training_for_First_Nations_community.php_

Christina Tachtampa and Jonathon Araujo Redbird of Redbird Circle.
**Kingston, Ont. –** A Smith School of Business initiative that launched on Monday will bring online business training to a First Nations community in British Columbia. Thirty-five members of the Xeni Gwet’in community will take part in the 12-week program to earn a Certificate of Completion in Administration and Business Management through the Centre for Business Venturing at Smith.
The pilot program will see participants work on projects that align with their community’s strategic plan. They will learn project management and strategic thinking skills that can be applied to areas of need within their community. 
The program is led by Jonathon Araujo Redbird and Christina Tachtampa of Redbird Circle, an educational training and consulting company with an Indigenous focus. Both Redbird and Tachtampa are graduates this year of the Master of Management Innovation and Entrepreneurship (MMIE) program at Smith. Redbird Circle was their capstone project.
This will be the first time the pair has a chance to deliver their customized educational content to a First Nations audience, teaching alongside a handful of MMIE instructors and advisers. Each module will also feature Indigenous speakers sharing their own perspectives and experiences, an approach the pair believe is critical to holistic learning. 
“It’s the medicine wheel,” explains Redbird, who is of European and Anishinaabe (Odawa Ojibwa) ancestry from Wiikwemkoong Unceded Territory, of their educational approach. “It’s a four-dimensional framework that is basically teaching people how to come back to balance. Before we get into teaching about bookkeeping or marketing, we need to be able to start at the core. How do we bring the business world, our dominant culture… how do we swing the pendulum back to Indigenous values and philosophies, merging the two to create an elevated humanity?” 
“How do you develop that balance between Indigenous and non-Indigenous ways of knowing, being and doing?” adds Tachtampa, who came to Canada from Greece. “What is the true meaning of reconciliation and building trust? That is a piece of our partnership that works well, balancing western and Indigenous world views.” 
The program got its start thanks to a summer internship grant from the federal government that funded three students, including Tachtampa, to work with the Xeni Gwet’in community, a member of the Tsilqhot’in (Chilcotin) First Nation, in order to help it identify strategic priorities.
Shari Hughson, director of the MMIE program, who already had an established working relationship with the community of 450, recognized the opportunity. One of the projects that emerged was a proposal for the certificate program, which has since received $70,000 in funding from the B.C. government. “Each student will have a practical project that they will work through over the three months of the program, to move them forward,” explains Hughson. “It is our hope that they will then be able to secure funding to keep the project going.”
“It is a program that will provide workforce development and entrepreneurial training,” adds JP Shearer, the partnership lead for Smith who is involved both as an adviser to the MMIE program and as the associate director of the Centre for Business Venturing. “It will give participants a chance to learn new skills through immersive learning experiences that can be immediately applied to their career search, job or even start their own ventures and to think like entrepreneurs… and then eventually to become self-sufficient in generating their own revenue. It is an exciting prospect.”

# [About Us](https://smith.queensu.ca/invest/about-us.php) 
 _https://smith.queensu.ca/invest/about-us.php_

**Smith Development & Alumni Relations** 
We provide resources and services for ~25,000 Smith alumni (Commerce and Masters-suite alumni), including SmithConnect, our exclusive online student and alumni directory and engagement platform, business clubs, networking events, reunion planning, and continuous learning opportunities through Smith Insight. As well, the department offers ways for alumni to give back to their alma mater through sharing their time, knowledge or financial support, to help ‘pay it forward’ to the next generation of business leaders at Smith. 
**Our Mission 
** 
To develop outstanding leaders with a global perspective, and to create new knowledge that advances business and society. Our Vision is to be one of the world's most innovative and influential business schools.
**Our Values**
* Excellence and innovation
* Respect for self and others
* Ethics and integrity
* Collaborative relationships with alumni, partners, and stakeholders

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=202309) 
 _https://smith.queensu.ca/news_blog/archive.php?a=202309_

[## Smith welcomes new faculty
](https://smith.queensu.ca/news_blog/2023/Smith-welcomes-new-faculty.php)
September 5, 2023
Kingston, Ont. – Ten new faculty have joined the business school’s outstanding roster of teachers and researchers in recent months. The new assistant and associate professors bring a diverse set of experiences and backgrounds to the school, plus expertise in strategy, marketing, accounting, finance, economics, digital technology and management analytics.

# [Our Insight Topics | Smith Business Insight](https://smith.queensu.ca/insight/tag.php?tid=International%20Women%27s%20Day) 
 _https://smith.queensu.ca/insight/tag.php?tid=International%20Women%27s%20Day_

The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=202009) 
 _https://smith.queensu.ca/news_blog/archive.php?a=202009_

[## Pilot project provides business training for First Nations community
](https://smith.queensu.ca/news_blog/2020/2020_Pilot_project_provides_business_training_for_First_Nations_community.php)
September 24, 2020
Kingston, Ont. – A Smith School of Business initiative that launched on Monday will bring online business training to a First Nations community in British Columbia. Thirty-five members of the Xeni Gwet’in community will take part in the 12-week program to earn a Certificate of Completion in Administration and Business Management through the Centre for Business Venturing at Smith.
[## Women in Capital Markets recognizes four Smith alumni
](https://smith.queensu.ca/news_blog/2020/2020_Women_in_Captial_Markets_recognizes_four_Smith_Alumni.php)
September 17, 2020
Kingston, Ont. – Four Smith alumni have been selected to take part in a prestigious annual leadership program run by Women in Capital Markets (WCM). The four are among 36 women chosen for the 2020 Emerging Leaders Award Program, an eight-month initiative designed to support the professional development and retention of mid-career women with five to 10 years of capital markets experience.

# [The lasting legacy of Mel Goodes](https://smith.queensu.ca/news_blog/2024/2024-Smith-remembers-Mel-Goodes-lasting-legacy.php) 
 _https://smith.queensu.ca/news_blog/2024/2024-Smith-remembers-Mel-Goodes-lasting-legacy.php_

**Kingston, Ont. –** Philanthropist, pharmaceutical pioneer, and business leader Melvin Goodes, BCom’57, LLD’94, is being remembered for his lasting impact on Smith and Queen’s, and the students and researchers who benefited from his generosity.
Mel, the former chief executive officer of Warner-Lambert (now Pfizer) and director of both the [Alzheimer’s Drug Discovery Foundation](https://www.alzdiscovery.org/) (ADDF) and the Melvin R. Goodes Family Foundation, passed away on Sept. 30 at the age of 89.
“I was deeply saddened to learn of Mel Goodes’ passing,” says Wanda Costen, Dean, Smith School of Business. “I was honoured to meet Mel and Nancy in 2022. I learned of Mel’s deep understanding of the role of business in society—long before business organizations were focused on corporate social responsibility and ESG—and his commitment to giving back. In particular, I was struck by his steadfastness in living a life that illustrated how one uses one’s privilege to advance the greater good. 
Smith School of Business faculty, staff, and students are privileged to teach, work, and learn in a building dedicated to Mel’s parents in recognition of their sacrifices and work ethic that led to Mel’s values-driven leadership and success.”
One of the university’s most generous supporters and a former member of the Board of Trustees, he was also a dedicated volunteer committed to helping Smith School of Business achieve its mission and vision. Mel and his wife Nancy were the lead donors for the capital project to ensure business students and researchers have effective space to work under one roof.
In recognition of his transformational gift to the project, the new building was named Goodes Hall. Mel and Nancy’s generosity also helped fund a further expansion, providing a welcoming gathering space, Goodes Commons, in 2012.
"I truly feel that this gift is a sound investment in the future," Mel said when Goodes Hall opened in 2002. "\[Smith\] School of Business has shown with its innovative and high-quality programs that it can meet the challenges of a global society. Having one central home where all these initiatives can come together will provide the School with the kind of presence it requires for the 21st century."
In 2006, the Melvin R. Goodes Entrance Award was created to support students entering an undergraduate program. Established by the Melvin R. Goodes Foundation in honour of Mel, the annual renewable award continues to attract the brightest students.
Mel was also a long-time supporter of groundbreaking academic research, establishing the [Monieson Centre for Business Research](https://smith.queensu.ca/centres/monieson/index.php) at Queen’s in 2000. The centre is named after his mentor Danny Monieson, a professor emeritus of Marketing at the university.
"Mel Goodes' legacy will live on through the ongoing research that progresses thanks to his generosity, the lives he continues to impact, and the building that bears his family’s name," says Principal and Vice-Chancellor Patrick Deane. "The researchers at The Monieson Centre for Business Research and the student recipients of the Melvin R. Goodes Entrance Award, will advance the work Mel was passionate about and make positive contributions to society."
His generosity extended farther than the Queen’s community and one of his greatest areas of advocacy was Alzheimer’s research. Long-time members of the ADDF Board of Directors, Mel and Nancy helped to progress Alzheimer’s science and Mel used his considerable industry knowledge to push drug development forward. Mel and Nancy also established the [Melvin R. Goodes Prize for Excellence in Alzheimer’s Drug Discovery](https://youtu.be/Z_TYqoGRjsY?si=X2jjNvFXkP7aKY2V), in 2015. Described as the Nobel Prize for Alzheimer’s research, the annual prize funds disease-modifying drug research to establish better treatments and to find a cure.
Queen’s University will continue to honour Mel for his enduring contributions to the university and beyond.

# [Kinnear New Venture Competition: 2024 Winners Announced](https://smith.queensu.ca/news_blog/2024/2024-Kinnear-Competition-Winners.php) 
 _https://smith.queensu.ca/news_blog/2024/2024-Kinnear-Competition-Winners.php_

Kinnear New Venture Competition winners: Chris Rambihar and Thomas Toulgoet of Evermore (top); and Theo Lemay, Azeem Khan, Jasmine Wu and Marcus Wright-Smith of Monarch Informatics (bottom).
**Kingston, Ont. –** Smith’s [Centre for Entrepreneurship Innovation & Social Impact](https://smith.queensu.ca/centres/ceisi/index.php) (CEISI) has awarded a total of $10,000 to new ventures as part of its annual Paul & Tom Kinnear New Venture Competition.
Two teams successfully pitched their businesses to a panel of judges earlier this month, securing funding for their ventures’ ongoing operations.
Chris Rambihar, MBA’25, and Thomas Toulgoet, Comm’28, were awarded $7,500 for their business Evermore, which aims to help extend the life of pet owners' beloved canine companions. The company’s natural treats infused with a proprietary formula target common aging issues, including cognitive decline, joint discomfort and digestive issues. 
“This funding will support our goal of revolutionizing pet wellness and enhancing the lives of our beloved animals. We aim to begin production of our proprietary longevity treats in the near future,” says Rambihar. “Evermore is just getting started, with many more milestones to come.”
Marcus Wright-Smith, Comm’25; Azeem Khan, Comp’25; and Jasmine Wu, Artsci’25, also impressed the judges, earning $2,500 for their venture, [Monarch Informatics](https://monarchinformatics.ca/). Monarch’s data analytics platform provides hospital laboratories with real-time insights on laboratory operational metrics to improve efficiency. The team also includes Theo Lemay, BSc(Eng)’25; Prameet Sheth, director of microbiology at Kingston Health Sciences Centre (KHSC); Henry Wong, molecular biologist at KHSC; and Calvin Sjaarda, bioinformatician at KHSC.
“The award from the Kinnear New Venture competition couldn’t have come at a better time. Monarch is preparing to launch the pilot program to test its product, LOLA, in a number of hospitals in Ontario. This funding will allow Monarch to build out further security and authentication for LOLA’s users, which needs completion before the pilot can begin,” explains Wright-Smith.
Since its creation in 2008, the Paul & Tom Kinnear New Venture Competition has supported 21 Smith undergraduates and their entrepreneurial ventures with funding that is often critical in the early stages of business and increases the odds of success. 
“At CEISI, we take pride in fostering the growth of emerging entrepreneurs through initiatives such as the Paul & Tom Kinnear New Venture Competition," says Simon VanAsseldonk, Program Coordinator, Centre for Entrepreneurship, Innovation & Social Impact. "The teams behind Evermore and Monarch Informatics are doing impactful work, and we look forward to seeing what the future holds.”

# [Financial Times publishes 2023 EMBA ranking](https://smith.queensu.ca/news_blog/2023/2023_Financial-Times-publishes-2023-EMBA-ranking.php) 
 _https://smith.queensu.ca/news_blog/2023/2023_Financial-Times-publishes-2023-EMBA-ranking.php_

**Kingston, Ont.** – Smith School of Business’ two EMBA programs are ranked top 100 in the world by the Financial Times (FT).
Smith’s Executive MBA – The National Program and Executive MBA Americas secured spots in the just-released FT 2023 ranking of global Executive MBA programs.
“We are honoured to receive this recognition from the FT, placing Smith School of Business at the forefront of executive business education,” said Professor Wei Wang, Associate Dean, Professional Graduate Programs. “Our EMBA programs are designed to empower professionals to reach new heights in their careers. The school’s strength in this area is evidenced in our rankings.”
The Smith Executive MBA – The National Program moved up 24 spots to No. 58 overall. Alumni salaries increased by an average of 75 per cent, the highest increase in Canada. This metric is based on the difference in alumni salaries from before the EMBA and now.
The Executive MBA Americas program, a partnership between Cornell University’s Johnson Graduate School of Management and Smith School of Business at Queen’s University, was ranked in the top 50 programs worldwide at No. 47, with overall satisfaction with the program rated 9.24 out of 10 by alumni.
“Our approach to leadership development goes beyond the classroom,” said Professor Wang. “Our students receive personalized executive coaching, empowering them to reach their full potential and become the leaders of tomorrow.”
The Financial Times ranking is based, in part, on a survey of alumni three years after graduation to get a clear snapshot of salary increase and career progress post-EMBA. The FT also collects data from each school on the diversity of students, faculty and board members, as well as international experience, environmental, social and governance (ESG), and faculty research.
Five Canadian programs made the 2023 ranking. View the [full FT 2023 Executive MBA ranking](https://rankings.ft.com/rankings/2950/emba-2023).

# [ISF - Smith School of Business](https://smith.queensu.ca/centres/isf/index.php) 
 _https://smith.queensu.ca/centres/isf/index.php_

The Institute for Sustainable Finance is a multi-disciplinary network of research and professional development that brings together academia, the private sector, and government to shape Canada’s innovations in sustainable finance.
## What is Sustainable Finance?
The Canadian Expert Panel on Sustainable Finance defines it as: capital flows, risk management activities, and financial processes that assimilate environmental and social factors as a means of promoting sustainable economic growth and the long-term sustainability of the financial system.
In its simplest form, this means aligning our financial systems and services to promote long-term environmental sustainability and economic prosperity. Learn more about Sustainable Finance through our [Primer Series.](https://smith.queensu.ca/centres/isf/resources/primer-series/index.php)
**Ryan Riordan,** Distinguished Professor of Finance at Smith School of Business and director of research at the Institute for Sustainable Finance explains sustainable finance.
## Newsblog
December 17, 2024
### Call for papers for the 2025 CSFN Conference: Deadline March 15
The CSFN Conference invites submissions of original research papers for presentation at the 2025 conference to be held June 5-6, 2025 at Schulich School of Business, York University in Toronto. The conference brings together academics and financial industry participants with a shared commitment to sustainable finance, offering a forum for exploring the latest research and educational innovations in the field.
December 17, 2024
### Next steps for sustainable finance in 2025: Environment Journal
In a Q & A with ISF's Maya Saryyeva, Environment Journal covers the emerging trends and upcoming research that will drive sustainable finance in 2025, from getting nature on the balance sheet to dealing with political headwinds.

# [Research - Centres & Initiatives at Smith](https://smith.queensu.ca/research/centres-and-initiatives.php) 
 _https://smith.queensu.ca/research/centres-and-initiatives.php_

Smith’s research centres and initiatives focus on moving research forward, applying insights to business applications, working with business partners, and enriching students’ education. Our centres and programs bring together faculty, students and practitioners who share their passion for discovery.
## The Institute for Sustainable Finance
The Institute for Sustainable Finance is a multi-disciplinary network of research and professional development that brings together academia, the private sector and government to shape Canada’s innovations in sustainable finance. The Institute is at the intersection of sustainability and finance. Its mission is to align mainstream financial markets with Canada’s transition to a prosperous sustainable economy.
## Scotiabank Centre for Customer Analytics
The goals of the Scotiabank Centre for Customer Analytics are: to bring together professors, graduate students and analytics practitioners to collaborate on applied research projects in customer analytics; and to build a community of data intensive users encouraging innovation across industries, in order to deliver a re-imagined customer experience.
## Centre for Entrepreneurship, Innovation & Social Impact
The Centre for Entrepreneurship, Innovation & Social Impact addresses the evolving dynamics of business today – inspiring and supporting the success of new ventures, building innovation capabilities in people and organizations, and fostering research, education and community engagement on responsible leadership and social impact.
## CPA Ontario Centre for Corporate Reporting and Professionalism
The CPA Ontario Centre for Corporate Reporting and Professionalism at Smith School of Business is committed to improving corporate governance in Canada through a variety of research and teaching programs. The Centre funds academic research into Canadian and international corporate governance issues, and contributes to the creation of leading-edge curriculum. The Centre is partially funded through the generosity of the Chartered Professional Accountants of Ontario.
## The Monieson Centre for Business Research
The Monieson Centre funds collaborative faculty initiatives, driven by rigorous academic research that forms the foundation for usable knowledge that impacts our thinking about business issues of contemporary importance. At present, the Monieson Centre is supporting six collaborative research initiatives.

# [Fake News Gives Brands a Real Headache | Smith Business Insight](https://smith.queensu.ca/insight/content/Fake-News-Gives-Brands-article.php) 
 _https://smith.queensu.ca/insight/content/Fake-News-Gives-Brands-article.php_

**When I was a magazine editor** in the 1990s and early 2000s, most brand advertisers and the agencies they employed had a keen interest in the placement of their advertisements. They wanted prime real estate, of course — a right-hand page, the inside or outside back cover or opposite the table of contents. So our ad salespeople also had to be alert to the stories positioned alongside particular ads. One time, someone took their eye off the ball and allowed an Air Canada message to appear next to a feature about an airplane crash investigation. I think we would still be offering Air Canada free makeup spots to this day were the magazine still alive.
My, how far we have come. For much of their online advertising — which is to say most advertising — brand managers now readily turn over the ad placement decision to algorithms that promise to deliver the demographically correct audience. If their messages appear alongside the finest sludge that conspiracy theorists and malignant actors can produce, it’s just the cost of pitching product in the digital age. Placement be damned.
Did someone forget to tell marketing executives there is a massive fake news crisis in societies around the world? Bad actors, now using generative AI, are creating alternate realities — from political propaganda to health-related fake news — that are undermining civil society. [Research has found](https://www.science.org/doi/10.1126/science.aap9559) that falsehoods reach 1,500 people six times faster than the truth. Social media users are 70 per cent more likely to share or retweet falsehoods than facts.
It’s not like advertisers are untouched by fake news. Eli Lilly’s stock price fell by more than four per cent after a fake Twitter account impersonating the company falsely announced insulin would be given away for free. Kay Jewelers lost 11 per cent of its share value in the week after fake news claimed its rings used low-quality gemstones instead of real diamonds.
Pepsi lost a lot of its fizz — twice. In 2016, its shares fell by four per cent during the U.S. presidential election campaign after false information circulated that Pepsi’s CEO supported Donald Trump. Two years later, Pepsi’s share price was hurt when fake news spread online that Pepsi products were laced with HIV-infected blood.
## **Brands score an own goal**
These are all examples of misinformation aimed at big corporate targets. But marketers also willingly expose their brands to contamination from fake news when they use [programmatic advertising](https://digitalmarketinginstitute.com/blog/the-beginners-guide-to-programmatic-advertising). This popular technique for managing online advertising relies on algorithms to place banner ads on web pages that maximize reach to targeted audiences. Brands generally have little control over where their ads are displayed; the algorithms are optimized based on the marketing goals of audience views or conversions, not on avoiding fake news. As a result, some of the largest household brands have messages running alongside misinformation.
Jacob Brower, an associate professor and Distinguished Teaching Fellow of Marketing at Smith School of Business, says the loss of control and potential exposure to fake news is a problem that marketing executives seem to ignore. “Are enough of them staying up at night \[because of fake news\]?” he asks. “No, because more and more they’re just relying on metrics and algorithms.”
Brower adds: “When you let the algorithm run and you have conversion set up to be your metric, it will do whatever it takes to get the right people that are going to convert. Is that good for your long-term brand image versus getting the transaction today? For every eyeball that turns into a conversion, how many people are you reaching that are saying, I can’t believe their ad is right next to that post.”
Recent research reveals the brand damage that a close encounter with fake news can cause. [One study](https://www.sciencedirect.com/science/article/abs/pii/S1094996818300525) found that news content low in truthfulness can hurt brands when their messages are displayed on the same web page. When the study participants perceived a news article as less credible, they were more likely to mistrust the advertised brand and to hold negative brand attitudes.
This finding wasn’t a flash in the pan. [Experiments conducted recently](https://www.degruyter.com/document/doi/10.1515/commun-2022-0110/html?lang=en) with Dutch consumers were the first to give empirical evidence that brands can be contaminated by disinformation. The study confirmed that when an ad is displayed on the same web page as fake news, brand attitude and brand trust are negatively affected. The effect is even stronger when the ad has some connection with the fake news (such as when a message from a mobile service provider is shown alongside fake news about 5G).
But the negative brand effects reach even further. The experiments showed that when an ad is delivered alongside misinformation, people are more likely to believe the fake news.
In short, brand advertising appearing next to misinformation has a triple-whammy effect: it provides an incentive for websites to publish fake news; it increases the credibility of the fake news; and it exposes the brand to consumer blowback and reputational damage.
## **How to fight fake news**
Brands that are serious about inoculating themselves from the spillover effects of misinformation and rebuilding brand trust share similar practices. They are adept at using tools such as blacklists of fake news sites, they contract with ethical digital ad agencies, and they devote resources to monitoring fake news in real time.
They also do not expect fact-check labels used by some social media sites to solve the fake news problem for them, which is prudent. A recent experiment showed that a news story flagged as false not only undermines the credibility of the story but also the credibility of the adjoining ad and brand. Even when the fake news has a positive spin, a fact-check label damages nearby ads.
Emerging evidence from fake news researchers offers other guidance. Experiments in psychology, for example, have found that corrections issued by a company can be effective at reducing false beliefs. The corrections are particularly effective when they include a factual alternative explanation for why the misinformation is false or why it may have spread (the myth-and-fact approach). Recent research has found that providing additional details increases the longevity of correction effects.
Studies have also laid to rest concerns that repeating false claims, even in a correction, is counterproductive by giving more oxygen to the original lie.
In the medium term, brands may have more tools to work with. It’s likely that a hybrid approach will develop in which humans work with AI and machine learning algorithms to ensure ads are not placed next to compromised content. AI has already revealed that fake news stories are substantially more negative than real news and that they trigger emotions of disgust and anger. Algorithms are undoubtedly being trained to sniff out potential fake news that marketing staff can then verify.
A cynic may say that big brands are getting what they deserve. Marketers have always skirted the line between fact and fiction and have increasingly adopted “[truthiness and post-fact positions](https://journals.sagepub.com/doi/abs/10.1177/0276146718755869?journalCode=jmka).” Many of them churn out dubious product claims that look a lot like fake news. Some industries — notably Big Tobacco and Big Oil — have mastered the art of undermining medical and environmental science to maintain their social licence to operate.
An optimist may respond by suggesting that the fake news crisis is an opportunity for firms to revisit their digital advertising strategies and to view these strategies through the lens of social responsibility. It’s also a chance to revisit how their brands are managed.
As Brower points out, in today’s marketing world, the keepers of the ad dollars, focused on short-term metrics, are seen as more credible than the keepers of the brand, who talk about ephemeral long-term brand value yet struggle to have their voices heard. As a result, technology-driven tactics designed to drive clicks and conversions win out, even if it means inadvertently feeding the misinformation monster and tarnishing the brand.
“From a branding perspective, this handing over the keys to data scientists and algorithms — especially AI where we can’t see what’s inside the black box — can lead to bad situations,” says Brower. “It can lead to situations where you’re actually deteriorating the value of the brand in exchange for short-term bumps in sales . . . Yes, you’re getting sales, but at what cost? And we don’t know the cost.”
Tags:

# [If you're ever in Lausanne, Switzerland | Smith Magazine](https://smith.queensu.ca/magazine/issues/spring-2024/connect/if-youre-in.php) 
 _https://smith.queensu.ca/magazine/issues/spring-2024/connect/if-youre-in.php_

Helen Vasilevski’s career has taken her to live in six countries and experience life in over 80. Born in Hamilton, the self-described city person has spent the past 18 years boomeranging back to Switzerland between work trips. As founder and managing director of advisory and fractional management firm flect., her work takes her across the globe, but she’s put down roots in Lausanne. She moved to “The Capital of Sport” and the home of the International Olympic Committee in 2006, trading the hustle and bustle of city life in Toronto and New York City for hiking, paddle boarding and skiing.
If you’re planning a trip, Vasilevski suggests activities that combine both natural beauty and tourist spots in Lausanne and the surrounding region. Why venture beyond the city? For perspective, Kingston to Toronto or Montreal is about the same distance as crossing Switzerland from Geneva to Zurich, so there’s “lots to see and discover within 15 to 30 minutes of Lausanne,” she says.
## Tourist traps you can’t miss:
The Olympic Museum. Walk uphill (everything is uphill in Lausanne!) from the lakeside to the front entrance. The interactive museum is great. Enjoy a meal at the restaurant (it has amazing views of the lake), or eat nearby at the terraces of Château d’Ouchy, Hôtel Angleterre or Beau Rivage Palace.
## Hidden gem:
La Cité (Old Town) and the Cathedral de Lausanne. Most people focus on the lake, the Alps and the vineyards. La Cité is amazing with a twist and turn at every point. The cathedral was built in the 12th century. Between 10 p.m. and 2 a.m., the cathedral’s night watchman stands at the top of the bell tower and shouts out each hour to the residents: “Plus ça change...”
## For a short jaunt:
Use public transit including the CGN boat cruise from Lausanne and be sure to stop at Evian (La Source), Château de Chillon (the impetus for Byron’s “Prisoner of Chillon”), Montreux (Freddie Mercury statue), or Vevey (Charlie Chaplin Museum). Slightly further by car, tour the Cailler Chocolate Factory and visit Gruyères (home to foundue and the HR Giger Museum).
## Best place for families:
Walk along La Petite Corniche in the UNESCO-listed Lavaux vineyard terraces for the view. Most owners don’t mind if you walk through the vineyards. Stop at Le Deck or at one of the many maisons for a glass of wine (“Prenez un verre”). Swim in Lake Geneva (Lac Léman; jump in from anywhere, really) or rent SUP boards. Wander the farmers’ markets for seasonal delectable produce. In winter, ski or snowshoe (“raquette”). In any season, go hiking. The views of the Alps are phenomenal and “cottage country” life abounds.
## My fav restaurants:
For Canadians, try rotisserie chicken at an original “Swiss Chalet”, the Auberge de Dully in Dully. Or enjoy the locally-sourced filets de perche at Café de la Poste or Fondue Bacchus at Le Léman, both in Lutry.
## My tip for visitors:
Check events calendars in Switzerland for your travel dates. There are globally renowned festivals and annual events. To not miss my faves, I plan my travels 12 months in advance. My top travel tip: Don’t forget to pack good walking shoes!

# [Amego Electric Vehicles | Smith Magazine](https://smith.queensu.ca/magazine/startups/amego-electric-vehicles.php) 
 _https://smith.queensu.ca/magazine/startups/amego-electric-vehicles.php_

**My company,** Amego Electric Vehicles,designs, distributes and retails electric bikes and electric scooters that require no insurance, licence or parking fees. Amego’s customers are leaving their cars at home, saving time and money, foregoing public transportation, and having fun! The company offers stylish electric bikes that emphasize safety and durability, and are available through 18 dealers across Canada and at a corporate store in downtown Toronto.
**Scope:** 4 employees, $400,000 annual revenue
**My ‘aha moment’:** I was inspired to pursue the business at a Queen’s Business Club event that featured Trend Hunter Jeremy Gutsche, AMBA’05, author of Exploiting Chaos. The light-bulb moment happened when Jeremy was asked what he saw as the next big market opportunity: “Electric bikes!” he exclaimed. Soon after, I went to China and connected with a pioneer in the industry, who showed me the ropes and travelled with me from Guangzhou to Shanghai. That’s where I selected the models that would set Amego apart from the competition, and where I found the best manufacturers of motors, controllers, moulds, batteries and frames.
**The most fun I’ve had so far** was when I formed a co-branding partnership with Ferrari’s Canadian professional race team, AIM Autosport, and travelled with them to promote our Ferrari-endorsed Amego Brave and Bold bikes.

# [Connecting our alumni](https://smith.queensu.ca/invest/impact-of-giving/tamara-mcgillivray.php) 
 _https://smith.queensu.ca/invest/impact-of-giving/tamara-mcgillivray.php_

Like many students who enrol in an MBA program, Tamara McGillivray hoped the degree she earned at Smith would help take her career to the next level. And it did. A year after graduation she joined Imperial Oil. Today, after several progressive moves within the company, she is Imperial Oil’s lead–Western Canada Fuels, a job that she loves.
Yet Tamara found another benefit to her degree: the Smith alumni network. It started when she joined the executive of the **Smith Alumni Calgary Chapter**. As she began to attend events and connect with fellow alumni, “it really hit home how strong and supportive the Smith community is for each other,” she says.
Alumni chapters provide a chance to make connections and learn. The Calgary chapter continued to thrive during the pandemic, and with the help of Tamara and fellow volunteers, it offered value to the Smith network by hosting “The Business of YYC”, a virtual event with the CEO of the Calgary Airport Authority that offered insights into Canada’s vital national transportation network.
“Our virtual and in-person events are excellent learning and networking opportunities,” Tamara says, “and they’re a chance to understand so much about different people and different industries too.”

# [Financial Times ranks Smith Master of International Business No. 1 in Canada](https://smith.queensu.ca/news_blog/2024/2024-Financial-Times-ranks-Smith-MIB-No-1-in-Canada.php) 
 _https://smith.queensu.ca/news_blog/2024/2024-Financial-Times-ranks-Smith-MIB-No-1-in-Canada.php_

**Kingston, Ont**. – Smith’s graduate program in international business has secured the top spot in the country in the recently released Financial Times ranking of global master in management programs. 
In addition to ranking No. 1 in Canada, the Smith Master of International Business (MIB) placed 70th out of 100 ranked programs globally, including a top 30 ranking for international work mobility, showcasing our alumni's experience working worldwide. The program also earned a top 50 ranking for international course experience, which reflects the number of international exchanges and internships available to students. Only three programs in North America made the top 100, with Smith the sole Canadian school to make the list.   
“This ranking reinforces that the Smith MIB is not only the top program of its kind in the country, but also stands out on the global stage," says Kerri Regan, Director, Master of International Business and Full-time MBA. "We offer a unique and immersive international experience that sets our graduates apart in the global job market." 
The FT Master in Management ranking is based on a wide range of criteria, including program design, value for money, student career progression, diversity of both students and faculty, student satisfaction, and international experience and reach.  
The complete [FT Master in Management 2024 ranking](https://rankings.ft.com/rankings/2961/masters-in-management-2024) is available on the Financial Times site. 
**About Smith’s Master of International Business** 
Smith’s Master of International Business is the must-have degree for the global business citizen. Students can earn double degrees with one of Smith’s 10 highly respected international business school partners. Or take the single degree Master of International Business in 12 months including an international exchange at one of more than 60 international business schools. This full-time program is designed to deepen students’ international expertise and provides a key differentiation to employers. Learn more: [**smithqueens.com/mib**](https://smith.queensu.ca/grad_studies/mib/index.php)

# [Equity, Diversity, Inclusion & Indigenization](https://smith.queensu.ca/engage/edi3.php) 
 _https://smith.queensu.ca/engage/edi3.php_

## What is EDI3?
This program assists equity-deserving students in finding internship opportunities for the upcoming summer, and connects them with dedicated mentors and professional development opportunities. This program is available to first, second, or third year Commerce students who are members of one (or more) of the following groups: Indigenous, Black, racialized, 2SLGBTQ+, women, first-generation, students with financial need, and students with disabilities.
## Why EDI3?
Data shows that students who secure meaningful work experiences in their first few years of higher education have significantly greater long-term career outcomes (such as faster progression to management, higher compensation, etc.) than students who do not. Equity-deserving students often face barriers to accessing these meaningful work experiences, which can put them at a disadvantage and affect their career trajectories.
The EDI3 program supports students and helps remove these barriers by connecting them with meaningful work experiences early in their academic careers, leaving a lasting impact on their future successes.

# [Highlighting our research expertise](https://smith.queensu.ca/yearinreview/features/research-expertise.php) 
 _https://smith.queensu.ca/yearinreview/features/research-expertise.php_

Feature
For 10 years, Smith Business Insight has delivered ideas with impact, courtesy of school faculty, to a business audience
What traits make leaders great? How can office teams be super-effective? These are vexing questions. Yet answers exist. If you look deep, you’ll find them in the research papers of business school professors.
But few of us have time to dig through academic journals. Luckily, some places do the work for you, turning research into articles with practical takeaways. One is [Smith Business Insight.](https://smith.queensu.ca/insight/index.php) Since it launched 10 years ago, Insight has produced more than 800 articles, [webinars,](https://smith.queensu.ca/insight/webinars.php) [podcast episodes,](https://smith.queensu.ca/insight/podcast/index.php) papers, [videos](https://smith.queensu.ca/insight/video.php) and more that feature the evidence-based expertise of Smith and Queen’s faculty and graduate students.
“There is so much business research that has implications for companies and employees and can be very useful for leaders to understand,” says Smith marketing professor Jay Handelman, PhD’96.
Smith Business Insight offers practical information for readers based on the research of Smith and Queen’s faculty.
Handelman was associate dean of research when he helped launch Smith Business Insight in March 2013. As he recalls, valuable research was being done at Smith but it didn’t usually make it to the corporate world. By contrast, research in other fields was often featured in the popular press. A good example is medical studies with the latest health information.
Handelman thought business research deserved a larger audience. And so, Smith Business Insight was born. Today, it features experts on many topics—from leadership and marketing, to finance, accounting, analytics, entrepreneurship, business strategy and social impact. There’s a [monthly newsletter,](https://smith.queensu.ca/insight/newsletter.php) too.
The pandemic highlighted the value of business research when, during the first lockdown, firms grappled with the ups and downs of employees working from home. Fortunately, Smith faculty have bench strength in remote and [hybrid teamwork](https://smith.queensu.ca/insight/collection/how-to-make-hybrid-work.php) and, through Insight, provide practical advice for managers. More recently, Insight has tapped the expertise of Smith professors on workplace trends such as the four-day workweek and quiet quitting.
Looking back, Handelman recalls some concern as to whether Smith’s faculty was producing enough research to warrant a website that would publish weekly. “But that was never a question for me,” he says. “I was blown away by how much research was done at the school here. We have so much knowledge in so many areas that we can share.”

# [Business education and research](https://smith.queensu.ca/about/index.php) 
 _https://smith.queensu.ca/about/index.php_

## Smith School of Business 
at Queen’s University
Smith Business is renowned for its excellence, innovation, and leadership in business education and research.
## Strategic Plan
In 2023 Smith School of Business launched a five-year Strategic Plan following extensive consultation with faculty, staff, students and alumni. It defines our Purpose and Priorities.
[Learn more our Strategic Plan](https://smith.queensu.ca/about/strategic-plan.php)   
## Teaching & Learning
From establishing the first undergraduate business degree a century ago to creating ground-breaking programs and courses in areas including artificial intelligence, fintech, analytics, cultural diversity, team dynamics, and social impact, Smith Business is at the forefront of preparing you for the business marketplace.
We deliver an outstanding learning experience. Small class sizes, personal attention, individual and team coaching, opportunities for specialization, and a deep commitment to student success characterize the experience and deliver the [SmithEdge.](https://smith.queensu.ca/smithedge/index.php) Explore our [degree](https://smith.queensu.ca/academic_programs/index.php) and [professional development programs.](https://smith.queensu.ca/executiveeducation/index.php)
The faculty at Smith Business advance business management and society through exceptional [research.](https://smith.queensu.ca/research/index.php) Research success is the result of the commitment and knowledge of faculty, students, and staff, and of the collaborations and partnerships that extend impact.
Smith Business fosters ecosystems and [centres of focus](https://smith.queensu.ca/centres/index.php) that connect complementary activities — research, teaching, community engagement — built around core faculty strengths. We collaborate with scholars worldwide, publish in leading journals, and inspire each other to explore new lines of enquiry.
Smith Business’ expertise is shared through the [Smith Business Insight](https://smith.queensu.ca/insight/index.php) platform of content and events.
## Internationalization
Smith Business attracts top students from across Canada and around the world. The school has international exchange partnerships with more than 100 respected business schools in more than 35 countries, and welcomes more than 500 international exchange students annually. Every year hundreds of our students travel to international destinations to participate in an international exchange or to complete their Global Business Projects.
[Learn more about our international connections](https://smith.queensu.ca/international/index.php)
Our partner schools are located all over the world, including Norway, Chile, Austria, and China.
## Smith Business Advisory Board
Smith School of Business has a large network of highly-respected and accomplished advisors who share their knowledge and expertise with School leaders and support the School's mission and vision in a wide variety of ways.
[Meet our advisory board](https://smith.queensu.ca/about/advisory_bodies.php)
## Equity, Diversity, Inclusion & Indigenization
Smith School of Business is committed to cultivating a vibrant, diverse and inclusive academic and work environment rooted in a culture of mutual respect and equity such that all members of our community feel safe, possess a strong sense of belonging, and are empowered to thrive.
[Read more about our commitment to EDII](https://smith.queensu.ca/about/EDII/index.php)
## Our Name
On October 1, 2015, the School began a new chapter in its impressive history. In recognition of the generous gift of $50 million from Queen’s alumnus Stephen Smith, the School adopted a new name – Smith School of Business at Queen’s University.
[Learn more about our name](https://smith.queensu.ca/about/our-name.php)

# [Queen’s undergrads shine at Microsoft global competition](https://smith.queensu.ca/news_blog/2015/2015-02-27-ImagineCup.php) 
 _https://smith.queensu.ca/news_blog/2015/2015-02-27-ImagineCup.php_

**Kingston, ON – Feb. 27, 2015** - Two teams of Queen’s Commerce and Computing students scored impressive results in the 2015 Microsoft ImagineCup competition. First prize in the [Blueprint Challenge](https://www.imaginecup.com/blog/details/announcing-the-2015-project-blueprint-winners) went to a team comprised of Eddie Wang, Comm’18, and Computing students Jake Alsemgeest and Zaeem Anwar (pictured). Their project plan won the $3,000 top prize in the World Citizenship category for Ciris, a real-time colour augmentation overlay that allows the colourblind to more clearly see contrasts on their desktop computers and mobile devices.
Microsoft’s Imagine Cup is described as the world’s premier student technology competition. Launched in 2003, this annual event attracts thousands of participants from around the world. The first phase of the competition, the [Pitch Video Challenge](https://www.imaginecup.com/blog/details/meet-the-pitch-video-challenge-2015-winners), garnered an Honourable Mention in the Games Category for a Queen’s team comprised of Alex De Rosa, Comm’15, and School of Computing students Susan Hwang, Tianbin Jiang and Gabrielle Quilliam.
Queen’s participation in the ImagineCup is just one part of an initiative to team up Queen’s Commerce and Computing students to develop innovative, marketable computer-based applications. QSB professors Brent Gallupe, Kathryn Brohman and Tracy Jenkin are leading QSB’s role in this initiative, lending their expertise in coaching and mentoring student teams.

# [Looming Issues | Smith Business Insight](https://smith.queensu.ca/insight/content/podcast-brave-new-workplace-looming-issues.php) 
 _https://smith.queensu.ca/insight/content/podcast-brave-new-workplace-looming-issues.php_

Covid set in motion huge changes to the world of work. The dawn of artificial intelligence is adding a new dimension of uncertainty. But some things will stay the same: “People will still be crying out for high quality leadership, for autonomy, a sense of belonging, for fairness, for growth and development, for meaning and safety.” In the final episode of this podcast series, guest Julian Barling, author of _Brave New Workplace_, takes a stab at divining the future by looking at how workplaces have handled major disruptions in the past, and offers his wish list of research questions that he hopes will be answered in the years ahead. Dr. Barling is joined in conversation by host Alan Morantz. 
### **Transcript** 
\[Music playing\] 
**Alan Morantz**: The Covid pandemic really did a number on the world of work. In a couple of short years, the term workplace has lost much of its old meaning. But it’s not only Covid that has disrupted the working world. Corporations have set out seemingly en masse in search of corporate meaning. Environmental challenges loom large. Social stresses are reaching a boiling point. Where are we headed? 
Welcome to episode five of Brave New Workplace. I’m your host, Alan Morantz, senior editor of Smith Business Insight. And in our final episode, we’re talking about some big questions about work and the workplace that will need to be addressed in the coming years. Here’s my final conversation with Dr. Julian Barling, author of the newly published _Brave New Workplace_. 
\[Music playing\] 
**0:59: AM**: You have two grandchildren who will be entering the workforce 15 to 20 years from now. What do you think their experience will be like at that time? 
**Julian Barling**: It’s very difficult to even imagine what they’re going to confront. But I think what we can predict is that the world of work will have faced several, if not more, of what we can think of as major jolts or disruptions. And, having said all of that, I think an easy one would be that the reliance on forms of technology that we probably cannot even imagine right now will be things that will be taken for granted in 15 to 20 years. 
What would I love to see? I think I would love to see a world of work in which organizations — and by that, I mean leaders, managers and people — have learned the major lessons from the major disruptions of the past, which has set them up to be in a better position to cope with and learn from and benefit from the next set of disruptions. A world of work which transitions based on the notion of building back fairer, and those are Michael Marmot’s words. 
And against a backdrop such as this, when we confront a question of this nature in terms of what will the world of work look like with these enormous changes, what we tend not to think of and what is equally important is what likely won’t have changed. And if we look over the last many decades, even maybe centuries, I think we can predict that human nature will remain the same. People will still be crying out for high quality leadership, for autonomy, a sense of belonging, for fairness, for growth and development, for meaning and safety. So I think the challenge will be, how can we ensure that no matter what our work looks like, that we can still be providing people’s needs. 
So I hope that my grandchildren will get to experience a world of work in which compassionate, fair minded, wise leaders and decision makers have learned the lessons available to them over the past century and the past few years, and have built workplaces in which everyone, including those people who have historically been excluded from the workplace in so many ways, get to be able to love their work just as much as I love mine. 
**3:36: AM**: I wonder how the working world looked to you when you started out. I think it was in the late seventies, early eighties. 
**JB**: So it certainly was different but it was different in some ways. And there are lessons that I think can help us today. 
So I’ll come out with this. I started working in the mid 1970s, and I remember lining up every second Friday to receive my paycheque. I remember in the early seventies being a student when handheld calculators became available. I remember the panic on university campuses about how this would allow cheating, and isn’t that reminiscent of what we’re going through right now? And that has prepared me in a way that I wouldn’t have thought back then. 
What happened back then is that for quite a while we were almost paralyzed as to what to do. But after a while, universities integrated the notion that you had this technology into the way they taught, the way they assessed. And I think that education benefited dramatically. I think the amount of time that we’re going to be, let’s just say, kind of panic stricken is going to be much shorter. Things happen much faster now. 
I think we are soon going to integrate the new forms of artificial intelligence into the way we learn, the way we teach, the way we work. And I’m far more comfortable now being able to say, I think we’ll benefit because I went through a previous jolt of the same nature. 
**5:22: AM**: You’re getting me to remember how I was writing stories on a typewriter, on electric typewriters. It was a bit of a leap, but that did shape the way I wrote. 
**JB**: Absolutely. And just to go back to the same theme, so showing my age, I typed my master’s thesis on a manual typewriter. And one of the changes that I think is most apparent is the editing job that we did was far more perfunctory because if you wanted to change something on the first page of a chapter, you had to retype the entire chapter. So you’re far less likely to make the changes you needed to change because it didn’t make sense. 
So what I’ve learned is the quality of our work, the quality of our learning has just increased dramatically because of simple changes in technology year by year. 
**6:25: AM**: In your book, you list seven characteristics of productive, healthy and safe workplaces. And I will list them right here: leadership, autonomy, belonging, fairness, growth, meaning and safety. And we spoke about some of these in this series. I presume you’ll say that leaders don’t need to work in all areas at once, but I’m going to put you on the spot. If you’re moving into a toxic or broken work environment, and you’re in a position to be a force for good, where would you start? 
**JB**: Not surprisingly that has to be one of the most frequent questions that I get. And at this stage, I don’t think there’s any indication from research that would suggest that we start with belonging versus growth or whatever. 
So given that there’s no research or evidence-based answer to this, if you pushed me, I would start with leadership development. And not because there’s any sense that leadership or leadership development would have a better, quicker, faster payoff than any of the others. But I think if you have to start somewhere, it can’t hurt starting with leadership. 
If you start with leadership development, one of the indirect medium-term benefits is we know that it’s going to help employees experience more meaning, safer workplaces, higher levels of performance and so forth. And I think it’s leaders who will decide in their own contexts what makes most sense. Is it belonging, autonomy, growth and so forth? 
I actually don’t believe that even when the research does exist, hopefully one day, that we’ll have an answer that is definitely one. I think it’s going to be more contextual than that. 
**8:30: AM**: Now, one of the themes of our conversations is that the term workplace has almost become anachronistic. The workplace is a spare bedroom or the corner of a local Starbucks. If one values well-rooted relationships at work — and I’m not talking about the work spouse here but good relationships that are good for effective teams or even for one’s own’s sake — how are we going to build and nurture those relationships? Have you seen any employers who have a response to this challenge? 
**JB**: If we just take a broader perspective to start off with this. On the one level, the scope of the problem is immense. So just when you mentioned the term workplace, I think that this raises such large questions. When we had the discussion about safety, can safety inspectors enter your home if that’s the workplace? 
Here is another challenge. As we allow remote work, what happens if the organization that employs you is located in Toronto and you live in New Zealand — where do you pay tax? I think that is an enormous issue, but I think we have to then go down to the interpersonal level. What happens if somebody’s working in New Zealand and somebody’s working in Toronto? 
And I think the issues, the challenges that are before us are really the same. How do we encourage high-quality working and interpersonal relationships? It’s the smallest things that are going make the biggest difference. I think right now many of us are stuck in the notion of what are the biggest things we can do to enhance those relationships. Ask people what they want themselves, provide the opportunities that they are suggesting, provide opportunities for relationships. I think we are going to get there. 
Again, to get back to a comment by Sarah Kessler, I’ve mentioned before, we’ve been worrying about the end of work for 500 years. Work doesn’t change that much. So I think that we should stop thinking about this in terms of grandiose things like the workplace has changed. Relationships remain relationships. 
**11:12: AM**: I was surprised slash not surprised by your citing of an estimate in your book that only one per cent of HR managers deliberately use research-based knowledge to guide their everyday workplace decisions. And that probably explains why we still see forced ranking systems, performance management, stock options for motivation and other kinds of tactics for which the evidence is scanty or non-existent. If managers want to be guided by evidence rather than by fad or inertia, what can they do? 
**JB**: That’s a really important question right now as we enter into somewhat of a difficult economic time. I’d like to add one fad that we are seeing that is just not guided by evidence, that perhaps goes against evidence. And that is we are seeing more layoffs in high tech companies guided by the almost anachronistic notion that you can shrink yourself back into excellence. 
So there is so much blame to go around in terms of only one per cent of decisions being guided by evidence. What I want to do is focus on the source of the problem rather than the end user. And the source of the problem is ourselves — the academics who produce the research. I think historically we’ve never been that great at sharing knowledge. The very term ivory tower I think accurately describes historically not just how we’ve been seen, but how we want to work in a hierarchical tower that’s separated from everybody else. 
And historically faculty in these ivory towers were almost looked down on by others in ivory towers if they did make knowledge translation and knowledge share sharing a priority, and I think this was true as recently as 20 to 25 years ago. As an example of this, I would still actively discourage managers from reading most of our academic journals because of the way in which articles are still written. I cannot understand articles that are written in areas that are, if I can put it this way, pretty adjacent to my own. I just won’t be able to get it. 
But I think we are seeing change. I think we are entering into an era where the link between people that produce the research and people that hopefully will use the research is becoming far closer. Just as some examples: the Academy of Management that produces some of the most prestigious journals in the area have a podcast series where authors are encouraged to do a podcast on their research that is likely to be accessible to a much larger audience. 
And now, our own school, we have the Smith Insight series that reaches a large group, that translates the research done primarily by people in the school into a way that can be used by other folks. 
Within schools. I think that faculty are being recognized for social impact, which includes things such as directly speaking with organizational leaders and policy makers, which includes directly researching topics that have social impact. 
So I’m optimistic in a way that I probably wasn’t five to 10 years ago that we are beginning to close the distance between the people that produced the research and the people that potentially can use the research. 
**15:26: AM**: On the theme of initiatives that may lack evidence, I spent a few weeks recently going down the rabbit hole of corporate purpose. I researched corporate purpose statements, best practices in operationalizing purpose, the value in motivating employees and stakeholders. To be honest, I still don’t know how I feel about today’s huge interest in corporate purpose. It’s hard to believe it’ll make any difference outside of a handful of organizational unicorns. I wonder, what’s your take? 
**JB**: I hate to sound cynical because I’m not. I think people who know me would tell you that I’m an incurable optimist. But I don’t believe that much will happen because of corporate purpose, vision, mission statements and so forth. I think we’ve all seen how much time, money and the extent of resources that organizations pour into developing these statements. And I think we’ve yet to see a meaningful tangible gain from them. 
People, and I mean people in organizations, peoples’ behaviours are not likely to be guided by words printed over the front door. They’re more likely to be guided by everyday examples set by their leaders. And I would suggest that’s where we need to spend our time, money and resources if we really want meaningful change within organizations. 
If I can give some anecdotal support for this, I would look back to the creation of the remarkably successful Dilbert cartoon character. I am not sure you can pin the emergence of Dilbert onto one factor alone, but if you go back to 1989 when Scott Adams introduced Dilbert, it was a time when organizations were being compelled to introduce mission statements. And a very major theme in those early Dilbert cartoons was your average employee railing against corporate mission statements. And to a large extent, it still is. 
I think we will achieve far more if we bring our focus closer to home and spend more of our time, money, resources and attention into helping our leaders at all levels do the kind of wonderful jobs that they want to do in leading people in organizations. 
**17:57: AM**: Ah yes, wisdom from the school of Dilbert. You’ve written about the importance of addressing some of the gender and LGBTQ discriminatory practices in organizations. And you’ve mentioned that voluntary compliance will likely be how these issues are addressed. What does that look like? And specifically, do you think it’s enough to enact real and lasting change? 
**JB**: Let me start with the term voluntary compliance. Looking at what’s changed over the last decade or two, a decade in which voluntary compliance is almost the mantra of North American organizations, I would have to conclude that it has failed all too many people. 
And just the term, by the way, voluntary compliance is an oxymoron if I ever saw one. As one example, look at the Fortune 500 or Fortune 1000 CEO list. And to what extent has voluntary compliance made a difference? Yes, 2022 is the first year in which we finally have witnessed a situation where more than 10 per cent of CEOs are female. 
But I would have to say that that’s kind of pathetic. Fifty-three out of 500 are now female. And what are we likely to see in 2023? Is that a sustainable change? Are we on an upward direction? After 20, 25 years of going from perhaps five to 10 per cent, how long are we willing to wait? 
So personally, I’m not a fan of voluntary compliance. I think that we have failed too many people, racialized people, indigenous people, people of different religions and so forth. I suspect we’ve reached the point where the dream of compliance with some voluntary targets can be relied upon to bring about change is simply no longer sufficient. I think what we are about to see is activist shareholder groups forcing change upon organizations, and I don’t personally believe there’s anything wrong with that. The experiment has been given enough time to work, and we have failed the notion of voluntary compliance. 
**20:36: AM**: In this series of conversations, we’ve talked about what existing research can tell us about how to build and manage productive and healthy workplaces. I’d like to now flip that around a little bit. What do we still not know about the big issues of leadership, safety, autonomy or meaning that you hope will be addressed in the coming years? 
**JB**: It’s a long list. But if I can share some of the questions that I would love to see answered. 
So in terms of safety, overwhelmingly my contact with many hundreds, thousands of leaders over the last couple of decades, overwhelmingly most managers are really good people who care deeply about their people. And that is something that has sustained me over the decades. How can we help them do the small things differently when they’re legitimately so busy? How can we get them to reappraise risk? If they went to work knowing that action “a” would result in a safety incidence, they would never do it, but they go to work thinking that it can never happen. How can we help people to reappraise risk? 
I think, as I mentioned when we discussed safety, I think changing the language around safety may create more of a change than we think. 
How can we get organizations and societies to care more about leaders’ wellbeing? I think organizations. . . society has done a remarkable job in the last decade or so of being legitimately and justifiably concerned about employees’ wellbeing. And that’s placed even more of an onus and responsibility on leaders. But we’ve forgotten leaders. We expect leaders to be healthy. We expect leaders to be strong. 
So I think until we care more about leaders’ wellbeing, we are simply going to leave them in a position where it becomes more and more difficult for them to care about others’ wellbeing. So it’s simply not about caring about leaders’ wellbeing because they’re the most senior people in the organization. They’re important because they’re people, but unless they’re well, they’re not going to be able to really help others. 
A third issue, I guess, artificial intelligence is coming to an organization near you, and it’s coming sooner than you might think. And in fact, research has already started. I’ve seen papers recently on programming robots to display different leadership styles and evaluating their effects. So if there’s a robot giving instructions, does it make a difference if it uses transformational language? 
**AM**: Robot leaders? 
**JB**: Robot leaders. It might seem like an oxymoron, but I think that it’s not going to be an oxymoron for long. So can we get there before the situation gets past us, if I can put it that way? 
Whatever the changes, however big, I’m comforted by the fact that one thing that will not change overnight, again, is human nature. So people will still be working and adjusting to all these changes. I think the organizations that will thrive in the future are going to be those that still ensure that they satisfy employees needs for good robot leadership, for autonomy, belonging and so forth. So what are the mental health and physical health consequences for being a leader? And why? 
If I can conclude with just a thought taken from a wonderful TED Talk by Itay Talgam, who’s a former orchestra conductor and a current leadership consultant. And his TED Talk is called Lead Like the Great Conductors. And a comment that Talgam has that he counsels us — and this comment has had a great effect on me — if you love something, give it away. And I’m so fortunate to have loved my job since I’ve started working many, many years ago. I’ve been so fortunate to have had work, in a sense, being such an important source of happiness, health and fulfillment to me. 
The challenge for me now is, what can I do to give this away so that the wonderful students, staff and faculty with whom I’ve been privileged to work can be lucky enough eventually to pass that along to their next generation? I would love to be able to answer those questions. 
**AM**: That’s a lovely way to tie up this podcast in a bow. I’ve really enjoyed these conversations, Julian. Thanks so much for sharing your insights. 
**JB**: Thanks for your really thought-provoking questions. 
\[Music playing\] 
**AM**: For more on Julian Barling’s vision of productive, healthy and safe workplaces, pick up a copy of his book, _Brave New Workplace_, from your favourite bookseller. _Brave New Workplace_ is published by Oxford University Press. 
Thank you to podcast producer Meredith Dault and to Bill Cassidy for editing support. Finally, for practical evidence-based insights on the organizational world and business and finance in general, check out Smith Business Insight at smith.queensu.ca/insight.

# [Why Do-Good Gifts May Miss the Mark | Smith Business Insight](https://smith.queensu.ca/insight/content/Why-Do-Good-Gifts-May-Miss-the-Mark.php) 
 _https://smith.queensu.ca/insight/content/Why-Do-Good-Gifts-May-Miss-the-Mark.php_

**It’s mid-December.** You’re sitting at your desk and a new message hits your inbox with the subject line: “A donation has been made on your behalf to…” You feel grateful, of course, but also a little dissatisfied for some reason. This doesn’t quite feel like a gift. 
The ambivalent reaction to a charitable or “prosocial” gift — a cash donation on one’s behalf to a food bank, the symbolic adoption of a species at risk — is not unusual, even as such gifts become increasingly popular. 
Ekin Ok, an assistant professor of marketing at Smith School of Business, credits the rise of prosocial gift-giving to advances in technology that make it a more accessible option. As well, a growing number of people value social responsibility and want it reflected in their consumption decisions. That extends to their gifts. Nearly half of Canadians say they would [prefer to receive charitable gifts](https://www.globenewswire.com/en/news-release/2022/11/22/2560587/0/en/Ipsos-Poll-Nearly-Half-of-Canadians-47-Prefer-to-Receive-Charitable-Gifts-Over-Material-Gifts-This-Holiday-Season.html) over material items. 
That may be great news for professionals who are on the hunt for a gift for a colleague or client, and a welcome opportunity for charitable organizations. But does it deliver the intended warm glow to the person on the receiving end? 
## **The importance of control** 
Ok and fellow researchers Rishad Habib (Toronto Metropolitan University) and Karl Aquino (University of British Columbia) are trying to answer that question. 
The literature on prosocial gift-giving suggests recipients may not always appreciate such gifts as much as givers anticipate. This is particularly true when it comes to gift recipients with whom [they do not have a close relationship](https://www.sciencedirect.com/science/article/abs/pii/S0749597815000771#b0010).
It is generally assumed that the recipient will feel a sense of satisfaction about contributing to something good, Ok explains. Here’s the catch: “We know from research that to feel this moral satisfaction, this feeling of having done good, we need to feel some agency behind the decision.” 
In prosocial gift-giving, gift recipients sometimes are not the ones deciding on the cause or the charity that receives the donation. “Because this type of gift-giving presents limited opportunities for recipients to feel agency behind the donation decision,” says Ok, “our ongoing research provides some preliminary evidence that recipients don’t actually feel that happy about it, especially if they haven’t explicitly asked for this type of a gift or if they haven’t previously communicated their genuine interest in the cause that the donation supports.” 
By “happy,” Ok means “the moral kind of happiness that we often experience after doing something at a cost to ourselves for the benefit of others.” 
Prosocial gift-giving can also have unintended negative effects on charities receiving the donations. While there are benefits from that initial donation, a prosocial gift may not inspire a strong relationship between the gift recipient and the charitable organization. “In some cases, it may even reduce gift recipients’ future willingness to donate to the organization,” Ok says. 
## **How to give a prosocial gift** 
Is there a way to make prosocial gift-giving a win-win-win? 
Ok speculates that, given what is known from current research, if gift-givers were to choose an organization that made the recipient feel as if they inspired the choice, that could thwart negative effects resulting from a lack of agency in the decision-making process.
“Let’s say I’m crazy about dogs. I talk about dogs all the time and everyone who knows me knows that I love dogs,” Ok says. “If a friend chose an animal rescue organization to donate to on my behalf without my prior knowledge, I would still feel somewhat responsible for having inspired that choice.” 
Another option for charitable organizations is to put more power into the hands of the gift recipient. Charities can do this by allowing gift recipients to determine how the donation is used. 
Ok says one of their studies shows that allowing the recipients to direct the gift to a specific area, fund, program or initiative will make them feel more involved in the process and increase their sense of moral satisfaction. 
“The idea of agency, or feeling personally responsible, is important when it comes to moral decisions like this,” says Ok, “because we know one of the reasons people act charitably is to help others, but it also helps us feel good about ourselves.”
Tags:

# [Our Insight Topics | Smith Business Insight](https://smith.queensu.ca/insight/tag.php?tid=Finance) 
 _https://smith.queensu.ca/insight/tag.php?tid=Finance_

 Smith Business Insight - Our Insight Topics 
[Skip to main content](#main-content)
Smith  
* [About](#)
 
 [Smith Home](/index.php)[Profile](/about/index.php)[News](/news_blog/index.php)[The Dean](/about/dean.php)[Strategic Plan](/about/strategic-plan.php)[Equity, Diversity, Inclusion & Indigenization](/about/EDII/index.php)[Learning Environment](/about/learning_environment.php)[Partnerships](/about/partners/index.php) [Services](/about/services.php) [SmithStore _​_](http://smithqueens.com/smithstore) [Queen's University _​_](https://queensu.ca)
 
* [Learning](#)
 
 [Explore Our Programs](/academic_programs/index.php)[Undergraduate Programs](/academic_programs/undergraduate.php) [MBA Programs](/mba_programs/index.php) [Graduate Programs](/grad_studies/index.php) [Executive Education](/executiveeducation/index.php)[Certificates](/academic_programs/certificates.php)[International](/international/index.php)[SmithEdge](/smithedge/index.php)[Academic Integrity](/about/academic_integrity/index.php)
 
* [Insights & Research](#)
 
 [Smith Business Insight](/insight/index.php) [Research](/research/index.php) [Publications](/about/publications.php) [Centres](/centres/index.php)
 
* [Faculty](#)
 
 [Meet Our Faculty](/faculty_and_research/faculty.php) [Join Our Ranks](/faculty_and_research/Join_Our_Ranks.php)
 
* [Alumni & Giving](#)
 
 [Give to Smith](https://smith.queensu.ca/invest/) [Alumni](/alumni/index.php)
 
* [Recruit & Engage](#)
 
 [Recruiting](/recruiting/index.php) [Partnerships](/about/partners/index.php) [Work with Students](/engage/index.php) [Smith Business Consulting](/centres/business-consulting/index.php)
 
Fresh ideas from [Smith School of Business](/index.php)
* [Topics](#)
 
 ### Categories
 
 * [Leadership](/insight/sections.php?sid=Leadership)
 * [Teams](/insight/sections.php?sid=Teams)
 * [Diversity](/insight/sections.php?sid=Diversity)
 * [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
 * [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
 * [Social Impact](/insight/sections.php?sid=Social%20Impact)
 * [Marketing](/insight/sections.php?sid=Marketing)
 * [Strategy](/insight/sections.php?sid=Strategy)
 * [Finance](/insight/sections.php?sid=Finance)
 
 ### Collections
 
 * [Our Emotions at Work](/insight/collection/Our-Emotions-at-Work.php)
 * [Speaking of Economics](/insight/collection/Speaking-of-Economics.php)
 * [The Age of Corporate Purpose](/insight/collection/the-age-of-corporate-purpose.php)
 * [How To Make Hybrid Work](/insight/collection/how-to-make-hybrid-work.php)
 * [All Collections](/insight/collections.php)
 
 ### Subscribe to Our Newsletter
 
 Cutting-edge research and expert advice delivered straight to your inbox.
 
 [Subscribe](/insight/newsletter.php)
 
* [Webinars](/insight/webinars.php)
* [Podcast](/insight/podcast/index.php)
* [Videos](/insight/video.php)
* [About](/insight/about.php)
Search
# Finance
## [How Catfish Effects Drive Stock Market Reform](/insight/content/How-Catfish-Effects-Drive-Stock-Market-Reform.php)
Competitive financial analysts from abroad force their domestic counterparts to up their game
## [Why Partisan CEOs Wear Rose-Coloured Glasses](/insight/content/Why-Partisan-CEOs-Wear-Rose-Coloured-Glasses.php)
When their favoured president is in the Oval Office, chief executives issue overly optimistic forecasts
## [Your Firm’s Most Undervalued Asset? Try Nature](/insight/content/Your-Firms-Most-Undervalued-Asset-Try-Nature.php)
Too few businesses understand the value of biodiversity — to the planet and their competitiveness
## [What Car Loans Can Teach Us About AI](/insight/content/What-Car-Loans-Can-Teach-Us-About-AI.php)
Research on car dealerships shows how artificial intelligence can boost profits and help more people get a car
## [The Hidden Message in What Executives Say](/insight/content/The-Hidden-Message-in-What-Executives-Say.php)
Discover the role of vocal cues in investor decision-making
## [A Guide to Social Impact Investing](/insight/content/A-Guide-to-Social-Impact-Investing.php)
Emerging business models are reshaping traditional finance for the common good
## [Consumer Credit Assessment in the Age of Big Data](/insight/content/Consumer-Credit-Assessment-in-the-Age-of-Big-Data.php)
Technology is adding a twist to the creditworthiness game. The good news: it may improve financial inclusion
## [On Proxy Overload and Biased Ballots](/insight/content/On-Proxy-Overload-and-Biased-Ballots.php)
How corporate governance can be undermined when shareholders and their advisors can’t keep up
## [Climate Impact Disclosure Gets Real](/insight/content/Climate-Impact-Disclosure-Gets-Real.php)
New regulations and accounting standards will give investors a truer picture of corporate sustainability
## [Can Investing Drive Social Impact?](/insight/content/Can-Investing-Drive-Social-Impact.php)
We talk with an expert on what happens when private capital does public good—and expects a return
## [Tracking the Rise of Zombie Companies](/insight/content/Tracking-the-Rise-of-Zombie-Companies.php)
The last 30 years have been good for the corporate walking dead. But for how much longer?
## [The Indigenous Impact Opportunity](/insight/content/The-Indigenous-Impact-Opportunity.php)
Big projects get the splash but impact investors see upside in funnelling capital into small Indigenous businesses
[Load More](#)
## Editor’s Picks
1. [The New Rules of Public Speaking](/insight/content/The-New-Rules-of-Public-Speaking.php)
2. [The Untapped Potential of Customer Loyalty Plans](/insight/content/The-Untapped-Potential-of-Customer-Loyalty-Plans.php)
3. [How to Build Trusted Brands](/insight/content/How-to-Build-Trusted-Brands.php)
4. [How Catfish Effects Drive Stock Market Reform](/insight/content/How-Catfish-Effects-Drive-Stock-Market-Reform.php)
[Topics](#nav-menu-topics)
* [Leadership](/insight/sections.php?sid=Leadership)
* [Teams](/insight/sections.php?sid=Teams)
* [Diversity](/insight/sections.php?sid=Diversity)
* [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
* [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
* [Social Impact](/insight/sections.php?sid=Social%20Impact)
* [Marketing](/insight/sections.php?sid=Marketing)
* [Strategy](/insight/sections.php?sid=Strategy)
* [Finance](/insight/sections.php?sid=Finance)
[Collections](/insight/collections.php)
[Webinars](/insight/webinars.php)
[Podcast](/insight/podcast/index.php)
[Videos](/insight/video.php)
[About](/insight/about.php)
## Kingston
Goodes Hall 
Queen's University 
Kingston, Ontario 
Canada K7L 3N6
[1.877.533.2330](tel:+18775332330)
## Toronto
Simcoe Place 
200 Front Street West 
30th Floor
[416.365.7141](tel:+14163657141)
## Smith Programs
* [Undergraduate Programs](/academic_programs/undergraduate.php)
* [MBA Programs](/mba_programs/index.php)
* [Graduate Programs](/grad_studies/index.php)
* [Executive Education](/executiveeducation/index.php)
## Directories
* [Contact Us](/about/contact.php)
* [Smith Centres](/centres/index.php)
* [Smith Services](/about/services.php)
## Connect with Smith
* [Facebook](https://www.facebook.com/smithbusiness)
* [Instagram](https://www.instagram.com/smithbusiness/)
* [Twitter X](https://twitter.com/smithbusiness)
* [Linkedin](https://www.linkedin.com/company/smith-school-of-business-at-queen's-university)
* [WeChat](https://mp.weixin.qq.com/s/SoosIZFmLD0D01aSGJzgLw)
The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.
* [Give to Smith](/invest/ "Give to Smith")
* [Careers](/about/careers/ "Careers at Smith")
* [Program Portals](/academic_programs/student-portals.php "Program Portals")
* [Privacy](http://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy")
© Smith School of Business

# [Smith School of Business - Year in Review - Exploring Analytics](https://smith.queensu.ca/yearinreview/2018-2019/stories/exploring-analytics.php) 
 _https://smith.queensu.ca/yearinreview/2018-2019/stories/exploring-analytics.php_

Faculty Research
## **Anton Ovchinnikov** 
_Associate Professor and Distinguished_ 
_Professor of Management Analytics_
Analytics, broadly defined, is the use of math and data to improve decision making. Why does analytics matter? Because “better decisions improve lives,” says Smith Professor Anton Ovchinnikov.
Analytics is part of Anton’s research, and his work contains useful insights for businesses. Consider customer analytics for example; Anton has done several studies in this area. In one, he and INSEAD professor So Yeon Chun analyzed the design of loyalty programs. They noticed companies were placing spending requirements on their programs, causing some customers to alter how they spent (in order to maximize points collection). The researchers wanted to know: Do companies really earn higher profits with such loyalty-program designs? And do customers necessarily lose out? Their research revealed win-win scenarios that allow both companies and customers to benefit.
“The key managerial question of the next decade is how to make humans and AI work better together.”
Anton joined the faculty at Smith in 2014 from the University of Virginia. He grew up in Siberia and earned his PhD in operations management at Rotman in Toronto. His work is published in top journals including _Management Science_ and _Operations Research_.
Today, Anton is especially interested in how artificial intelligence and machine learning affect decision making within organizations. “The key managerial question of the next decade is how to make humans and AI work better together,” he says. That includes ethical considerations. Will decisions made by machines be fair or will they discriminate?
In another study, Anton and Smith PhD student Stephanie Kelley examined existing anti-discrimination laws and AI decision making in financial services. Their research showed that the data governance policies prescribed by U.S. and European Union laws could lead to significant decreases in access to credit for women.
“Artificial intelligence will force us to rethink many aspects of how societies work,” says Anton. Researchers like Anton are working to understand how people will interact with AI systems and ensure the decisions that result help make lives better, not worse.

# [Empowering Women in Global Mining | Smith Business Insight](https://smith.queensu.ca/insight/content/Empowering-Women-in-Global-Article.php) 
 _https://smith.queensu.ca/insight/content/Empowering-Women-in-Global-Article.php_

**If you’re concerned that minerals** inside your phone or laptop fund armed conflicts, you should be, says Shengwen Li, a PhD candidate at Smith School of Business. But she says there’s another reason to care about the source of these metals: gender discrimination.
It’s no secret that some consumer products are packed with metals mined in developing countries such as the Democratic Republic of the Congo (DRC) that finance armed groups in those countries. Most of the extraction activities are considered “artisanal mining” — a form that is labour-intensive and informal and that often uses basic extraction tools like pans and hand shovels.
Less known, however, is that while millions of women find subsistence employment in artisanal mining, gender discrimination, economic instability and gender-based violence [are rampant in the sector](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/6913dd84795c217cc1c8c05358d8e782/asset-v1:SDGAcademyX+NR001+2T2019+type@asset+block/Women_and_artisanal_mining_-_gender_roles_and_the_road_ahead.pdf).
The multinational corporations behind some artisanal mining don’t help the situation, says Li. “They often reinforce these gender divisions of labour, leveraging gender discrimination to minimize production costs through global sourcing. And so female workers frequently find themselves trapped in a poorly paid job or insecure working conditions.”
All is not lost. As Li and [Anthony Goerzen](https://smith.queensu.ca/faculty_and_research/faculty_list/goerzen-anthony.php), Sobey Professor of International Business at Smith, reveal in a [new study](https://www.sciencedirect.com/science/article/pii/S1090951624000178), two types of third-party interventions can go a long way towards ensuring gender equality in artisanal mining, the first link in a high-stakes global value chain.
**NGO with impact**
Li and Goerzen came to this conclusion after taking a deep dive into a project launched by the Canadian-based non-governmental organization [Impact](https://impacttransform.org/en/) in 2017 in Ituri, a province in eastern DRC. Ituri is rich in gold deposits but its artisanal mining sector deals with severe challenges, including interference by armed groups and an overwhelmingly macho mining culture.
Impact’s project, known as the Village Savings and Loan Association, invited women and men from across Ituri to join the association and make weekly contributions to savings pools. Members then decided where to direct the loans to fellow VSLA members. The initiative focused on enhancing financial and employment opportunities, promoting female leadership and fostering inclusion for all artisanal miners and community residents.
Li and Goerzen were curious to know the impact the VSLA had on women’s inclusion and empowerment and, more importantly, what drove that impact.
“So many interventions from NGOs or multinational companies or governments are practically driven, which means they often lack the robust and theoretical foundations to explain the mechanisms behind the interventions,” says Li. “That’s why sometimes they lead to inconclusive results or varying effects across different contexts. We didn’t want that.”
When they looked at the VSLA’s track record closely, they identified two strategies that led to more women being included in mining activities and feeling empowered.
One, known in academic circles as a “conversion” intervention, doesn’t change existing norms in a community but leverages the ambiguity in them to promote gender equality. In Ituri, husbands wouldn’t generally allow their wives to be involved in a project such as a VSLA, but because it provided financial and employment opportunities to households struggling with poverty, the men tended to allow women to participate.
The other strategy, called a “layering” intervention, is similarly subtle in that it doesn’t change existing community norms but adds new ones. In Ituri, men don’t typically allow women to be in decision-making roles, but the VSLA was purposely designed with new guidelines to promote female leadership. From surveying participants, Li and Goerzen found that this layering approach made women feel empowered and that it promoted both economic and attitudinal changes among men and women.
**Lessons for policymakers and managers**
There are a few big lessons to take away from these findings, says Li. And they can be applied to almost any sector where global supply chains rely on a workforce that is fundamentally unequal.
For one, Li says policymakers must do a better job of understanding the nature of local institutional arrangements. They must also be aware of the unintended consequences of different interventions and know the nuances of what female empowerment can mean.
“Take this VSLA, for instance, which was funded by the Canadian government,” says Li. “They stopped that funding after a couple of years. What we found was that after that funding ended, the effects of the project on women’s empowerment were no longer statistically significant.”
This doesn’t mean the VSLA failed, she adds, but that it would likely take a lot longer than a couple of years for female empowerment on a household and community level to be more fully realized through a similar project.
For multinational corporations, Li says the lesson is simple: if you’re part of global supply chains where gender discrimination is rampant in the first link of the chain, you can’t bury your head in the sand.
“Just because your corporation is not directly involved in such issues doesn’t mean those issues aren’t caused by your strategies,” she says. “So instead of ignoring the problems or withdrawing your presence in these high-risk regions, you have to develop a more gender-sensitive approach. Maybe this means collaborating with NGOs who have more resources on the ground, who have access to the local communities, and who have a capacity and expertise in dealing with these issues.”
Tags:

# [Home](https://smith.queensu.ca/about/EDII/index.php) 
 _https://smith.queensu.ca/about/EDII/index.php_

Smith School of Business is committed to cultivating a vibrant, diverse and inclusive academic and work environment rooted in a culture of mutual respect and equity such that all members of our community feel safe, possess a strong sense of belonging, and are empowered to thrive.
## Our Commitment
Smith School of Business is committed to cultivating a vibrant, diverse and inclusive academic and work environment rooted in a culture of mutual respect and equity such that all members of our community feel safe, possess a strong sense of belonging, and are empowered to thrive. Through intent and action, we must eliminate all forms of racism, discrimination and harassment that have perpetuated inequities in our environment, the curriculum, our research and in administrative operations.
_​_
### Building Diversity
Introducing policies and practices to increase access and inclusion for underrepresented groups — including BIPOC communities, members of the 2SLGBTQ+ community, persons with disabilities, and women — among undergraduate and graduate student bodies, staff, faculty, administrators and advisory boards.
_​_
### Education & Training
Incorporating education and training to enable members of our community to recognize, acknowledge and address systemic racism and the unconscious biases that each of us holds into the onboarding of new students, staff and faculty members and into the professional development of others.
_​_
### Fostering Inclusion
Supporting the success of our community members by: fostering open and respectful dialogue; ensuring the voices and perspectives of those from marginalized communities are sought, presented, amplified and valued; and integrating EDII considerations into all aspects of life at Smith.
## Queen’s-wide Declaration of Commitment to Address Systemic Racism
Principal Patrick Deane released a declaration, on behalf of the university’s administration, to address racism — systemic as well as individual. All members of the senior leadership endorsed the declaration as a signal of their commitment to take action to root out the causes of racism within the university and to ensure that those who experience racism and related forms of injustice are treated equitably and are able to participate in the life of the university, fully and authentically.
[View the declaration](https://www.queensu.ca/gazette/stories/declaration-commitment-address-systemic-racism)
## Smith EDII Strategy & Action Plan
Smith has established a detailed EDII Strategy & Action Plan to guide its actions, define targets, and measure progress. Our goal is for Smith to be an inclusive community of purpose that strives for excellence, integrity, and impact on a global stage by upholding the values and principles of EDII.
[Detailed plan](https://smith.queensu.ca/about/EDII/PDF/StrategyAndActionPlan-Detailed.pdf) [One-page overview](https://smith.queensu.ca/about/EDII/PDF/StrategyAndActionPlan-Overview.pdf)
## EDII Resources
Find out more about Queen’s commitment to advancing EDII across the University.
_​_
### EDII at Queen’s
Get more information about EDII efforts, resources, and the latest EDII news at Queen’s.
[Learn more](https://www.queensu.ca/vpcei/)
_​_
### Human Rights & Equity
The Human Rights & Equity Office is an inclusive community that values, respects, and celebrates the dignity and worth of every person.
[Visit HREO](https://www.queensu.ca/hreo/)
_​_
### Contact Us
Connect with the various services and resources provided by the Human Rights & Equity Office.
[Get in touch](https://www.queensu.ca/hreo/contact-us)

# [Search | Smith Magazine](https://smith.queensu.ca/magazine/search.php) 
 _https://smith.queensu.ca/magazine/search.php_

 Search | Smith Magazine | Smith School of Business 
 
* [Current Issue](index.php)
* [Archive](issues/index.php)
* [Alumni Notes](alumni-notes-index.php)
* [Startups](startups-index.php)
* [Search](search.php)
[Skip to main content](#main-content)
 
* [Current Issue](index.php)
* [Archive](issues/index.php)
* [Alumni Notes](alumni-notes-index.php)
* [Startups](startups-index.php)
* [Search](search.php)
# Search
Enter your keywords Use up and down arrows to select available result. Press enter to go to selected search result. Touch devices users can use touch and swipe gestures.
## Smith Programs
* [Bachelor of Commerce](../bcom/index.php)
* [MBA Programs](../mba_programs/index.php)
* [Graduate Programs](../grad_studies/index.php)
* [Executive Education](../executiveeducation/index.php)
## Smith Websites
* [Smith School of Business](../index.php)
* [Invest in Smith](../invest/index.php)
* [Smith Business Insight](../insight/index.php)
* [Program Portals](../academic_programs/student-portals.php)
## Get Connected
* [Facebook](https://www.facebook.com/SmithBusiness/)
* [Twitter](https://twitter.com/smithbusiness)
* [Instagram](https://www.instagram.com/Smithbusiness/)
* [LinkedIn](https://www.linkedin.com/company/smith-school-of-business-at-queen's-university/)
**© Copyright, Queen’s University** 
Smith Magazine is published twice annually by 
The Stephen J.R. Smith School of Business 
at Queen’s University.
* [Update your Queen's Profile](https://apps.adv.queensu.ca/forms/biographic/)
* [Send an Alumni Note](send-alumni-note-update.php "Send an Alumni Note Update")
* [Submit your New Venture](newventures.php)
* [Contact Us](contact-us.php "Contact Us")
* [Privacy](http://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy")

# [Class Recognition](https://smith.queensu.ca/invest/class-giving/class-recognition.php) 
 _https://smith.queensu.ca/invest/class-giving/class-recognition.php_

The Smith School of Business Class Giving Wall recognizes the remarkable commitment, generosity and participation of our top classes. Classes with cumulative gifts of $100,000 or more received will also be recognized in the Lifetime Giving section.
**Scroll image to view the wall**
**We have also created an area on the wall to recognize our exceptional classes in the following categories:**
* **Graduating Class Gift:** Recognizes the graduating classes that gave the largest cumulative gifts between September 1st of their last year until June 30th (post-graduation). This excludes any giving to the Goodes Hall student pledge.
* **Student Participation:** Recognizes the graduating classes with the highest rate of participation between September 1st of their last year until June 30th (post-graduation). This excludes any giving to the Goodes Hall student pledge.
* **Lifetime Participation:** Recognizes the classes who have cumulatively given the most to Smith School of Business. This is based on all gifts designated to our school and donations are counted towards the preferred year (unless otherwise requested).
* **Class Endowed Funds:** Recognizes the three largest endowed class funds based on the capital balance of the account updated April 30th each year.
* **Lifetime Giving - First Decade:** Recognizes the three classes that raised the most for Smith School of Business in the 10 years following graduation. This counts all gifts and pledges allocated to Smith School of Business.
* **Planned Giving:** Recognizes the classes who have thoughtfully remembered Smith School of Business through a provision in their will or other future gift arrangement involving life insurance, a trust or registered retirement savings. This plaque displays the class with the highest participation rate in establishing planned gifts.
_\*Wall updated as of October 2018_
_\*All counting is based on Preferred Degree_

# [Un-Prideful Laws Send the Wrong Signals | Smith Business Insight](https://smith.queensu.ca/insight/content/The-Impacts-of-Anti-LGTBQ-Legislation.php) 
 _https://smith.queensu.ca/insight/content/The-Impacts-of-Anti-LGTBQ-Legislation.php_

**It is Pride Month,** a time associated with all things in celebration of the LGBTQ+ community. Usually it is a bright and hopeful four weeks, and no doubt will be again this year. Still, it is tough to ignore that big legislative shadow darkening the festivities.
Since the beginning of 2023, [more than 500 bills](https://www.aclu.org/legislative-attacks-on-lgbtq-rights-2024) have been tabled in the U.S. that the American Civil Liberties Union call “anti-LGBTQ+”. Almost 40 have been signed into law so far. Some ban gender-affirming care or make it illegal for teachers to talk about gender identity and sexual orientation in class. Others allow the intentional misgendering of transgender and non-binary people.
Canada has not been immune to a similar, albeit more limited, legislative action. In Alberta, Premier Danielle Smith has proposed restrictions for youth seeking gender-affirming care. She has also introduced rules similar to those in New Brunswick and Saskatchewan that would require teachers to get parental consent before changing the names or pronouns of students under 16.
Such initiatives by lawmakers have a wide impact. As Smith School of Business Professor of Equity and Inclusion Eddy Ng has seen, the sentiments behind these types of laws can spill over into the wider culture, including the workplace. Now all of a sudden it might not be so rare to hear a co-worker casually using the f-word or your boss parroting a comedy podcaster’s most recent transphobic rant. “These laws help signal that it’s OK to discriminate,” says Ng.
They can also be a signal for LGBTQ+ workers to find employment in fields that tend to support their way of life. As Ng’s research shows, [LGBTQ+ job seekers tend to gravitate to public and non-profit sectors](https://onlinelibrary.wiley.com/doi/abs/10.1111/capa.12039) because these fields are seen as safe havens. 
**The hit on health**
The price for people who work outside those safe havens may involve having to conceal who they truly are. “If you’re somewhere you feel devalued and stigmatized, you’re probably going to try to engage in some type of identity management,” says Ng. “That creates a cognitive burden, and it can be really detrimental to yourself and your career.”
That cognitive load can be especially detrimental to one’s mental and physical health. Ng was recently part of a team of 13 researchers looking into past studies on the health impacts of anti-LGBTQ+ legislation. While none of the findings were necessarily surprising on their own, Ng says it was sobering to see them anthologized together.
You can read that [anthology](https://link.springer.com/article/10.1007/s41542-024-00174-2) in the journal _Occupational Health Science_, but the short of it is that the researchers uncovered reams of [evidence linking the stress caused by these types of laws](https://journals.scholarsportal.info/details/15538605/v15i0003/329_lcaalmhcaas.xml&sub=all) to increased rates of anxiety, depression, suicidal thinking and other psychological distress in the LGBTQ+ community. They also found evidence for [increases in mental health conditions](https://pubmed.ncbi.nlm.nih.gov/19833997/) such as generalized anxiety disorder and post-traumatic stress disorder.
There can be physical consequences to this legislative stress as well. Chronic stress can result in an [accumulation of physiological strain](https://psycnet.apa.org/record/2021-57225-001) for LGBTQ+ individuals. Systemic inflammation is a driver of health disparities among sexually-diverse and gender-diverse people.
But as the researchers point out, the LGBTQ+ population is not homogenous when it comes to work-related health challenges. Bisexual men, for instance, have [reported](https://pubmed.ncbi.nlm.nih.gov/31659745/) more discrimination at work, more stress and more substance abuse and psychological distress than bisexual women. People who are transgender have been [found](https://www.researchgate.net/publication/348247375_Transgender_Employees_Workplace_Impacts_on_Health_and_Well-Being) to be the most violently, physically and psychologically targeted in the workplace.
Knowing these differences matters, says Ng, because it can help shape how organizations respond to the health needs of their different employees. 
**Where to start**
In general, though, Ng says corporate efforts should begin with comprehensive workplace non-discrimination policies. This may seem obvious, he adds, but it is important because clear rules and clear consequences put everyone on the same page. And as research indicates, such [policies enhance perceptions of job safety](https://onlinelibrary.wiley.com/doi/full/10.1002/smj.3340) and security. 
Evidence also shows that LGBTQ+ employee resource groups (ERGs) can be highly [effective for creating more inclusive workplaces](https://www.researchgate.net/publication/320368709_The_case_for_employee_resource_groups_A_review_and_social_identity_theory-based_research_agenda). ERGs provide safe spaces for LGBTQ+ employees to get together, discuss their experiences and work on diversity and inclusion initiatives for their organizations. “These are really critical because they allow people to speak about their experience without judgment and find strategies for countering some of the things they’re experiencing,” says Ng.
Diversity training can be another essential tool. Certain training strategies have been shown to be more effective than others — [like combining diversity skills and awareness](https://pubmed.ncbi.nlm.nih.gov/27618543/). The key is to focus on squashing stereotypes, says Ng. “Oftentimes people don’t know what they don’t know, and their stereotypes can be at the root of a lot of the discrimination we see. So having that training can help bring those stereotypes out and create awareness about how unfounded they are.”
Diversity training can also develop allies within organizations who are willing to stand up for their LGBTQ+ co-workers. It is most helpful if these allies are from the groups typically engaging in discrimination, says Ng. “Think about it: If I’m a stigmatized person without a voice and somebody attacks me, I’ll probably just stay silent. But somebody with that legitimacy, that clout who says, ‘Hey, that’s not acceptable behaviour,’ carries a lot more weight.” 
The moral of the story here is for employers and allies to stay vigilant, Ng says. The recent wave of anti-LGBTQ+ legislation signals that there are, as he puts it, “intolerance pockets” throughout society, including in workplaces. “And so organizations need to know that they can actually have a lot of influence on ending this intolerance. They can’t stay silent. They have to stand up and say what’s not acceptable, that one’s identity is not a barrier but that one’s uniqueness adds to the organization.”
Tags:

# [Reading the CEO's Mind on Diversity | Smith Business Insight](https://smith.queensu.ca/insight/content/Reading-the-CEOs-Mind-on-Diversity.php) 
 _https://smith.queensu.ca/insight/content/Reading-the-CEOs-Mind-on-Diversity.php_

CEOs have powerful leverage to drive organizational change around diversity and inclusion—if they choose to use it. So far, it has been a mixed bag. Even for leaders out front on the issue, it’s a challenge to convert good intentions to new realities in offices and on shop floors. Too often, responses are short term and reactive to explosive events rather than long term and systemic.
Following these trends closely is [Eddy Ng](https://smith.queensu.ca/faculty_and_research/faculty_list/ng-eddy.php), Professor of Equity and Inclusion at Smith School of Business. Ng has researched [how CEOs signal their priorities](https://digitalcommons.bucknell.edu/fac_journ/1714/) and mobilize staff to implement diversity management. In this conversation with Smith Business Insight, he discusses what he has learned. 
## **On issues relating to diversity and inclusion, there seems to be a disconnect between words coming out of the C-suite and actions within organizations. What explains this disconnect?**
In organizations, the people charged with implementing diversity, or any HR policy, are managers, not senior executives. But CEOs are important for substantive and symbolic reasons. They set the corporate agenda, they devote time and resources. At the CEO level, they hear far more noise from the environment. They can’t deal with everything, so they classify issues into opportunities and threats. Things that are not opportunities or threats, they ignore.
Managers have a lot of discretion on whether and how to implement organizational policies and practices. They may hear their CEO say something \[about diversity\] but conclude that the CEO didn’t really mean it, that public affairs wrote the script. Or they can say, Wait, the CEO is taking this seriously, and we have to take it seriously as well. Managers have a lot on their plate; they pick and choose what’s important.
Our study looked at what CEOs say versus what they do. We surveyed their direct reports—VPs and directors—and asked them to assess their CEOs’ commitment to diversity. Not just what they hear but what they see the CEOs do. And then we studied the outcomes—the amount of diversity policies and practices being implemented.
We found that when HR managers perceived the CEOs to be committed to concrete actions in workplace diversity, it was a stronger predictor of implementation of diversity initiatives. What the CEO says is important, but HR managers have to _perceive_ that the CEO is serious before they implement any of those policies. And CEOs must sustain that effort for HR managers to continue to be committed to diversity. 
## **So CEOs have to buy into the value of diversity or be really good actors.**
Some believe in workplace diversity and some don’t. But for CEOs who don’t believe in the business case for diversity, our study found that if they have strong moral values, which can come from their religion or other places, they are much more likely to display pro-diversity behaviour.
The other part is that younger CEOs may feel they have to prove themselves, so they’re more focused on bottom-line issues. More established CEOs have proven themselves to the board and shareholders, and that’s when their legacy becomes important. There was a study, for example, that found CEOs with daughters tended to act in a much more socially responsible manner. It’s not so much having offspring that matters. It’s more about thinking about the future and making sure their children have equal opportunities. This type of thinking can act as a potential moderator when the belief in the business case for diversity is weak. 
## **How can CEOs signal they are serious about diversity and inclusion in a way that compels managers to actually follow through?**
The only thing that really catches people’s attention is when you hold them accountable, when job performance and compensation are tied to diversity goals. Otherwise, everything is on a best-effort basis.
The most common argument we hear is that there aren’t qualified candidates, or that there’s no one in the pipeline. Managers absolve themselves: Well, we advertised. We hired consulting firms to help us but unfortunately couldn’t find anyone. When their year-end merit bonus is tied to diversity goals, managers expend the effort to make sure those goals are met.
## **If it’s good to tie managers’ compensation to diversity-related goals, why don’t boards do the same for executive compensation?**  
Fair comment, and a lot of boards are starting to do that. But we also have a problem of interlocking boards, where members are CEOs or senior executives from other corporations. It’s a very clubby community. They hang out at the National Club. They avoid these issues because—guess what?—they’re difficult to achieve.
Boards are still generally very white and very male, but there’s institutional and legislative pressure for greater diversity. As we gain a critical mass on boards, it will improve. What’s that critical mass? Not one or two; that’s tokenism. Some studies suggest the magic number is three or four women or other underrepresented groups on the board. That’s when you have greater legitimacy. 
## **Do you sense a greater willingness from senior executives to take the lead on this issue?** 
Historically, diversity never really sat within the umbrella of corporate social responsibility (CSR). When we talked about CSR, it was about safety standards, environmental records, child labour. Now, diversity is part of that rubric. Still, very few Canadian organizations issue a social impact or community report. And it concerns me because diversity and inclusion is still instrumental. Organizations like to put diverse faces on the cover of annual reports, but what does that mean? 
What’s really critical is political leadership. I remember Paul Martin, who was prime minister for a short time, tried to make an impact on Indigenous issues. Had he been in office longer, we would have seen better outcomes. All of us care, but not many of us can have a big impact. To be effective you need resources. Who has those resources? The government and multinationals. They’re the most critical groups.
Tags:

# [Why Is the Public Sector a DEI Laggard? | Smith Business Insight](https://smith.queensu.ca/insight/content/Why-Is-the-Public-Sector-a-DEI-Laggard.php) 
 _https://smith.queensu.ca/insight/content/Why-Is-the-Public-Sector-a-DEI-Laggard.php_

**Recruiters for public service jobs** talk a good game. Sure, the pay may not be as generous as in the private sector, but what about the opportunity to do purposeful work with diverse colleagues? Some government employers, such as the B.C. Public Service, promise that [“diversity, inclusion and respect is at the heart of our work”](https://www2.gov.bc.ca/gov/content/careers-myhr/about-the-bc-public-service/what-the-bc-public-service-offers) — and offer accessibility and inclusion toolkits to ensure everyone feels welcome. 
The sales pitch seems believable. After all, there is a greater expectation that public sector employers will more readily enforce equity policies and anti-discrimination laws than their business counterparts. But does this perception match on-the-ground reality? Should the public sector be considered diversity, equity and inclusion (DEI) standard-bearers?
Eddy Ng says the facts tell a different story. Ng, Smith Professor of Equity and Inclusion, points out that the public sector workforce lags the private sector in minority employee representation. Minority representation in the federal public sector is 2.7 per cent below their labour market availability rate. In comparison, federally regulated private sector employers exceeded the labour market availability rate by five per cent.
What explains the surprising underrepresentation of minorities in Canada’s public services? Ng believes one reason could relate to leadership. His prior research showed that organizational leaders play an influential role in developing diverse workforces. In particular, servant leaders, who focus on employee needs rather than organizational goals, would be expected to shine as DEI overachievers. By definition, they are more likely to invest their efforts in supporting employees, building stronger workplace relationships and enhancing employees’ sense of belonging.
This gave Ng and his colleagues Greg Sears (Carleton University) and Kara Arnold (Memorial University) an idea: Studying the relationship between servant leadership and inclusive practices in both sectors could reveal insights into why public employers don’t seem to be carrying their weight in minority employee representation.
“We wanted to examine whether the pursuit of similar goals by servant leaders could lead to dissimilar outcomes across the two sectors,” says Ng.
## **Servant leaders have a weaker pull in bureaucracies**
[Their study](https://journals.sagepub.com/doi/10.1177/07349149241253726) was based on an online survey of 151 Canadian DEI managers in the public and private sectors. Participants were asked to assess their organizational leaders using a well-validated measure of servant leadership as well as their organization’s implementation of various inclusive practices. They also reported the overall percentage of racial minorities in their organizations and the percentage of racial minorities in management positions.
Once the results were analyzed, the study confirmed what the researchers suspected: Servant leadership led to greater implementation of inclusive practices as well as increased numbers of minorities in organizations generally and, in particular, management roles. 
Ng says this finding signals that “servant leadership may not only help to foster more positive employee attitudes and behaviours, but among senior leaders, servant leadership may influence the formulation of inclusive practices that enhance workplace diversity.”
But the servant leadership story plays out differently depending on the type of organization. To Ng’s surprise, servant leadership was rated higher among private sector versus public sector employers. Further, the positive effect of servant leadership on DEI was noticeably stronger for private employers.
## **Removing institutional barriers**
Ng is unsure why servant leadership is rated lower in the public sector. He says it is possible that servant leader behaviours may be perceived through a different lens within each sector.
As for why servant leadership has a stronger effect on inclusion in the private sector, Ng says business leaders have more room to exercise managerial discretion. Servant leaders in the highly institutionalized public service may be constrained in hiring and promoting minorities and implementing inclusion because of existing rules, unionization or work requirements (think bilingualism or citizenship).
Servant leaders in the public sector may also be up against social expectations, says Ng. In their workplaces, they are often viewed as “bureaucrats” following government directives or advancing political interests. “This unfortunate view of leaders as bureaucrats,” says Ng, “can render servant leaders in the public sector to be perceived as more socially distant, cold, untrustworthy and even out of touch.” With those personas, it’s no surprise servant leaders in the public sector struggle to implement diversity and inclusion initiatives.
Given the structure of the study, the findings offer suggestive inferences rather than causal connections. Ng hopes further research will flesh out some of the insights. But for now, he says, the case is strong enough for public sector organizations to support their servant leaders better. That may involve offering leadership training and development, building a culture that supports servant-leader behaviours and removing institutional constraints where possible.
“Our findings suggest that institutional constraints may limit the potential for servant leaders to exercise agency and mobilize organizational members to make transformational changes,” says Ng. “These constraints can impede the public sector and reform, and limit an organization’s ability to keep pace with private sector organizations.”
Tags:

# [ISF - Taxonomies](https://smith.queensu.ca/centres/isf/resources/taxonomies-resources.php) 
 _https://smith.queensu.ca/centres/isf/resources/taxonomies-resources.php_

## Canada’s Transition & Green Taxonomy for Sustainable Finance
Canada has just taken a major step towards enabling investment in climate change solutions. The Sustainable Finance Action Council (SFAC) has released its [Taxonomy Roadmap Report](https://www.canada.ca/en/department-finance/programs/financial-sector-policy/sustainable-finance/sustainable-finance-action-council/taxonomy-roadmap-report.html). The Institute for Sustainable Finance (ISF) provided research support and is a core knowledge partner on this initiative.
The SFAC report outlines a framework to guide the development of a Canadian Green and Transition Finance Taxonomy. The Canadian Taxonomy will enable businesses and capital providers to credibly identify green and transition projects, and facilitate the further mobilization of capital to support the Canadian economy’s transition towards Net Zero. While many countries and jurisdictions are developing ‘green’ taxonomies, the addition of a transition taxonomy by SFAC is a significant and innovative contribution to the rapidly evolving global taxonomy landscape, and offers an opportunity for Canada to become a closely watched global leader in this space.
We have prepared a briefing note on sustainable finance taxonomies for finance practitioners, industry leaders, policy makers and the general public to learn more about these important issues: [ISF’s Taxonomies Briefing Note](https://smith.queensu.ca/centres/isf/pdfs/Briefing-Note-Report.pdf) (PDF 1.6MB).
## Financial Sector Prioritization Survey
Smart Prosperity Institute surveyed financial institutions about which industries have the greatest potential for allocating capital to green and transition activities, and where a taxonomy will have the biggest impact.
[Financial Sector Prioritization Survey](https://smith.queensu.ca/centres/isf/pdfs/financial-sector-prioritization-survey.pdf) (PDF 1.6MB)
## A Sustainable Finance Taxonomy for Canada
To learn more about SFAC’s approach, how taxonomies are defined and the importance to Canada of a Transition and Green Taxonomy, the ISF’s Executive Director, Sara Alvarado interviewed Barb Zvan, Chair of SFAC’s Taxonomy Technical Expert Group and Chief Executive Officer at University Pension Plan Ontario.

# [Smith joins global responsible leadership alliance](https://smith.queensu.ca/news_blog/2023/Smith-Joins-Global-Responsible-Leadership-Alliance.php) 
 _https://smith.queensu.ca/news_blog/2023/Smith-Joins-Global-Responsible-Leadership-Alliance.php_

_The Council on Business & Society welcomes Canada’s Smith School of Business_
_as first North American member 
_ 
**Kingston, ON** – Smith School of Business is pleased to announce that it has joined a global alliance of business schools dedicated to promoting responsible leadership, research and education.
Recognizing the enormous role business can and must play in helping solve global issues, the Council on Business & Society (the CoBS) brings together leading business schools from around the world to create and disseminate knowledge about these issues and train future business leaders to solve them. Member schools recognize the need for a multicultural approach on global issues, practices and projects, seeking to bring greater value to their students, stakeholders and to the public by combining the strengths of their institutions.
“The CoBS is a global alliance of leading business schools, the members of which are known for their teaching and research excellence and for their meaningful impact on companies and organizations. It is committed to positively changing the world by educating tomorrow’s responsible leaders to bring sustainable solutions to business, society, and the planet. We are therefore delighted to welcome Smith School of Business, Canada, as the 9th member of this purposeful alliance," said Vincenzo Vinzi, Dean of ESSEC Business School and President of the Council on Business & Society.
The CoBS launched in 2011 with four founding members: ESSEC Business School (France, Singapore, Morocco); Keio Business School (Japan); FGV-EAESP (Brazil); and School of Management Fudan University (China), rounding out its global ranks in subsequent years with Warwick Business School (U.K.); Trinity Business School (Ireland); IE Business School (Spain); Stellenbosch Business School (South Africa); and, most recently, Smith School of Business (Canada).
“We are proud to be the first North American partner school in the Council for Business and Society. It’s an honour to be part of an influential group of global business schools that are committed to responsible leadership and the common good. We are excited to be deepening our collaboration with other schools to find solutions to the world’s most pressing issues,” said Wanda Costen, Dean, Smith School of Business.
The CoBS is dedicated to promoting its member schools’ expertise in responsible leadership and sustainable business practice. The Council creates and disseminates materials to encourage a multicultural perspective among students, academics and practitioners, and provides visibility for the member schools’ research, programs and events with a responsible business, management and leadership dimension.
The Council produces editorial resources featuring thought leadership that are free to the public, including its [CoBS Insights](https://cobsinsights.org/) platform and [Global Voice](https://www.council-business-society.org/downloads), the alliance’s quarterly magazine, featuring the global perspectives of faculty and student experts from member schools in the areas of business, management and leadership, and business, society and the planet. The CoBS is also producing a book series, _Focus on Responsible Business,_ together with Routledge.
The CoBS also runs several inter-school faculty-student initiatives in the field of CSR, including a faculty exchange and research initiative, forums focused on issues at the crossroads of business and society, and the [annual student CSR article competition](https://www.council-business-society.org/2023-competition).
Finally, the alliance engages faculty, students, business leaders, practitioners, NGOs and policy-makers to explore how business can positively contribute to society, the planet and the common good, to offer knowledge and solutions to today’s major business and society issues. The Council regularly collaborates with groups such as the United Nation’s Principles for Responsible Management Education (PRME) initiative, the Global Business School Network (GBSN), the Globally Responsible Leadership Initiative (GRLI), the Organisation for Economic Co-operation and Development (OECD), Business for Inclusive Growth (B4IG), as well as social enterprises and other NGOs. 
**The Council on Business & Society**
The [Council on Business & Society](https://www.council-business-society.org/) (The CoBS), visionary in its conception and purpose, was created in 2011, and is dedicated to promoting responsible leadership and tackling issues at the crossroads of business and society including sustainability, diversity, ethical leadership and the place responsible business has to play in contributing to the common good. Follow the CoBS on [CoBSTwitter](https://twitter.com/The_CoBS) and [CoBSLinkedIn](https://www.linkedin.com/company/the-council-on-business-&-society/mycompany/?viewAsMember=true).
**About Smith School of Business**
[Smith School of Business](https://smith.queensu.ca/index.php) at Queen’s University is renowned for its excellence, innovation and leadership in business education. From establishing the first undergraduate business degree over a century ago to creating groundbreaking programs and courses in emerging areas including artificial intelligence, fintech, analytics, cultural diversity, entrepreneurship, team dynamics, social impact and more, Smith is at the forefront of preparing students for the business marketplace. In addition to its rich tradition of academic and teaching excellence, Smith is known for delivering an outstanding learning and development experience. Small class sizes, personal attention, individual and team coaching, opportunities for specialization, and a deep commitment to student success characterize the Smith experience.

# [Experiential Learning](https://smith.queensu.ca/engage/index.php) 
 _https://smith.queensu.ca/engage/index.php_

## Industry & Community
Smith’s Experiential Learning team is dedicated to helping industry and community partners take advantage of our many experiential learning options, and connect with students across our undergraduate and graduate programs.
Discover the [benefits](#benefits) and multiple [ways of participating,](https://smith.queensu.ca/engage/ways-to-engage.php) and the various [incentives,](https://smith.queensu.ca/engage/partner-incentives.php) tax credits and grants available to organizations.
[Contact our team](https://smith.queensu.ca/engage/contact.php)
> “Providing real-world experiences for our students is at the heart of Smith’s approach to business education. Mutually beneficial collaborations with industry – such as internships, capstone projects, Living Cases and hackathons — give our students valuable experience. It enhances their learning while better preparing them for employment after their degree. I thank our many industry partners for their important contribution to the student experience at Smith.”
Wanda Costen 
Dean, Smith School of Business
## Industry Partner Benefits
### Access exceptional talent
Build a pipeline of future employees by engaging with Smith’s highly motivated and skilled students. Evaluate prospective candidates for new or permanent positions, while they are working with your organization.
[View opportunities](https://smith.queensu.ca/engage/opportunities/index.php)  
### Leverage student expertise & knowledge
With 18 academic programs at the undergraduate, early-career, mid-career, and research-focus levels, Smith provides a greater breadth of talent than any other Canadian business school.
[Our programs](https://smith.queensu.ca/academic_programs/index.php)  
### Promote your brand and profile
Experiential learning can showcase your culture, employment opportunities, and values to prospective hires. In a competitive talent landscape, building connection with your brand can be essential in securing the right hires.
### Boost innovation
Smith students are future leaders who contribute new thinking and ideas that will drive organizational innovation.
### Support diversity & inclusion
Foster meaningful engagement with a variety of student groups, including D&I clubs and related case competitions. Hire an intern or mentor a student.
### Achieve strong ROI
Advance important work at competitive labour costs. Plus there are incentives, tax credits and grants available specifically for experiential learning.
[Incentives & funding](https://smith.queensu.ca/engage/partner-incentives.php)

# [Are Bad Visuals Holding You Back? | Smith Business Insight](https://smith.queensu.ca/insight/content/Are-Bad-Visuals-Holding-You-Back.php) 
 _https://smith.queensu.ca/insight/content/Are-Bad-Visuals-Holding-You-Back.php_

**Like a lot of us,** Shiz Aoki has experienced her share of bad visuals. She’s seen big, bold ideas lose oomph due to cluttered charts. She’s seen brilliant minds lose credibility because of slapdash slide decks. She’s seen scientific breakthroughs rendered unintelligible by muddled graphics. She knows, better than most, that what audiences see affects how they react — and that most busy people need help creating accurate and effective visuals. “I realized this is such a huge problem,” Aoki says. 
Aoki, a Queen’s University graduate, is the CEO and co-founder (with fellow Queen’s grad Ryan Marien and Katya Shteyn) of [BioRender](https://www.biorender.com/). This Toronto-headquartered startup is quickly changing the way scientists communicate visually. BioRender operates a web-based design tool that allows scientists to develop polished and accurate figures, graphs and other forms of data visualization simply and intuitively. Think of it as a Canva or Figma for folks who live in the lab. Since its launch nearly seven years ago, the company has become one of the country’s buzziest businesses: in 2018, it graduated from the prestigious Silicon Valley accelerator program [Y Combinator](https://www.ycombinator.com/companies/biorender); in 2023, it landed 17th on the Globe and Mail’s annual ranking of [Canada’s Top Growing Companies](https://www.theglobeandmail.com/business/rob-magazine/top-growing-companies/article-canadas-top-growing-companies-2023/).
Aoki brings a unique, and specific, perspective to how visuals are communicated in presentations and beyond. A lifelong interest in both medicine and visual art led her to concurrently pursue Bachelor of Science (in life science) and Bachelor of Fine Arts (in painting) degrees at Queen’s, before earning a master’s degree from the renowned medical and biological illustration program at the Johns Hopkins University School of Medicine.
Her deep knowledge of the medical illustration space positioned her to both identify a clear market opportunity (a lack of user-friendly tools to create effective scientific graphics) and to lead the development of a better mousetrap in BioRender. “If you’re going to make a difference in a space or for a group of people, you really, really have to understand the problem,” she explains. “There can be a lot of layers to that, and we obsess over all of them. I think that’s what makes the tool feel so easy to use, like something that’s been here the whole time.”
In Aoki’s view, good visuals are about a lot more than esthetics: Clean and clear graphics, charts, decks and more can make a material difference in educating, persuading and motivating audiences, whether you’re in a bio lab or a boardroom. Here, Aoki explains the problems that can arise from bad visuals — and the benefits that can come from investing in good ones.
## Good visuals make your message easier to understand
Most of us have been there: You’re at a conference, and the speaker clicks through to a slide with a crowded, complicated, convoluted graph. You immediately tune her out as you try to make sense of what you’re seeing. Then, before you can register the logic behind the image — much less what you’re supposed to do with it — she moves on to the next, leaving you disoriented, confused and no more educated about the matter at hand than you were when she took to the dais.
Aoki believes that audiences should not have to strain to understand the imagery in front of them. “Less is often more,” she says. Consistent, logical and uncluttered imagery serves as a sort of shortcut for brains to take in big ideas — ultimately making the delivery much more effective. “When you have great visual communication, it aligns everybody in the room in a meeting so much faster,” Aoki says. “It brings people up to speed to the story you’re trying to get across, and that is so valuable.”
## Good visuals build trust 
Pretend you’re in the market to switch banks. You’re evaluating two options. Bank One has a website that looks clean and professional, with colours and fonts that match what you see when you walk into a branch. Bank Two’s site has dated photos, a jumbled user interface, and looks like something your cousin might have dashed off in 2004. Which feels like a safer place for your money?
Again, this is not simply a matter of superficial or decorative preference, as veteran Silicon Valley product designer [Margaret Gould Stewart](https://mags.medium.com/) articulated in an [influential 2015 essay](https://medium.com/facebook-design-business-tools/why-beauty-matters-c38f77d384f0). “If products look ‘janky’ — our industry’s favourite term for poorly crafted — then perhaps our customers might start doubting the validity of our data or the reliability of our back-end systems,” wrote Gould Stewart. “We want the craft of what we do to reinforce a sense of quality; that the product is well made, is reliable, and can be trusted.”
 Aoki believes this is as true in science as it is in business. When things look sloppy or unclear, she says, audiences start to question the degree of care applied elsewhere: “There are a lot of repercussions,” she says. Might a brand that doesn’t care about a harmonious online presence skip due diligence? Might a prospective hire with a rough-and-ready trial presentation struggle to represent the company professionally? It takes very little time to plant a seed of doubt. “Things have to look professional for audiences to feel trust,” Aoki explains. “Mistrust starts when things look intimidating or hard to understand visually.”
## Good visuals influence business outcomes
Imagine a meeting to decide whether to invest in a new technology. The presenter circulates a diagram to represent how it works. One attendee has a question about the icons used. Another can’t tell which colour represents what. A third can’t read overlapping labels. No one is quite sure what Fig. A is supposed to mean, and no one can make out what Fig. B is supposed to depict at all. Before you know it, two-thirds of the meeting has been chewed up in explanations and justifications that wouldn’t be needed had the design been better attended to.
“When you do things like standardize fonts or imagery, it creates a shared grammar or language that helps people quickly pick up what a figure symbolizes,” Aoki explains. “And that allows audience attention to move towards understanding the concepts.” In a world in which time is money, this can make the difference in green-lighting proposals, publishing papers, securing funding and locking down deals.
“Poor visual communication might seem a few degrees removed from things like that, but it can quite directly impact the outcomes of important work,” Aoki says. “So much depends on getting the right buy-in at the right time. That’s true in science, and it’s true in business, too.”
Tags:

# [Five Ideas to Improve Gender Equity Today | Smith Business Insight](https://smith.queensu.ca/insight/content/Five-Ideas-to-Improve-Gender-Equity-Today.php) 
 _https://smith.queensu.ca/insight/content/Five-Ideas-to-Improve-Gender-Equity-Today.php_

**Here’s the good news:** Almost everyone with a successful career in business today [gets the value](https://www.forbes.com/sites/forbesbusinessdevelopmentcouncil/2023/05/11/the-business-case-for-diversity-equity-and-inclusion/) of gender diversity at work. At the very least, they know they can no longer ignore it. 
Here’s the less-good news: Most workplaces still have a lot of ground to gain on the path to equity. Across the board, women are still [paid less](https://www150.statcan.gc.ca/n1/daily-quotidien/230921/dq230921b-eng.htm), [promoted less](https://sgff-media.s3.amazonaws.com/sgff_r1eHetbDYb/Women+in+the+Workplace+2023_+Designed+Report.pdf), and [respected less](https://www.forbes.com/sites/michelleking/2021/10/26/the-authority-gap-why-women-are-still-taken-less-seriously-than-men/) than their male counterparts. Women are more likely to [quit their jobs](https://blog.canadianprosperityproject.ca/burnout-is-the-new-threat-to-canadas-economy-especially-for-women/). And they’re more likely to [experience discrimination](https://www.forbes.com/sites/bryanrobinson/2021/02/15/gender-discrimination-is-still-alive-and-well-in-the-workplace-in-2021/). 
Of course, progress takes time. There’s no button to immediately eliminate every sexist vestige lingering in businesses designed by and for men for decades (if not centuries); there’s no switch to transform workplaces overnight into places where women and non-binary people can thrive and prosper. Pursuing gender equity involves deep, long-term changes to systems, structures and cultures — and that can feel frustratingly slow. 
But in the meantime, there’s plenty you can do to make things better. 
We asked five leading experts on diversity, equity and inclusion to share ideas, decisions and changes you can apply now — as in, today — to put your organization on a more equitable path forward.
## Start tackling systemic barriers
Kate Rowbotham
Distinguished Teaching Fellow of Organizational Behaviour, Smith School of Business
“Many organizations have initiated and implemented incredible individual efforts to benefit women, and a lot of managers and leaders are working very hard to create more equitable workplaces. And these individual responses are important. But they cannot, in isolation, overcome the systemic forces — including the patriarchy and white supremacy — that often underpin how organizations have traditionally been structured. They tend to occur in a framework that, for instance, doesn’t support caregivers, or upholds very specific norms of professionalism as it relates to appearance, or doesn’t accommodate people with different experiences related to generational wealth. There are many systemic elements that get in the way of progress. 
“I think of a saying that is often cited in disability work: ‘[Nothing about us without us](https://en.wikipedia.org/wiki/Nothing_about_us_without_us).’ If decision-makers want to create more equitable places to work, they should commit to bringing in women who have different experiences — including Black women, Indigenous women, trans women, and women with disabilities — to help shape and support the initiatives that make that goal happen. And not in a token way. That’s how we can start to effect systemic change.”
## Understand that no two women are the same
“I think when we hear this question, we naturally think about changes to policies or training. And these are of course important, but before we get there, organizations need to _listen_ to women and _stop_ assuming that all women need the same things. 
“It may seem obvious, but you’d be surprised how many organizations fail at gender equity simply because they have not taken an intersectional approach, at the core of which is understanding that while all women do share some common concerns, there are so many different variations of our needs. The danger in not taking an intersectional approach is that you can end up perpetuating systemic inequalities, leading to the exclusion of certain groups within one community. 
“Workplace leaders must actively consider how various forms of discrimination and privilege intersect to shape women’s lived experiences and tailor workplace initiatives and policies to be inclusive of all women and gender-diverse people, regardless of their intersecting identities.”
## Consider potential — not just proof points
“I think it would be great to see organizations start to look more at the potential of women—and women of colour—when opportunities emerge. 
“Often, if there is going to be a promotion or a new role, leaders will look at men and say ‘I think he can do the job. I think he has the potential to do it,’ even if the candidate might not have all the experience. For women, [it’s very different](https://www.mckinsey.com/featured-insights/diversity-and-inclusion/women-in-the-workplace). The evaluation tends to [centre on proof points](https://www.huffpost.com/entry/first-time-manager-performance-bias-women-of-color_l_6526c699e4b0a32c15c122c2) or past track records. It’s more about ‘Show me that you’ve already done a job like this well,’ instead of ‘Show me what you can do.’ 
“People need to realize that this is a real barrier for the advancement of women. Until there is a mindset shift, it is going to be very difficult to get to a place where we have equity. 
“It would really help if, whenever leaders talk about their talent strategy, or hiring managers review a candidate for a role, they would pause for a moment to reflect and say, ‘Hey, are we having the same conversation about a woman we’re considering for a role as we would for a man?’ Even just stopping to ask that question would be a game changer, in my view.”
## Commit to a menopause action plan
“I think organizations can immediately take action to create menopause-inclusive workplaces for women. In 2023, we released a report called [Menopause and Work in Canada](https://menopausefoundationcanada.ca/menopause-and-work-in-canada-report/), which, for the first time, quantified the staggering economic impact of the unmanaged symptoms of menopause to the Canadian economy at $3.5 billion annually — that includes 540,000 lost days of work per year and $237 million annually in lost productivity.  
“A surprising reality is that women themselves are bearing the brunt of this impact with $3.3 billion in lost income annually. There are five million working women in the country over the age of 40; we represent one quarter of the workforce. Menopause intersects with a critical career stage where women are taking on more leadership roles, and assuming greater responsibility. So, in their peak earning years — when women should be earning the most — some women are stepping away from their roles altogether, or taking a lesser job, or going part time, because they’re having to manage menopause symptoms.  
“We think menopause is the missing link to explain why more women aren’t breaking through the glass ceiling. In fact, _Harvard Business Review_ has done [a](https://hbr.org/2022/12/research-workplace-stigma-around-menopause-is-real) [number](https://hbr.org/2020/02/its-time-to-start-talking-about-menopause-at-work) [of pieces](https://hbr.org/2024/01/how-companies-can-support-employees-experiencing-menopause) on the reality that if organizations want to get serious about retaining and promoting talent, they need to recognize that menopause is a legitimate workplace issue worthy of conversation and action. We cannot afford to lose the competence, skills and capabilities of women in the prime of their working lives.  
“I see this as a significant opportunity for organizations to demonstrate their support for women in their prime and to change the conversation on the ageist narratives that have helped to drive the silence around menopause. We offer a free [Menopause Inclusive Workplace Playbook](https://menopausefoundationcanada.ca/resources/menopause-inclusive-workplace/) to help organizations make meaningful change. We don’t think it’s a heavy lift.”
## Embrace flexibility — permanently
Tanya van Biesen
President and CEO, [_WCM_](https://wcm.ca/)
“We need to keep talking about flexibility. In our society, the burden of care — family care, home care, elder care and child care — still tends to fall disproportionately on women. Flexibility of where, when and how they work enables women to do the many things that often fall to them, while also remaining in the workplace. 
“Flexibility involves orienting workplaces more around performance than presenteeism; it involves focusing on outcomes, not face time. This naturally has implications for return-to-workplace efforts, which are important to a lot of employers. In some roles you simply need to be on site at certain times, but the pandemic has presented us with an opportunity to be more creative and more thoughtful around flexibility at work and to think about how we assess and measure performance on a lasting basis. Are we leveraging everything we learned during that two- to three-year period where many of us worked from our kitchen tables? How much of that can we take into the future?
“In financial services in Canada, we are seeing a number of organizations that are being more creative in their approach to flexible work. And I think there’s a real opportunity for more businesses to do more of that as we move forward.”
Tags:

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=202102) 
 _https://smith.queensu.ca/news_blog/archive.php?a=202102_

The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.

# [Smith School of Business welcomes 10 Team Canada Athletes](https://smith.queensu.ca/news_blog/2024/2024-Smith-School-of-Business-welcomes-10-Team-Canada-Athletes1.php) 
 _https://smith.queensu.ca/news_blog/2024/2024-Smith-School-of-Business-welcomes-10-Team-Canada-Athletes1.php_

**Toronto/Kingston, Ont.** – Today, Smith School of Business, the Canadian Olympic Committee (COC) and Game Plan announced a new wave of Team Canada athletes that will be welcomed into the Smith family.  
  
Ten athletes have been granted Game Plan Awards to pursue their post-secondary education across four graduate programs as part of Smith and the COC’s ongoing partnership. They are:  
* [Michelle Caron](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fmichellejcaron%2F&data=05%7C02%7Cjulia.lefebvre%40queensu.ca%7C99253debf1964ec0f15408dc49d830aa%7Cd61ecb3b38b142d582c4efb2838b925c%7C1%7C0%7C638466440084170533%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=K0eIz2uyd0MKFRssxQEt4X1mkVni12vBFwVxoCD%2B62I%3D&reserved=0), Water Polo (Executive MBA Americas)
* [Alysia Olsen](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Falysia-olsen-oly-14a9ab122%2F&data=05%7C02%7Cjulia.lefebvre%40queensu.ca%7C99253debf1964ec0f15408dc49d830aa%7Cd61ecb3b38b142d582c4efb2838b925c%7C1%7C0%7C638466440084182658%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=nBwrlypEpqPUYB9YtYQ4IRMvfLxlWpnRV%2BbcdZh9L48%3D&reserved=0), Bobsled (Executive MBA Americas)
* [Murray McCullough](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fmurray-mccullough-917154b3%2F&data=05%7C02%7Cjulia.lefebvre%40queensu.ca%7C99253debf1964ec0f15408dc49d830aa%7Cd61ecb3b38b142d582c4efb2838b925c%7C1%7C0%7C638466440084191623%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=0p8amUSzU%2Fd0d9R9RSQIyevoZ%2BfUlB4l7JEkVO6vVvc%3D&reserved=0), Sailing (Executive MBA – The National Program)
* [Victoria Nolan](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fvictorianolanparalympian%2F&data=05%7C02%7Cjulia.lefebvre%40queensu.ca%7C99253debf1964ec0f15408dc49d830aa%7Cd61ecb3b38b142d582c4efb2838b925c%7C1%7C0%7C638466440084199582%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=KnMH1LQJRdDvm4t2jMqMsD4SCO8luU4mNBJVrtRbK5M%3D&reserved=0), Para Rowing (Executive MBA – The National Program)
* [Sam Bonin](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fsamuel-bonin%2F&data=05%7C02%7Cjulia.lefebvre%40queensu.ca%7C99253debf1964ec0f15408dc49d830aa%7Cd61ecb3b38b142d582c4efb2838b925c%7C1%7C0%7C638466440084206824%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=S91bjyiJ15JSYLKWyHNZP8PEw%2BEF%2F%2BxqosGNEXXVUCs%3D&reserved=0), Sailing (Master of Management in Artificial Intelligence)
* [Liam Kopp](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fliam-kopp%2F&data=05%7C02%7Cjulia.lefebvre%40queensu.ca%7C99253debf1964ec0f15408dc49d830aa%7Cd61ecb3b38b142d582c4efb2838b925c%7C1%7C0%7C638466440084214450%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=Vr2bQHnmr8AZ06saM%2BezyGBKe%2Fz%2BZYVA9sTCYuwWHXY%3D&reserved=0), Beach Volleyball (Master of Management in Artificial Intelligence)
* [Kaylee Glagau](https://www.linkedin.com/in/kaylee-glagau-5094a02ab/), Beach Volleyball (Master of Management Innovation & Entrepreneurship)
* [Bret Himmelman](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fbret-himmelman-bb48701b0%2F&data=05%7C02%7Cjulia.lefebvre%40queensu.ca%7C99253debf1964ec0f15408dc49d830aa%7Cd61ecb3b38b142d582c4efb2838b925c%7C1%7C0%7C638466440084228821%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=bQX6i2RUIK1fK9gvWUUzbEsoYV4OwsN6oawubKCGkm0%3D&reserved=0), Canoe Kayak (Master of Management Innovation & Entrepreneurship)
* [Madi Thurgood](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fmadison-thurgood-57504a1b4%2F&data=05%7C02%7Cjulia.lefebvre%40queensu.ca%7C99253debf1964ec0f15408dc49d830aa%7Cd61ecb3b38b142d582c4efb2838b925c%7C1%7C0%7C638466440084235772%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=RlpalaQS96ogvoCP4YbLuHopM34BavbUF6Ogw5AUKSY%3D&reserved=0), Fencing (Master of Management Innovation & Entrepreneurship)
* [Coralie Vittecoq](https://can01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fcoralie-vittecoq-63065a23a%2F&data=05%7C02%7Cjulia.lefebvre%40queensu.ca%7C99253debf1964ec0f15408dc49d830aa%7Cd61ecb3b38b142d582c4efb2838b925c%7C1%7C0%7C638466440084242441%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=3h7BWmKqgyeHoi9zChwG%2BZVT4k7zyFob7MjBV%2B%2BQxO8%3D&reserved=0), Sailing (Master of Management Innovation & Entrepreneurship)
These successful applicants join a network of over 350 Team Canada athletes, including Olympic gold medalists Brad Gushue, AMBA’22; Erica Wiebe, EMBAA’23; and Tessa Virtue, EMBA’22, who have attended Smith’s professional graduate and Certificate in Business programs. Smith was named the Official National Business Education Partner of the Canadian Olympic Committee in 2016.  
“Smith’s team-based approach to learning prepares students for leadership, and these high-performance athletes bring the skills, tools and mindset from world-class coaching and training to the Smith experience,” said Wei Wang, associate dean, professional graduate programs. “Smith is honoured to support Canada’s national team athletes in developing the skills necessary to thrive in today’s dynamic business landscape. In doing so, their classmates also benefit from their determination, collaboration, coachability and resilience.
Smith’s academic awards program is a key component of the COC’s Game Plan, which empowers Canada’s national team athletes to pursue excellence by helping them plan for their careers after competitive sport. 
“We are thrilled to see these 10 Game Plan Awards recipients further their education through Smith’s graduate programs,” said Cara Button, senior manager, Game Plan. “These athletes exemplify the drive to excel not only in their sport but also in their future careers. This opportunity is a testament to their hard work and dedication. We are proud to support them in their journey to success beyond competitive sports.”
**About Smith School of Business:**   
Smith School of Business at Queen’s University is renowned for its excellence, innovation and leadership in business education. From establishing the first undergraduate business degree over a century ago to creating groundbreaking programs and courses in emerging areas, Smith is at the forefront of preparing students for the business marketplace. In addition to its rich tradition of academic and teaching excellence, Smith is known for delivering an outstanding learning and development experience. Personal attention, individual and team coaching, opportunities for specialization and a deep commitment to student success characterize the Smith experience.   
**About Game Plan:**  
[Game Plan](https://www.mygameplan.ca/), powered by Deloitte, is Canada’s total athlete wellness program that strives to develop holistic, well-rounded individuals that excel in and out of sport through a fully integrated program where long-term personal, educational, and professional achievement does not come at the expense of athlete wellbeing. Game Plan supports athletes on and off the field of play, and equips them to stay in sport longer, perform better, and retire healthier knowing they have the tools to prepare and be positive members of their communities at all stages of their career.  
Game Plan is a collaboration between the Canadian Olympic Committee (COC), Canadian Paralympic Committee (CPC), Sport Canada and Canadian Olympic and Paralympic Sport Institute Network (COPSIN) to provide the best resources this country has to offer to our national team athletes – a team that has given so much and inspired so many.   
**About the Canadian Olympic Committee:**  
The [Canadian Olympic Committee](https://olympic.ca/) believes sport has the power to transform Canada. We achieve this by leading the achievement of Team Canada’s podium success and by promoting Olympic values through the Team Canada Impact Agenda. Together with our partners, the COC is committed to making sport safe, inclusive and barrier-free so more young people can play and stay in sport. Learn more at olympic.ca.

# [Indigenous - Black students](https://smith.queensu.ca/yearinreview/2021-2022/highlights/bipoc-scholarships.php) 
 _https://smith.queensu.ca/yearinreview/2021-2022/highlights/bipoc-scholarships.php_

12 highlights from our year## Supporting Indigenous and Black students
In March 2022, two new scholarships were created at Smith to help make business education more accessible to students from two equity-deserving groups.
The Smith School of Business Scholarship for Black Students and Smith School of Business Scholarship for Indigenous Students were created to enhance diversity while increasing access and inclusion for underrepresented groups. The scholarships are awarded annually across each of 13 Smith programs to candidates who self-identify as Indigenous or Black and demonstrate academic excellence, community involvement and proven leadership experience.
"The Indigenous student scholarship helped me to feel more comfortable with the cost of going back to school to complete my MBA. As a Métis woman in business, I appreciate how vital it is to increase Indigenous representation in business management and ownership,” said Caitlin MacCuish, scholarship recipient and full-time MBA student at Smith.
“Scholarships like these give ​underrepresented populations in business a much-needed seat at the table. I am grateful to have this opportunity and look forward to increasing the representation of Indigenous students in business for years to come,” she added.
Originally from Calgary, Caitlin completed Smith’s Graduate Diploma in Business in 2016 before starting her MBA in January 2022.
“Business education must be accessible to people from different backgrounds,” said Wanda Costen, dean of Smith School of Business. “The business world is diverse and the classroom experience should reflect that diversity. Increasing financial award options for students is just one of the ways we are working towards greater accessibility and diversity at Smith.” 
The new scholarships, valued at up to $10,000 each, are available for applicants in all of Smith’s Masters of Business Administration, professional master’s and graduate diploma programs.
During the application process, applicants are given the opportunity to self-identify as Indigenous or Black and confirm whether they would like to be considered for the scholarships.

# [Giving and receiving support](https://smith.queensu.ca/invest/impact-of-giving/daniel-wang.php) 
 _https://smith.queensu.ca/invest/impact-of-giving/daniel-wang.php_

Alumni giving helps the students of today succeed both at Smith and in their future careers. Meet **Daniel Wang, Comm’26,** in the video below, and learn how he is benefitting from alumni support — and how he’s giving back too.
Daniel is the recipient of two awards: **The Commerce 1992 Entrance Award** and **The Ian & Carol Friendly Leadership Admission Award.**
**The Commerce 1992 Entrance Award:** This award was established as an admission award by the Commerce Class of 1992 in celebration of their 15th reunion in 2007 and, as a result of continued fundraising efforts by the class, increased to a renewable award in 2021. It is awarded on the basis of demonstrated financial need and involvement in extracurricular activities or community service to students entering their first year of the Commerce program. The award is renewable for three subsequent years provided a satisfactory academic average is maintained each year and financial need remains evident.
**The Ian & Carol Friendly Leadership Admission Award:** This award was established in April 2008 by Carol and Ian Friendly, BCom’83. It is awarded on the basis of demonstrated financial need and academic excellence to students entering first year of the Commerce program. Preference is granted in the following order of priority: (1) to students who have demonstrated student leadership experience in their high school and (2) to students from the City of Ottawa.

# [Contact Us](https://smith.queensu.ca/invest/contact-us.php) 
 _https://smith.queensu.ca/invest/contact-us.php_

## Smith School of Business
Goodes Hall, Queen's University Kingston, Ontario
1.800.267.7837

# [Smith School of Business | Queen's University](https://smith.queensu.ca) 
 _https://smith.queensu.ca_

_​_
## This is business now.
Smith School of Business at Queen’s University is renowned for its excellence, innovation and leadership in business education. From establishing the first undergraduate business degree over a century ago to creating groundbreaking programs and courses in emerging areas, Smith is at the forefront of preparing students for the business world.
Business happens beyond boardrooms, markets, and borders. Cultural shifts, geopolitical changes, technology innovations — it all impacts business. At Smith we anticipate the rapidly changing business landscape and prepare you for it.
### Smith's EMBA programs ranked top 75 by Financial Times
The Financial Times has released its 2024 EMBA Rankings, with two Smith programs among the best in the world.
 
### New program helps organizations measure impact effectively
The Certificate in Professional Impact Analysis teaches professionals to measure and manage impact, contributing to sustainable business practices.
 
### Scotiabank Centre for Customer Analytics awarded $1.18 million in research funding
New grant to Smith researchers will help move analytics and AI adoption to its ‘next level’ in Canada.
 
### Financial Times ranks Smith MIB No. 1 in Canada
Smith's Master of International Business ranked among top 100 programs globally, the sole Canadian school to make the list.
## Leading-Edge 
Knowledge & Skills
Smith’s programs deliver the knowledge, skills and personal development you need to thrive in this ever-changing business world. General management or specialized, professional or research-based, degree or development, full-time or while working, we have a rich portfolio of options.
## Smith Business Insight
Exploration, commentary and perspective from Smith faculty and experts.
### [Our Top 10 Stories of 2024](https://smith.queensu.ca/insight/content/Top-stories-of-2024.php)
Evolving leadership trends and technological advancements drove interest in our most popular content from the past year
### [How to Build Trusted Brands](https://smith.queensu.ca/insight/content/How-to-Build-Trusted-Brands.php)
Jacqueline Prehogan has grown two of the hottest pet businesses in Canada. She reveals what’s involved in earning consumer confidence — and developing brands that last
### [A Guide to Digital Transformation](https://smith.queensu.ca/insight/content/A-Guide-to-Digital-Transformation.php)
In today’s evolving business landscape, “digital transformation” has become a buzzworthy phrase but what does it really mean for organizations?
## Research@Smith
Creating new knowledge is a central tenet of the Smith School of Business mission. Our research success is the product of the commitment and knowledge of faculty, students, and staff, and our collaborations and partnerships with external organizations.
[Learn more about Research at Smith](https://smith.queensu.ca/research/index.php)

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=201710) 
 _https://smith.queensu.ca/news_blog/archive.php?a=201710_

[## Smith celebrates in Calgary
](https://smith.queensu.ca/news_blog/2017/2017_SmithYYC.php)
October 31, 2017
Calgary, AB — Smith school pride was well represented in Calgary last week as part of #SmithYYC, a series of events honouring the school’s 20th year in Alberta.
[## Michael Pitfield: from Trudeau to teaching at Smith
](https://smith.queensu.ca/news_blog/2017/2017_Pitfield.php)
October 27, 2017
Kingston, ON – When Michael Pitfield, once Canada’s most powerful bureaucrat, died last week at 80 of Parkinson’s disease, obituaries noted his long association with Pierre Trudeau and behind-the-scenes role bringing home Canada’s Constitution in 1982. Lesser known is Pitfield’s contribution to business education here at Smith School of Business.
[## Smith’s Year in Review is now out
](https://smith.queensu.ca/news_blog/2017/2017_YIR_Facts.php)
October 17, 2017
Kingston, ON – The Year in Review 2016/2017 for Smith School of Business is hot off the presses, available in print and online for alumni and friends of the school.
[## Sobey scholars say thanks by giving back
](https://smith.queensu.ca/news_blog/2017/2017_Sobey_Scholars_Thank_You.php)
October 13, 2017
Kingston, ON – Every year around this time, students on the D&R Sobey Atlantic Scholarship at Smith School of Business give a gift to their benefactors: Donald Sobey, BCom’57, LLD’16, and his son Rob, BAH’88.
[## A new Homecoming tradition at Smith
](https://smith.queensu.ca/news_blog/2017/2017_Homecoming_Reunion_Pins.php)
October 3, 2017
Kingston, ON — Alumni who attend this year’s Smith Homecoming Alumni Brunch will find something special “pinned” to their name tags at the registration desk.

# [Jacob Brower](https://smith.queensu.ca/faculty_and_research/faculty_list/brower-jacob.php) 
 _https://smith.queensu.ca/faculty_and_research/faculty_list/brower-jacob.php_

Academic Co-Director - Business (Master of Digital Product Management), Associate Professor & Distinguished Teaching Fellow of Marketing
## Overview
Dr. Jacob Brower is an Academic Co-Director - Business (Master of Digital Product Management), Associate Professor & Distinguished Teaching Fellow of Marketing at Smith School of Business.
[Download Full CV _​_](https://smith.queensu.ca/faculty_and_research/faculty_list/CVs/Jacob-Brower-CV.pdf) [Download Image _​_](https://smith.queensu.ca/faculty_and_research/faculty_list/download_images/brower-jacob.jpg)
### Academic Area
* Marketing
### Interest Topics
* Behaviour & Psychology
* Brand
* Ethics
* Innovation
* Management
* Marketing & Sales
* Social Impact & Sustainability
* Strategy & Innovation
## Faculty Details
### Profile
#### Full Bio
Dr. Brower's research interest include marketing strategy, corporate reputation and brand management, corporate social responsibility and sustainability, brand loyalty and loyalty programs, top management team dynamics, and innovation and design thinking.
His research has primarily examined: 1) the factors that drive corporate social performance (CSP) by firms, 2) whether or not firm CSP impacts firm performance, and 3) how organizations can stimulate pro-social behaviour and ethical consumption practices.
His work has been published in a number of leading international academic journals including the Journal of Management Studies, Journal of Business Ethics, Journal of Product Innovation Management, Journal of Business Research, Journal of Medical Internet Research and Marketing Letters, and has been presented at a number of national and international conferences.
Originally from the Syracuse, NY area, he completed his PhD at the University of Texas at Austin in 2011, and also holds an M.S. in Marketing from the University of Texas at Austin, an M.A. in Economics from Syracuse University, and a B.A. in Economics at the State University of New York College at Geneseo.
Prior to earning his PhD, he worked for several years as a consultant and market research analyst specializing in brand management and tracking for several Fortune 500 clients including FedEx, AT&T and IBM.
#### Academic Degrees
**PhD, Marketing** 
McCombs School of Business, The University of Texas at Austin (2011)
**M.S., Marketing** 
McCombs School of Business, The University of Texas at Austin (2008)
**M.A., Economics** 
Maxwell School of Citizenship and Public Affairs, Syracuse University (2003)
**B.A., Economics (magna cum laude)** 
State University of New York College at Geneseo (2001)
#### Academic Experience
**Smith School of Business, Queen’s University 
**Distinguished Faculty Fellow of Marketing (2019 - Present) 
Associate Professor of Marketing (with tenure) (2019 - Present) 
Assistant Professor of Marketing (2011-2019)
**McCombs School of Business, The University of Texas at Austin** 
Assistant Instructor/Research Assistant (2006-2011)
### Publications
#### Refereed Publications
Brower, Jacob, Monica C. LaBarge, Lauren White and Marc Mitchell. (Forthcoming) Examining Individual Responsiveness to an Incentive-Based Mobile Health App: A Longitudinal Observational Study. _Journal of Medical Internet Research_.
Brower, Jacob and Peter Dacin (2020), An Institutional Theory Approach to the Evolution of the Corporate Social Responsibility – Corporate Financial Performance Relationship. _Journal of Management Studies_, 57(4), 805836.
Brower, Jacob and Pravin Nath (2018). How Top Management Team (TMT) Characteristics Encourage a Market Orientation: The Roles of CEO and TMT Marketing Experience and CMO Presence. _Marketing Letters_, 29(4), 405-419.
Brower, Jacob, Saim Kashmiri and Vijay Mahajan (2017). Signaling Virtue: Does Firm Corporate Social Performance Trajectory Moderate the Social Performance-Financial Performance Relationship? _Journal of Business Research_, 81(December), 86-95.
Brower, Jacob & Katie Rowe (2017). Where the Eyes Go, the Body Follows?: Understanding the Impact of Strategic Orientation on Corporate Social Performance. _Journal of Business Research, 79_(October), 134-142. 
Kashmiri, Saim and Jacob Brower (2016). Oops! I Did it Again: Effect of Corporate Governance and Top Management Team Characteristics on the Likelihood of Product-Harm Crises. _Journal of Business Research, 69_(2), 621-630_._
Brower, Jacob and Vijay Mahajan (2013). Driven to Be Good: A Stakeholder Theory Perspective on the Drivers of Corporate Social Performance. _Journal of Business Ethics, 117_(2), 313-331_._
Luchs, Michael G., Jacob Brower and Ravindra Chitturi (2012). Product Choice and the Importance of Aesthetic Design given the Emotion-laden Trade-off between Sustainability and Functional Performance. _Journal_ _of Product Innovation Management, 29_(6), 903-916_._
* _Reprinted, 2016: “Produktwahl und aesthetisches Design: der emotionsgeladene Trade-off zwischen Nachhaltigkeit und Funktionalitat” in Nachhaltiger Konsum: Institutionen, Instrumente, Initiativen. K. Jantke, F. Lottermoser, J. Reinhardt, D. Rothe and J. Stöver, eds.  Nomos Publishing: Germany._
### Teaching
#### Graduate Supervision and Other Teaching Experience
MSc Supervisor, Chris Murray, MSc in Management, 2018-2019
MSc Supervisor and Dissertation Committee Member, Joel Mohr, MSc in Management, 2015-Present
First Year Project Supervisor and Dissertation Committee, Aaron Zhou, PhD in Management, 2013-Present
Outside member of Dissertation Committee, Barbara Castel, PhD Candidate, Cultural and Policy Studies, Faculty of Education, 2013-Present
Outside Dissertation Committee Member, Ahmad Hijazi, DBA, IE Business School (Madrid), 2017-2019
Dissertation Committee Member, Svetlana Davis, PhD in Management, 2012-2015
MSc Supervisor, Vanessa Schamer, MSc in Management, 2013-2014
MSc Supervisor, Kathleen Guiney, MSc in Management, 2012-2013
Supervisor, Independent Study on Brand Management, Miriam Stauble (BCOM), Fall 2015
Supervisor, Independent Study on Digital Marketing, Ciara Milanetti-Hunt (BCOM), Summer 2016
Supervisor, Independent Study on Digital Marketing, Liam Killops (BCOM), Summer 2016
Teaching Assistant, Analysis of Markets (MBA Core), University of Texas at Austin, Fall 2009-2010
Teaching Assistant, Marketing Engineering (MBA), University of Texas at Austin, Spring 2008-2011
Teaching Assistant, The Invisible Global Market (MBA)
#### Interests
Marketing Strategy, Marketing Analytics/Marketing Engineering, Innovation and Design Thinking, Corporate Social Responsibility and Sustainability, Marketing Research, Introductory/Intermediate Marketing Principles 
### Research
#### Interests
Marketing Strategy, Corporate Social Responsibility/Sustainability, Social Entrepreneurship and Innovation, Corporate Reputation Management, Loyalty and Reward Programs, Marketing Metrics, Ethical Consumerism
### Presentations
#### Conferences and Other Invited Presentations (\*denotes presenter)
Brower, Jacob\* and Peter Dacin, An Institutional Theory Approach to the Evolution of the Corporate Social Responsibility – Corporate Financial Performance Relationship. Invited presentation at Otago Business School, University of Otago, Dunedin, New Zealand, February 2020.
Brower, Jacob\* and Peter Dacin, An Institutional Theory Approach to the Evolution of the Corporate Social Responsibility – Corporate Financial Performance Relationship. Invited presentation at University of Saskatchewan Edwards School of Business, Saskatoon, SK, October 2019.
Brower, Jacob\* and Monica LaBarge\*. Implementing and Managing a Team-Based Learning Environment. Invited presentation at Queen’s Centre for Teaching and Learning Teaching Development Day, Queen’s University, Kingston, ON, September 2019. 
Brower, Jacob\*. Putting Segmentation to Work. Invited presentation at Queen’s Innovation Centre Summer Initiative, Queen’s University, Kingston, ON, June 2019. 
Brower, Jacob\* and Peter Dacin, An Institutional Theory Approach to the Evolution of the Corporate Social Responsibility – Corporate Financial Performance Relationship. Invited presentation at Trinity School of Business, Trinity College of Dublin, Dublin, Ireland, May 2019.
Brower, Jacob\*, Monica C. LaBarge, Lauren White and Marc Mitchell. Examining Individual Responsiveness to an Incentive-Based Consumer Mobile Health App: An Analysis of the Carrot Rewards App Roll Out in British Columbia. Invited keynote presentation at Nudge 2.0 Conference, Toronto, ON, November 2018.
Brower, Jacob\* and Peter Dacin, An Institutional Theory Approach to the Evolution of the Corporate Social Responsibility – Corporate Financial Performance Relationship. Invited presentation at Telfer School of Management, University of Ottawa, Ottawa, ON, October 2018.
Brower, Jacob\* and Peter Dacin, An Institutional Theory Approach to the Evolution of the Corporate Social Responsibility – Corporate Financial Performance Relationship. Centre for Social Impact Brown Bag Series, Smith School of Business, Queen’s University, Kingston, ON, October 2018.
Brower, Jacob\*. Marketing Metrics and Strategy: A Brief Primer. Invited presentation at University of Saskatchewan Edwards School of Business, Department of Marketing MSc Research Camp, October 2018.
Brower, Jacob\*, Monica C. LaBarge\*, Lauren White and Marc Mitchell. Examining Individual Responsiveness to an Incentive-Based Consumer Mobile Health App: An Analysis of the Carrot Rewards App Roll Out in British Columbia. Invited presentation at University of Saskatchewan Edwards School of Business, Department of Marketing MSc Research Camp, October 2018.
Brower, Jacob\*, “Corporate Social Responsibility: Source of Competitive Advantage or Cost of Doing Business”, 10th International Corporate Identity and Associations Research Group Conference, Reading, UK, September 2016.
Brower, Jacob\* and Kathleen Guiney, “Where the Eyes Go, the Body Follows?: Understanding the Impact of  Firm Stakeholder Emphasis on Corporate Social Responsibility”, Centre for Social Impact Brown Bag Series, Smith School of Business, Queen’s University, Kingston, ON, December 2015.
Brower, Jacob\*, “Corporate Social Responsibility: Source of Competitive Advantage or Cost of Doing Business”, Smith School of Business Research Showcase, Queen’s University, Kingston, ON, November 2015.
Brower, Jacob\* and Kathleen Guiney, “Where the Eyes Go, the Body Follows?: Understanding the Impact of  Firm Stakeholder Emphasis on Corporate Social Responsibility”, Faculty Research Seminar Series, Queen’s School of Business, Queen’s University, Kingston, ON, October 2013.
Brower, Jacob\* and Vijay Mahajan, “The CSR Black Hole: Does Firm Corporate Social Performance History Have an Impact on the Social Performance-Financial Performance Relationship?”, Faculty Research Seminar Series, Queen’s School of Business, Queen’s University, Kingston, ON, November 2012.
Brower, Jacob\* and Vijay Mahajan, “The CSR Black Hole: Does Firm Corporate Social Performance History Have an Impact on the Social Performance-Financial Performance Relationship?”, Fordham University, New York, NY, October 2010.
Brower, Jacob\* and Vijay Mahajan, “The CSR Black Hole: Does Firm Corporate Social Performance History Have an Impact on the Social Performance-Financial Performance Relationship?”, Oregon State University, Corvallis, OR, September 2010.
Brower, Jacob\* and Vijay Mahajan, “The CSR Black Hole: Does Firm Corporate Social Performance History Have an Impact on the Social Performance-Financial Performance Relationship?”, Iowa State University, Ames, IA, September 2010.
Brower, Jacob\* and Vijay Mahajan, “The CSR Black Hole: Does Firm Corporate Social Performance History Have an Impact on the Social Performance-Financial Performance Relationship?”, Queen’s University, Kingston, ON, September 2010.
Brower, Jacob\* and Vijay Mahajan, “The CSR Black Hole: Does Firm Corporate Social Performance History Have an Impact on the Social Performance-Financial Performance Relationship?”, Colorado State University, Fort Collins, CO, September 2010.
Luchs, Michael G.\*, Jacob Brower and Ravindra Chitturi, “Sustainable Consumption: The Sustainability Liability and Trading-off Sustainability”, presented at the Carlson Institute for Research in Marketing Sustainability Conference, October 20-22, 2010, Minneapolis, Minnesota.
Brower, Jacob\* and Vijay Mahajan, “The CSR World: Which Companies are More Likely to have a CSR Initiative?”, talk presented at Second Annual International Conference on Business and Sustainability: Designing Sustainability, October 15-17, 2008, Portland State University, Portland, Oregon_._
#### Refereed Conference Proceedings
Brower, Jacob and Joel A. Mohr (2018), “The Moderating Effects of Environmental Knowledge and Concern on Consumer Responses to Green Claim Quantity”, in _Marketing and Public Policy Conference Proceedings Volume 28_, eds. K. Easwar, C. Lamberton and R. Walker Reczek, American Marketing Association, 144-145.
Kashmiri, Saim and Jacob Brower (2013), “Oops I Did it Again: Are Some Firms More Likely to Experience a Product-Harm Crisis?”, in _Annals of the Society for Marketing Advances Volume 2,_ ed. Kevin J. Shanahan_,_ 212-213.
Luchs, Michael G., Jacob Brower and Ravindra Chitturi (2011), “Product Choice and the Benefit of Design given a Trade-off between Sustainability and Functional Performance”, in the _18th International Product Development Management Conference Proceedings,_ European Institute for Advanced Studies in Management.
Luchs, Michael G., Jacob Brower and Ravindra Chitturi (2010), “Trading-Off Sustainability: Choice and Willingness-to-pay Given a Trade-off Between Sustainability and Functional Performance”, in _Marketing and Public Policy Conference Proceedings Volume 20_, eds. Kenneth C. Manning, Kathleen J. Kelly and David E. Sprott, American Marketing Association, 24-25.
### Awards
#### Fellowships
Distinguished Faculty Teaching Fellow of Marketing (2019 - Present)
University Continuing Fellowship, The University of Texas at Austin (2010-2011)
Dean’s Fellowship, McCombs School of Business, The University of Texas at Austin (2007-2010)
Indiana University Haring Symposium Fellow (2009)
#### Teaching Awards
Fred H. Moore Assistant Instructor Teaching Excellence Award Nominee, University of Texas Austin (2010)
#### Other Awards
Best Paper Award, 2010 AMA Marketing and Public Policy Conference, Denver, CO (2010)
#### Grants & Funding
Institutional Grant (2019-2020) 
SSHRC | $4,500
DI McLeod Summer Research Assistantship Award 
2019 | $4,000 
2018 | $2,500 
2017-2018 | $3,840 
2017 | $1,800
Insight Development Grant, with Monica LaBarge (2016-2018) 
SSHRC | $40,540 
Center for Consumer Insight and Marketing Solutions Grant, “Trading-Off Sustainability: When and Why Do Consumers Favor a Product With Superior Sustainability Over One With Superior Functional Performance?”, University of Texas at Austin (2008-2010) 
CCIMS | $5,000
### Service
#### Academic - External
* Editorial Review Board, _Journal of Public Policy and Marketing_
* Reviewer, _Journal of Product Innovation Management_
* Reviewer, _Journal of Business Ethics_
* Reviewer, _Journal of Business Research_
* Reviewer, _California Management Review_
* Reviewer, _Business Ethics Quarterly_
* Reviewer, _Journal of Retailing and Consumer Services_
* Reviewer, _Business Ethics: A European Review_
* Reviewer, _International Small Business Journal_
* Reviewer, _Canadian Journal of Administrative Sciences_
* Reviewer, _Social Sciences and Humanities Research Council Insight Grant_
* Reviewer, American Marketing Association (AMA) Marketing and Public Policy Conference
* Reviewer, AMA Summer and Winter Educator’s Conferences
* Reviewer, Academy of Marketing Science (AMS) World Marketing Congress
* Doctoral Workshop Faculty Mentor, AMA Marketing and Public Policy Conference, June 2019.
* Track Co-chair (with Meike Eilert) and Session Chair, Ethics and Socially Responsible Marketing, AMA Summer Educator’s Conference, 2018.
* Session Chair, Corporate Affairs, Social Responsibility, and Sustainability Track, AMA Winter Educator’s Conference, 2010.
#### Academic - Internal
* Faculty Facilitator, Queen’s Centre for Teaching and Learning Teaching Development Day, September 2019
* Marketing Mentor, Queen’s Innovation Centre Summer Initiative, Kingston, ON, Summer 2019-2020.
* Co-organizer, Smith School of Business Pedagogy Café Teaching Retreat, June 2019
* Co-organizer, Smith School of Business Pedagogy Café, 2018-Present
* General Research Ethics Board (University Level), 2018-Present
* PhD Comprehensive Examination Committee – Marketing Specialization, 2014-Present
* Unit Research Ethics Review Board, 2012-2018 (Acting Chair, Summer 2017)
* Certificate in Business Curriculum and Academic Progress Committee, 2014-Present (Chair 2015-Present)
* MSc/PhD Admissions and Program Committee – Marketing Representative, 2014-2015
* Undergraduate Curriculum Committee – Marketing Representative, 2012
* Organizer of Smith School of Business Case Teaching Workshop and Mentor Network, 2016
* Organizer of Marketing Area Seminar Series, 2012-2013, co-organizer 2014-2015
* Queen’s School of Business (QSB) Building Usage Committee, 2013-2014
* Co-leader of Career Management session at QSB MSc/PhD Consortium – 2013
* Case Facilitator, 10th Annual QSB Responsible Leadership Summit – 2014
* Case Competition Judge, Commerce & Engineering Environmental Conference (CEEC), 2015
* Case Competition Judge, Center for Social Impact Hult Prize Competition, 2015.
* Case Competition Judge, CaseIT Competition, 2016
* Preliminary Round Judge, Inter-Collegiate Business Competition, 2014, 2016.
* Queen’s Leadership, Excellence and Development (QLEAD) - Professor Panelist, 2016
* Queen’s Reads Program Faculty Facilitator – (University-wide, 2013)
#### Community
* Co-chair of Local Marketing Committee, Canada v. USA Rugby Match, Kingston, ON, June, 2012.
* Trail Maintenance Crew, Mountain Bike (MTB) Kingston, Kingston, ON, 2017-Present.
* Trail Ambassador, Mountain Bike (MTB) Kingston, Kingston, ON, 2017-Present.
* Steering Committee Member, Gear Up! Bicycles, Kingston, ON, 2018-Present
* Repair and Renovations Committee, Queen’s Day Care, Kingston, ON, 2018-Present

# [The Wisdom of Do-Nothing Leaders  | Smith Business Insight](https://smith.queensu.ca/insight/content/The-Wisdom-of-Do-Nothing-Leaders.php) 
 _https://smith.queensu.ca/insight/content/The-Wisdom-of-Do-Nothing-Leaders.php_

**Perhaps because he once played** point guard for a number of professional basketball teams in Macedonia, Goce Andrevski likes to punctuate his competitive dynamics research with the wisdom of famous basketball coaches. Legendary NBA coach Phil Jackson is a favourite. Jackson was known for making confounding in-game moves that defied conventional thinking. If the opposing team was on a six-to-nil run and his team was staggering, for example, Jackson would force his players to devise a solution on the fly rather than calling a time out and giving direction.   
Andrevski, the Distinguished Research and Teaching Fellow of Strategy at Smith School of Business, used this type of thinking and other insights from basketball coaching as the basis for his groundbreaking work on what he and colleague Danny Miller (HEC Montréal) termed [strategic forbearance](https://smith.queensu.ca/insight/content/zen-and-the-art-of-competing.php). They found that some basketball coaches — often the most experienced and successful — occasionally make the conscious decision not to react to a challenge even when they have the opportunity and capability to do so. It’s about staying focused on the long game, which may involve providing players with opportunities to gain experience, develop skills and build confidence. 
Just as on the basketball court, executives in corporate boardrooms must determine how to respond to a market competitor. Though they may be twitching to act, Andrevski found, those practising strategic forbearance keep their powder dry for another day. Perhaps they want to avoid [tangling with rivals and their allies](https://smith.queensu.ca/insight/content/when-a-rope-a-dope-strategy-makes-sense.php) or attracting the interest of a regulator, or even concealing strategies that could be used to surprise competitors in the future.  
## **When is purposeful non-action beneficial?** 
When Andrevski discussed strategic forbearance with Smith colleagues and veteran organizational behaviour researchers Julian Barling and Matthias Spitzmuller, it seemed clear that wily basketball coaches like Phil Jackson had something to teach leaders responsible for employee performance in traditional organizations.  
After all, the Western approach to leadership is action-oriented — guiding, motivating and mentoring  — and leaders are judged on the outcomes from those actions. Those who don’t act are often labelled as [passive leaders](https://smith.queensu.ca/insight/content/how-passive-leaders-undermine-employee-well-being.php) — a polite way to say lazy, indecisive, checked out. Is there something to learn from the Eastern approach, inspired by [Taoism](https://www.bbc.co.uk/religion/religions/taoism/), in which “non-action” allows situations to unfold organically and people have the chance to realize their full potential with minimal interference? 
Riffing on what Andrevski learned in competitive dynamics, the researchers, with Smith PhD student Melissa Trivisonno, first brainstormed what “forbearance leadership” would look like. Their formulation: Leaders exhibit forbearance leadership when they are aware of organizational problems and have the capacity and resources to address them, but they intentionally consider the employees’ development needs and refrain from doing so. It could mean not disciplining minor rule violations or reprimanding employees, but also withholding assistance and developmental feedback.    
The leader’s reason for avoiding intervention is the dividing line between forbearance leadership and passive leadership. While passive leaders fail to act due to incompetence and ignorance, forbearance leaders are alert and competent but choose not to intervene in order to compel people to solve problems or learn from experience, or to protect their feelings. 
## **Forbearance under the microscope** 
To test whether their theory held up, the Smith research team conducted four studies based on online surveys — in all, the studies involved 632 followers and 136 leader-follower relationships from various industries. In the first three, they developed a measure of the two dimensions of forbearance leadership (learning and nurturing); in the fourth, they validated their predictive model and examined how this leadership behaviour translated into actual performance. 
The researchers were pleased with the results. They showed that when followers perceive their leaders as intentionally practising forbearance, they learn faster and develop the skills to be more effective. Followers are more dedicated to their work and have greater trust. They have a clearer idea of what’s expected of them and their role at work. 
The key is for the followers to believe that their leaders are making a deliberate choice to be hands-off in the interest of their development and performance, says Andrevski. If they do not interpret their leaders correctly — if the leader means well by forbearing, for example, but the employee doesn’t pick up on that — the employee may interpret the leader’s behaviour as boorish or incompetent. Alternatively, when leaders mindlessly ignore employee needs, but followers see that inactivity as intentional, it could result in unmet expectations that lead to underperformance.   
## **Make intentions known** 
For those leaders who choose to forbear, the message is clear: make sure your employees understand your true intentions. If you exhibit little interest in your employees’ development or comfort level at work, don’t be surprised if your out-of-the-blue forbearance leadership episode backfires. 
For organizational development (OD) practitioners, it may be time to revisit the curriculum of leadership training programs. The researchers say forbearance leadership requires a different set of skills from the active leadership behaviours that are almost the exclusive focus of corporate training. They include being comfortable with silence and inaction, the ability to take a long-term perspective, the openness to reflection and the instinct for compassion. 
OD practitioners may not want to stop there. They may want to revisit their organizations’ performance review and reward systems to determine to what extent they are based on leaders’ observable behaviour versus improvements in their employees’ performance.  
## **Broader view of leadership** 
The researchers are now considering where to take this research further. Since forbearance leadership is a situational behaviour rather than a full-blown style, are there leadership styles (such as servant or transformational leadership) in which it can flourish? Which situations call for forbearance? What are the effects of forbearance leadership over time? Is it equally effective among mature or inexperienced leaders or followers?  
If nothing else, though, the researchers hope their studies highlight the importance of broadening the view of “active” leadership. To think that leaders are only effective when they engage in evident activity is a limiting perspective.  
“Our research marks a radical departure from this long-standing narrative,” says Andrevski. “Ironically, by being seen as doing nothing, forbearance leadership is an active reminder to followers of how much they are trusted and respected, setting the stage for ever-higher levels of motivation and performance.” 
Tags:

# [CPIA - Modules](https://smith.queensu.ca/centres/cpia/program-details/modules.php) 
 _https://smith.queensu.ca/centres/cpia/program-details/modules.php_

## Learning Modules
Module 1
## Impact Foundations
Gain an overview of the concept of impact, including the different dimensions in which an organization and its activities are beneficial or costly to society.
Learn how to assess and define the impact of a decision, strategy, organization, policy, or project, and how to assess existing evidence regarding impact.
### Key Content
* Defining different types of impact e.g., financial, economic, environmental, health, inequality, empowerment, and general wellbeing
* Navigating dynamics with stakeholders, rights-holders, beneficiaries, and other relevant perspectives
* Quantifying, aggregating & comparing intended and unintended impacts
* Analyzing risk and dealing with uncertainty
* Identifying and collecting data and evidence and assessing their quality
Includes examples & case studies
### You will learn how to:
* Justify the need for rigorous impact analysis
* Identify the impacts of decisions on various drivers of wellbeing
* Choose methods and techniques for qualitative and quantitative assessment of impact
* Find existing data and evidence and assess their quality and relevance
* Quantify and value impacts on gender and social inclusion, environment, financial inclusion, access to infrastructure, measures of sustainability, and more
Module 2
## Impact Accounting
Apply the Certificate in Professional Impact Analysis’ impact accounting toolbox to track, document, and report benefits, costs, decision criteria, and risks. This is fundamental to assessing the impact of decisions, organizations, policies, interventions, and investments.
### Key Content
* Grounding in key tools including
 * Cost-benefit analysis
 * Cost-effectiveness analysis
 * Value-for-money analysis
 * Cost analysis
 * Cash benchmarking
 * Social, economic & financial feasibility assessments
 * Portfolio analysis
 * Risk analysis
Apply these tools to examples and case studies and interpret results
### You will learn how to:
* Conduct impact accounting using value-for-money or cost analysis, including cost-benefit, cost-effectiveness, cost-efficiency, and cost-economy
* Use impact accounting to analyze the theory of change
* Measure/report net impact from alternative perspectives
* Estimate and report alternative decision criteria about the viability of a decision
* Use standardized impact analysis statements
* Use impact accounting to design successful interventions and innovative financing mechanisms
* Use impact accounting to prioritize knowledge gaps and develop an institutional learning agenda
Module 3
## Evaluating & Learning
Become adept at using a monitoring, evaluation, and learning toolbox to facilitate data collection, and experimentation. Master impact evaluation, measuring and reporting impact, and improving the design and effectiveness of current and future activities.
### Key Content
* Measuring what matters: how monitoring, evaluation, and learning informs accountability and decision-making
* Evidence culture: using and generating evidence within organizations
* Basics of statistics and analysis for measuring impact
* Approaches for assessing impact
 * Is before-after analysis enough? Review of pre-post, interrupted time series, and event studies
 * Experimental and quasi-experimental approaches including RCTs, A/B testing, difference-in-differences, and regression discontinuity
* Interpreting and communicating results: learning to improve design and funding decisions
* Quantitative data from new and existing sources e.g. firm data, surveys, assessments
* Best practices for qualitative and mixed methods analysis
* Ethics
* Pitfalls in data collection, analysis, and interpretation
* Cutting edge approaches
Exam
## Learning Assessment
The final step in achieving the Certificate in Professional Impact Analysis is a learning assessment. It verifies your understanding of the key components of each learning module and how they fit together. It establishes your knowledge of the role of evidence at all stages of the impact analysis project cycle. The assessment is designed to be very achievable for those who have completed all three learning modules.
Stand out among your peers with this certified credential from Queen’s University.

# [WIL Digital](https://smith.queensu.ca/about/partners/wil-digital.php) 
 _https://smith.queensu.ca/about/partners/wil-digital.php_

Smith partners with ICTC’s Work Integrated Learning (WIL) program to help employers grow their businesses and secure digital internships for students.
## Providing Valuable Experience in IT and Digital Roles
Employers who are hiring students for digital internships may be eligible for [ICTC’s WIL Digital program](https://etalentcanada.ca/for-job-seekers/programs/work-integrated-learning-wil-digital), which offers a wage subsidy of up to $7,000. Smith School of Business and Queen’s University have secured funding for 500 positions to support its corporate partners in hiring students.
The program is available for employers that hire post-secondary students and provide them with valuable hands-on experience in IT and digital roles across all industries, including social media, e-commerce, CRM, IT, digital transformation, data analytics, machine learning, and more.
## What is the ICTC WIL Digital Program?
* Employers with full-time or part-time internship opportunities involving technology or digital transformation can apply for funding.
* Funding of up to $5,000 is available for each internship. Up to $7,000 in funding is available if the student falls within one of the following under-represented groups: Women in STEM (Science, Technology, Engineering and Mathematics), Indigenous students, recent immigrants, students with disabilities, and first-year students.
* Funding is available on a first-come, first-served basis.
* Employers can apply for the WIL Digital subsidy up until the start date of the student internship.
## Applying for Funding
### Eligibility Criteria
#### Organizations
* Are a registered business or not-for-profit in Canada
* Must be hiring for a net new position.
#### Students
* Must be enrolled in a program at a Canadian accredited post-secondary institution during the work placement period and have domestic status.
* All disciplines of study, including business, are eligible.
### How to Apply
* Post your WIL Digital Internship opportunity using the [Smith ‘Post a Job’ form.](https://smith.queensu.ca/recruiting/hire-students/post-a-job.php) You will find an editable template job description here to use.
* Your job posting will be shared with Smith students and you will receive applications as they come in for your review.
* Once an employer has identified the student they would like to hire, the employer completes and submits [Employer Application Form.](https://ictc-ctic.smapply.ca/prog/wil_digital/)
* Upon submission of the form, the student will receive an automated email with a link to the employer’s application and will be prompted to complete and submit a Student Application Form.
* After the student information is submitted, the employer will receive an email notification that the application has been submitted.
* ICTC will alert employers of their approval status within 5-10 business days.
* Successful organizations must sign a contract with ICTC.
* For more details on how to apply, refer to the [ICTC WIL Digital Application guide](https://etalentcanada.ca/sites/default/files/2023-05/WIL-EMP-Guide23.pdf).
ICTC’s WIL Digital supports Canadian organizations that offer student work placements within the Digital Economy. WIL Digital is funded by the Government of Canada through the Student Work Placement Program (SWPP). This program supports the mission of the Information and Communications Technology Council (ICTC) to strengthen Canada’s digital advantage in a global economy.
## Get In Touch
For more information about the WIL Digital partnership, please contact:

# [ISF - Our Team](https://smith.queensu.ca/centres/isf/our-team.php) 
 _https://smith.queensu.ca/centres/isf/our-team.php_

The Institute for Sustainable Finance is led by a team of Canada’s foremost experts and academics in areas of business and sustainable finance. With passion, drive, and determination, the leadership team is committed to helping Canada become an innovator shaper.
## Ryan Riordan, PhD 
Director of Research
[ryan.riordan@queensu.ca](mailto:ryan.riordan@queensu.ca)
Ryan is a Professor and Distinguished Professor of Finance at Smith School of Business and a recent recipient of the Bank of Canada Governor’s Award. He is the Research Director for the Institute for Sustainable Finance and was recognized by the Globe and Mail as a Changemaker for his work on climate finance. Ryan is also the head of the newly established Institute of Financial Innovation and Technology at the Ludwig-Maximilians University in Munich Germany. Prior to joining Smith, Ryan was an Assistant Professor of Finance at the University of Ontario Institute of Technology (UOIT) and an Assistant Professor at the Karlsruhe Institute of Technology in Germany. His work has been published in all of the leading academic finance journals including the Journal of Finance, _Journal of Financial Economics, and_ _Review of Financial Studies_.
## Maya Saryyeva, MA 
Interim Executive Director
[maya.saryyeva@queensu.ca](mailto:maya.saryyeva@queensu.ca)
Maya Saryyeva joined the Institute for Sustainable Finance (ISF) in December 2018 to support the implementation of the Institute’s core programs and outreach efforts. Prior to joining ISF, Maya worked in the international development sector, leading a number of United States Agency for International Development (USAID) funded governance and economic development initiatives in Eastern Europe as well as South and Central Asia. Maya is also pursuing a PhD in global development with a focus on sustainable finance. She researches the efficacy of global governance frameworks surrounding green bonds and sustainable initiatives.
## David Watson 
Associate Director, Communications
[david.watson@queensu.ca](mailto:david.watson@queensu.ca)
David is an experienced professional in public policy, media and the non-profit sector. Before joining ISF he held senior positions at the Macdonald-Laurier Institute, an Ottawa think tank, and the Ottawa Citizen, where he was the Editorial Pages Editor. David began his journalism career at the Globe and Mail. He is a graduate of Bishop's University and Ryerson University.
## Yingzhi Sarah Tang 
Senior Research Associate
Yingzhi Sarah Tang joined the Institute for Sustainable Finance (ISF) in November 2022. Before joining the team, Yingzhi worked with both the private and public sector in Europe, Asia and North America to accelerate their climate and biodiversity ambitions. Over the past three years, Yingzhi led research on green finance and energy transition for emerging markets at the International Institute of Green Finance (Beijing, China), supported the insurance and banking sectors’ climate risk assessment projects at the UNEP Finance Initiative (Geneva, Switzerland) and the Intact Centre on Climate Adaptation (Waterloo, Canada). She holds both a research-based Master’s degree in Environmental Studies (Sustainability Management) and a Bachelor of Environmental Studies from University of Waterloo, and a Bachelor’s degree in Business Administration from Nanjing University of Finance and Economics (China).
## Will Hamilton 
Research Associate
William has a mathematics degree from Dalhousie University and worked in radiomics and computer aided diagnosis before moving into sustainable finance. At the Institute for Sustainable Finance, he develops machine learning models to help process and understand large datasets, and provides assistance with research-related software development and writing tasks.
## Apoorva Hegde, PhD 
Research Associate
Apoorva holds a PhD in Finance from the Indian Institute of Management Mumbai. Her thesis focussed on the dynamic adjustment of capital structure within the Indian manufacturing industry. With expertise in econometric modeling and data analysis, she has authored several publications in reputable international journals. Passionate about sustainability, Apoorva's research is centered on sustainable finance and ESG-related issues, demonstrating her dedication to integrating sustainability into the future of finance. Currently, at the Institute for Sustainable Finance, Apoorva lends her support to various research initiatives focusing on sustainable debt markets, voluntary carbon markets, and projects related to natural assets.
## Tariq Aziz, PhD 
Research Associate
Tariq is an Environmental Economist/Scientist passionate about sustainable resource management. He drives impactful initiatives by combining skills in environmental modelling, economic valuation, and policy analysis. With experience in both public and private sectors, Tariq has contributed to diverse projects such as the Watershed Security Strategy, Nature Agreement, Water Sustainability Act, and Canada1Water. During his academic career, Tariq worked on renowned projects such as Global Water Futures—the largest water science collaboration worldwide among Canadian universities. At the University of Waterloo, his Ph.D. and postdoc work largely focused on integrating water and other natural resources into economic accounts. He earned his master’s in water resources management from five European universities (in France, Germany, the UK, Spain, and Hungary), funded by the European Commission.
## Prateek Sood 
Research Associate
Prateek Sood holds a B.A. in Economics and International Studies from Simon Fraser University and an M.A. in Global Development Studies from Queen’s University. With experience conducting both public sector and academic research, Prateek brings expertise in research design, economics, political science, and data analytics. His recent works on debt sustainability and sovereign debt has been featured by Boston University’s Global Development Policy Center and in _Ethics and International Affairs_. His research was also selected for inclusion in a conference on debt sustainability hosted by the Institute of New Economic Thinking’s Young Scholar Initiative.
## Paris Malakian 
Communications and Marketing Intern
Paris is currently a second-year Commerce student at Smith School of Business, Queen's University. Actively involved in a variety of student organizations, Paris serves as the Sponsorship Coordinator for the Queen's Marketing Association and a Business Competitions member for the Queen's Hyperloop Design Team. Passionate about marketing and communications, Paris is currently a summer student at the Institute for Sustainable Finance (ISF), where she contributes to various marketing and communications initiatives.

# [Journal Prep | Smith Magazine](https://smith.queensu.ca/magazine/startups/journal-prep.php) 
 _https://smith.queensu.ca/magazine/startups/journal-prep.php_

**My company,** Journal Prep, provides academic researchers with services and resources to help them accelerate the academic publication process. Our services include English editing, pre-submission peer review, statistical support and more to be introduced soon.
**Scope:** 30 employees, Montreal-based
**What is the business problem that your product/service solves?** We help level the playing field for non-native English-speaking researchers who want to submit their research papers to English-language journals. We also critique academic papers and offer researchers, including native English-speakers, advice on how to reduce the time it takes to get their papers published.
**The most important thing I’ve learned about starting a business** is that it isn’t easy, and you have to be prepared for not receiving financial compensation for the time you put in, at least not for quite some time. When cash-poor, you have to be creative and efficient in your expenditures.
**Other lessons learned?** Starting my own business has really helped me grow up faster than I likely would have otherwise. Having other people depend on me means I need to ensure that I don’t let anyone down and that I stay focused, even amid the distractions of a university setting.

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=202206) 
 _https://smith.queensu.ca/news_blog/archive.php?a=202206_

The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=201609) 
 _https://smith.queensu.ca/news_blog/archive.php?a=201609_

[## Smith Career Centre’s New Approach to Recruiting a Hit
](https://smith.queensu.ca/news_blog/2016/2016-09-29_OCR_wrapup.php)
September 30, 2016
Kingston, ON – September 30, 2016— On-campus recruiting (OCR) wrapped up at Smith School of Business last week, connecting hundreds of students from the Commerce, MBA, Master of International Business and Graduate Diploma in Business programs with representatives from 60 global organizations.
[## New inductees for Smith Faculty Hall of Fame announced
](https://smith.queensu.ca/news_blog/2016/2016-09-22_Faculty_Hall_of_Fame.php)
September 22, 2016
Kingston, ON – September 22, 2016— Outstanding research, exceptional mentoring and excellent teaching are just a few of the accomplishments of the 2016 Faculty Hall of Fame inductees.

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=202405) 
 _https://smith.queensu.ca/news_blog/archive.php?a=202405_

[## The spring 2024 issue of Smith Magazine has dropped
](https://smith.queensu.ca/news_blog/2024/2024-Spring-Issue-Smith-Magazine.php)
May 21, 2024
Kingston, Ont. – The spring issue of Smith Magazine is now available online and in print. Block some time in your calendar to read the latest articles, including features, alumni profiles, school news and insights from faculty and alumni experts.

# [Raising a hand for equity](https://smith.queensu.ca/invest/impact-of-giving/ana-lopez.php) 
 _https://smith.queensu.ca/invest/impact-of-giving/ana-lopez.php_

One of the strengths of any alumni network is involvement. Are alumni connecting with one another? Helping each other? Helping students? It matters—a lot. Case in point, the support that the Smith alumni community provides to students engaged in advocacy for improvements in diversity, inclusion and student experiences at Smith. The Stolen by Smith Instagram account created in the summer of 2020 highlighted often painful stories of discrimination and exclusion experienced by alumni and current students.
**Ana Lopez, BCom’16,** read those stories and recalls the reaction she and others had. “For many of us, the stories were a catalyst to reflect on our own experiences at Smith.” She decided she had to do something. Or, as she puts it, “I raised my hand.”
Over the next several months, Ana and other alumni mobilized support for the student movement for change that Stolen by Smith started. She volunteered with Reform Smith, a student-led initiative for greater diversity and inclusion, and she helped connect alumni interested in equity work.
Along the way, she became a point person between the school’s administration, students, alumni and Reform Smith. Throughout that process, she says, it was crucial that alumni worked in lockstep with the students. “We are there to support them and to amplify their voices,” she says.
Much work has been done on equity, diversity, inclusion and Indigenization (EDII) at Smith. With the collaboration of alumni, students and the administration, change is happening, with many more initiatives to be implemented. Last year, the school created an EDII task force to develop a strategy to advance system-wide and cultural changes. In March 2021, that strategy and action plan was put into place ([smithqueens.com/inclusion](https://smith.queensu.ca/about/EDII/index.php)).
Ana believes alumni have an important role to play in maintaining momentum on EDII. “What really came up through this process was a desire for change and that people want to be part of that change,” she says.
Ana, who leads operations and platform at Golden Ventures, a seed-stage venture capital fund in Toronto, is also helping to organize the Commerce 2016s’ five-year reunion class-giving campaign this year. Fittingly, her class has elected to support four different school funds that support the following: EDII, equal opportunity access to extracurricular activities, access to needs-based funding, and student mental health and wellness.
“We want to make sure that every student has a great experience and can fully participate at Smith,” she says.

# [Invest](https://smith.queensu.ca/invest/) 
 _https://smith.queensu.ca/invest/_

## Invest in Smith
In the age of COVID-19, the world has shifted rapidly, with uncertainty and disruption across all aspects of Higher Education, including teaching and research. We have had to change how we provide learning and conduct research at an extraordinary pace and scale. At Smith, we thank all our supporters for their leadership in helping us continue to engage in teaching excellence and research.
Borden Chair of Leadership, and Professor of Organizational Behaviour, Smith School of Business.
Smith School of Business is committed to ensuring access to all students with the talent and potential to lead and succeed in business, contribute to their communities, and positively impact society on a broader scale. Having the resources to offer financial support to those students through admission bursaries and awards is vital to upholding that commitment. The Commerce Bursary Fund ensures Smith is better able to recruit a wide array of exceptional students with the diverse perspectives, skills, and capabilities needed to succeed in business. Through the support of our alumni and friends, we are able to ensure talented students with financial need have access to the best resources, education and unparalleled opportunities possible to explore, and reach, their full potential.
## Investment Priorities

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=201408) 
 _https://smith.queensu.ca/news_blog/archive.php?a=201408_

[## QSB’s Centre for Responsible Leadership host environmental change expert
](https://smith.queensu.ca/news_blog/2014/qsbs-centre-for-responsible-leadership-host-environmental-change-expert.php)
August 19, 2014
Kingston, ON – August 19, 2014 - As part of its ongoing commitment to foster leading-edge education in the area of responsible leadership, QSB’s Centre for Responsible Leadership (CRL) recently hosted a visiting scholar with expertise in corporate culture and environmental change.

# [Building Bridges to Smith Commerce](https://smith.queensu.ca/invest/impact-of-giving/john-wilkin.php) 
 _https://smith.queensu.ca/invest/impact-of-giving/john-wilkin.php_

For John Wilkin, BCom’94, the path to the commerce program at Queen’s University wasn’t an obvious one. The son of a homemaker and tool and die maker, John was just the second in his family to consider post-secondary education, and his family had no connections to the university an almost four-hour drive east from his hometown of Brantford, Ontario.
The engineering path his older brother had taken didn’t play to John’s strengths, and while he had a keen interest in history, he also had thoughts of a law career and was looking for something more practical. A little research steered him toward business, and tagging along on a trip to Kingston with some friends to visit Queen’s, he found the commerce program. “I came across it almost by accident,” he says.
That happy accident laid the foundation for John’s 25-year (and counting!) law career with Blake, Cassels & Graydon LLP. “Not coming from a background in the professional world, I got my initial exposure through my experience at Queen’s,” he says. “It helped me develop skills that allowed me to successful.”
Now, John is leveraging that success to help ensure that the path to business education at Smith School of Business is clearly marked, through the creation of a scholarship for young people in Brant County in Southern Ontario, which he initiated during his return to Kingston for Homecoming last month.
“I wanted to create a link to the community that I grew up in,” he says, explaining that outside of the larger city centres where many young people are aware of and focused on Smith Commerce, there are smaller communities with really bright students who aren’t necessarily considering it as an option.
The scholarship is the latest example of John’s ongoing commitment to giving back to the institution he credits as having a profound and lasting influence on his life.
John’s philanthropic support of Queen’s started before he crossed the stage and became an official member of the Commerce alumni network. During his time as president of the Commerce Society, the group launched a giving program called Commitment with the goal of encouraging the graduating class to think about donating to the institution that played a role in their development. It also sought matching donations from some of the leading companies that were recruiting students at that time.
“When you are part of a community and you derive value from that community, it’s important to — in whatever way you can — give back, whether it’s volunteering your time or contributing financially, if you have the resources,” John says. “That’s an important lesson I learned from my parents.”
Since graduating, John has remained engaged with the business school through mentoring, delivering talks to clubs like the Queen’s Commerce Law Association and through the Class of 94’s class giving campaigns.
“Comm’94 has a bursary and I’ve been a part of the team during milestone homecomings that tries to boost that fund,” he says. Established in 2014, the BCom’94 Bursary is awarded based on financial need to students entering first year of the Commerce program. This year, John championed his class to boost contributions to this fund as part of their 30th anniversary Homecoming.
“I really believe in directing resources to help open access and keep the burden off students and their families,” John says. He wants to ensure that other young people have the same opportunity to experience the quality education and community he did.
That community aspect is something he highlights in discussions with two of his three sons, who have followed in his footsteps and are Smith Commerce students. “I tell my kids, when you’re at Queen’s you have this opportunity to meet a lot of great people who, professionally or personally, will be part of your entire life… Members of my class and Queen’s Commerce alumni are my friends, my colleagues, they’re my clients, and they have been my mentors. You become a part of that community early on and it’s such a gift.”

# [Our Insight Topics | Smith Business Insight](https://smith.queensu.ca/insight/tag.php?tid=Looming%20issues) 
 _https://smith.queensu.ca/insight/tag.php?tid=Looming%20issues_

 Smith Business Insight - Our Insight Topics 
[Skip to main content](#main-content)
Smith  
* [About](#)
 
 [Smith Home](/index.php)[Profile](/about/index.php)[News](/news_blog/index.php)[The Dean](/about/dean.php)[Strategic Plan](/about/strategic-plan.php)[Equity, Diversity, Inclusion & Indigenization](/about/EDII/index.php)[Learning Environment](/about/learning_environment.php)[Partnerships](/about/partners/index.php) [Services](/about/services.php) [SmithStore _​_](http://smithqueens.com/smithstore) [Queen's University _​_](https://queensu.ca)
 
* [Learning](#)
 
 [Explore Our Programs](/academic_programs/index.php)[Undergraduate Programs](/academic_programs/undergraduate.php) [MBA Programs](/mba_programs/index.php) [Graduate Programs](/grad_studies/index.php) [Executive Education](/executiveeducation/index.php)[Certificates](/academic_programs/certificates.php)[International](/international/index.php)[SmithEdge](/smithedge/index.php)[Academic Integrity](/about/academic_integrity/index.php)
 
* [Insights & Research](#)
 
 [Smith Business Insight](/insight/index.php) [Research](/research/index.php) [Publications](/about/publications.php) [Centres](/centres/index.php)
 
* [Faculty](#)
 
 [Meet Our Faculty](/faculty_and_research/faculty.php) [Join Our Ranks](/faculty_and_research/Join_Our_Ranks.php)
 
* [Alumni & Giving](#)
 
 [Give to Smith](https://smith.queensu.ca/invest/) [Alumni](/alumni/index.php)
 
* [Recruit & Engage](#)
 
 [Recruiting](/recruiting/index.php) [Partnerships](/about/partners/index.php) [Work with Students](/engage/index.php) [Smith Business Consulting](/centres/business-consulting/index.php)
 
Fresh ideas from [Smith School of Business](/index.php)
* [Topics](#)
 
 ### Categories
 
 * [Leadership](/insight/sections.php?sid=Leadership)
 * [Teams](/insight/sections.php?sid=Teams)
 * [Diversity](/insight/sections.php?sid=Diversity)
 * [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
 * [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
 * [Social Impact](/insight/sections.php?sid=Social%20Impact)
 * [Marketing](/insight/sections.php?sid=Marketing)
 * [Strategy](/insight/sections.php?sid=Strategy)
 * [Finance](/insight/sections.php?sid=Finance)
 
 ### Collections
 
 * [Our Emotions at Work](/insight/collection/Our-Emotions-at-Work.php)
 * [Speaking of Economics](/insight/collection/Speaking-of-Economics.php)
 * [The Age of Corporate Purpose](/insight/collection/the-age-of-corporate-purpose.php)
 * [How To Make Hybrid Work](/insight/collection/how-to-make-hybrid-work.php)
 * [All Collections](/insight/collections.php)
 
 ### Subscribe to Our Newsletter
 
 Cutting-edge research and expert advice delivered straight to your inbox.
 
 [Subscribe](/insight/newsletter.php)
 
* [Webinars](/insight/webinars.php)
* [Podcast](/insight/podcast/index.php)
* [Videos](/insight/video.php)
* [About](/insight/about.php)
Search
# Looming issues
## [Looming Issues](/insight/content/podcast-brave-new-workplace-looming-issues.php)
Robot bosses? Random safety checks at your home office? We may be careening into the unknown, but the workplace of the future will be guided by familiar human needs
[Load More](#)
## Editor’s Picks
1. [The New Rules of Public Speaking](/insight/content/The-New-Rules-of-Public-Speaking.php)
2. [The Untapped Potential of Customer Loyalty Plans](/insight/content/The-Untapped-Potential-of-Customer-Loyalty-Plans.php)
3. [How to Build Trusted Brands](/insight/content/How-to-Build-Trusted-Brands.php)
4. [How Catfish Effects Drive Stock Market Reform](/insight/content/How-Catfish-Effects-Drive-Stock-Market-Reform.php)
[Topics](#nav-menu-topics)
* [Leadership](/insight/sections.php?sid=Leadership)
* [Teams](/insight/sections.php?sid=Teams)
* [Diversity](/insight/sections.php?sid=Diversity)
* [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
* [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
* [Social Impact](/insight/sections.php?sid=Social%20Impact)
* [Marketing](/insight/sections.php?sid=Marketing)
* [Strategy](/insight/sections.php?sid=Strategy)
* [Finance](/insight/sections.php?sid=Finance)
[Collections](/insight/collections.php)
[Webinars](/insight/webinars.php)
[Podcast](/insight/podcast/index.php)
[Videos](/insight/video.php)
[About](/insight/about.php)
## Kingston
Goodes Hall 
Queen's University 
Kingston, Ontario 
Canada K7L 3N6
[1.877.533.2330](tel:+18775332330)
## Toronto
Simcoe Place 
200 Front Street West 
30th Floor
[416.365.7141](tel:+14163657141)
## Smith Programs
* [Undergraduate Programs](/academic_programs/undergraduate.php)
* [MBA Programs](/mba_programs/index.php)
* [Graduate Programs](/grad_studies/index.php)
* [Executive Education](/executiveeducation/index.php)
## Directories
* [Contact Us](/about/contact.php)
* [Smith Centres](/centres/index.php)
* [Smith Services](/about/services.php)
## Connect with Smith
* [Facebook](https://www.facebook.com/smithbusiness)
* [Instagram](https://www.instagram.com/smithbusiness/)
* [Twitter X](https://twitter.com/smithbusiness)
* [Linkedin](https://www.linkedin.com/company/smith-school-of-business-at-queen's-university)
* [WeChat](https://mp.weixin.qq.com/s/SoosIZFmLD0D01aSGJzgLw)
The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.
* [Give to Smith](/invest/ "Give to Smith")
* [Careers](/about/careers/ "Careers at Smith")
* [Program Portals](/academic_programs/student-portals.php "Program Portals")
* [Privacy](http://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy")
© Smith School of Business

# [Leaning into our alumni chapters](https://smith.queensu.ca/invest/impact-of-giving/craig-oconnor.php) 
 _https://smith.queensu.ca/invest/impact-of-giving/craig-oconnor.php_

By day, **Craig O’Connor, MMA’20,** is a data science manager at Compass Digital in Toronto. But last year he took on an extra role as president of Smith Alumni Analytics & AI Chapter. It’s one of [seven alumni chapters](https://smith.queensu.ca/alumni/alumni-chapters.php) that connect the Smith community across industries and cities.
Alumni chapters focus on networking and professional development. Events they host feature top-notch speakers and panellists (who are often Smith and Queen’s alumni).
A big reason these chapters are successful is that each is run by alumni volunteers like Craig. Here, he talks about why he stepped up to volunteer for the Smith community and explains what the chapter has been working on lately.
### How did you get involved in the Smith Alumni Analytics & AI Chapter?
I first heard about the chapter by attending a virtual event a few years ago. It was a panel discussion on building your career in analytics, and afterwards I sought out additional information about the chapter. I originally joined in 2021 as mentorship chair, and I became president last fall when our past president and founder, **Jane Ho, MMA’14,** stepped down. I’m lucky to build on the strong foundation Jane built over her years as president.
### Tell us about an event you’ve held recently.
We’re particularly proud of our panel event at SmithToronto on product management, which served to welcome the new [Master of Digital Product Management](https://smith.queensu.ca/grad_studies/mdpm/index.php) program to Smith. We were lucky to have **Kathryn Brohman,** director of the MDPM program to moderate, and three engaging speakers who shared their experiences in the industry. Our chapter has expanded from the more traditional [Master of Management Analytics](https://smith.queensu.ca/grad_studies/mma/index.php) (MMA) and [Master of Management in Artificial Intelligence](https://smith.queensu.ca/grad_studies/mmai/index.php) (MMAI) grads to welcome any Smith alumni interested in the analytics and AI space, and so we were delighted to have alumni attendees from a variety of Smith undergraduate and graduate programs.
### What kind of mentorship initiatives have you done?
We recently launched our first group mentoring circle focused on people and strategy topics in analytics. Our inaugural group of mentees has a great opportunity to connect with one another and foster a lasting relationship with a mentor in an intimate setting. We’re on track to launch further circles with varied themes shortly. Last year, we also hosted a speed mentoring event, where mentees were able to connect with a series of mentors in a shorter and more informal setting. It was fun, and we’d love to host it regularly.
### What are some of the benefits for alumni to attend chapter events and get involved?
From my experience as an MMA grad, the program’s relatively short duration and high intensity make it difficult to connect with others outside your section, and there was generally very little contact with other programs. The analytics and AI space moves quickly, so we tend to focus our initiatives on continued education. Our events and mentorship offering are the perfect opportunity to connect with fellow alum and stay up to date with the latest industry trends. In my time with the chapter, I’ve been pleased to find that our alumni are generous with their time and open to assisting others in whatever capacity they can.
### What got you interested in working in the analytics field?
Earlier in my career, I bounced around across a few different roles and industries but always noticed my most successful colleagues tended to be the most technically competent. I found myself almost accidentally dabbling in analytics projects — mostly out of curiosity despite it not fitting my job description. Like most analytics professionals, I’d say I’m naturally inquisitive. But I lacked technical experience, so I made a point of developing those hard skills. The MMA program was a big part of that process, and it was a perfect match for me and my career goals.
### Who else is involved in leading this alumni chapter?
I’m lucky to work with four others on the leadership team: **Julia McKeown, BCom’18, Kelvin Zhang, MMA’20, Sammy Steiman, MMA’20,** and **Usman Janvekar MMIE’19, MMA’23.** We’ve also benefitted from fantastic support from Smith faculty and staff. There are a variety of paths to getting involved, and we’re always on the lookout for mentors and panellists. [SmithConnect](https://smithalumniconnect.com/) and our LinkedIn group are the best ways to keep in touch.

# [Is Your Company Socially Responsible Enough? | Smith Business Insight](https://smith.queensu.ca/insight/content/Is-Your-Company-Socially-Responsible-Enough.php) 
 _https://smith.queensu.ca/insight/content/Is-Your-Company-Socially-Responsible-Enough.php_

**Last September, Patagonia** founder Yvon Chouinard made headlines when he announced that he would donate his company to fight climate change. “Earth is now our only shareholder,” he wrote in a [widely circulated letter](https://www.patagonia.ca/stories/a-letter-from-yvon-chouinard/story-127258.html). “Instead of ‘going public,’ you could say we’re ‘going purpose.’ ”
Few companies have put their profits where their purpose is quite like Patagonia. Chouinard and his family are putting their entire company into a specially designed trust and non-profit so that all its earnings—some US$100 million annually—go to save the planet.
But the outdoor clothing retailer isn’t alone in standing up for a cause. Take [Nike’s famous ads](https://www.youtube.com/watch?v=-grjIUWKoBA) with quarterback Colin Kaepernick. Or Delta Air Lines’ defence of voter rights in Georgia. Or the thousands of other corporate pronouncements over the past several years on issues as wide-ranging as race, gender and the environment.
Yet as headline-grabbing and seemingly mainstream as these public displays have become, some critics question whether companies are doing enough. When a company like Apple has a market valuation of US$2.3 trillion—which would make it the seventh wealthiest country on the planet—what level of responsibility does it have to address society’s ills? Moreover, which ills should companies tackle, and how should they do it?
These questions were at the heart of a survey of 1,120 Canadians commissioned by Smith School of Business that gauged what Canadians expect businesses should contribute to social and environmental issues. The big takeaway: many think companies need to prioritize a lot more than their bottom lines.
## **Survey says . . .**
The survey, conducted by Proof Strategies, put a battery of questions to Canadians 18 to 84 from across the country. To the question of whether businesses should do more than they do now to solve society’s problems and help meet the needs of people, 52 per cent of respondents agreed. (Another 32 per cent somewhat agreed.) On average, respondents said that businesses should dedicate 21 per cent of their profits to important social issues.
As for which issues are most urgent, respondents weren’t in agreement. Fair wages topped the list, with 45 per cent saying it must be one of the top three priorities for companies, but 19 other issues were also cited, including food affordability (23 per cent), gender equality (19 per cent), economic development (16 per cent) and net zero carbon emissions (13 per cent).
Some respondents did agree, however, that businesses should be punished for letting them down. About one in five (18 per cent) said they decreased their spending entirely with a brand because of its bad behaviour towards others, or the brand’s position, or lack of a position, on an important issue.
Others went further than that, particularly young people. Canadians 18 to 24 were four times as likely as those 65 and over to ask that an authority (such as a government agency) police or regulate the company. They’re also nearly three times as likely to protest a company that disappoints them.
So how should businesses respond to the issues that Canadians care about? Close to one-third of respondents strongly expect CEOs to take a firm position on social issues. About the same number said it’s more important that a business’s support for a cause be “authentic” than how much money or other support it provides to that cause. Also noteworthy: The authenticity of a company’s support for a cause diminishes in the eyes of Canadians when the CEO stays silent on that issue.
## **A quick history lesson**
At first glance, one of the more eyebrow-raising survey findings is that Canadians view businesses and charities as equally responsible for helping others.
But maybe this shouldn’t be so surprising, says Jacob Brower, Distinguished Faculty Fellow of Marketing at Smith School of Business. “Corporations are the most powerful entities on earth, and therefore people are expecting more from businesses because they see businesses as having the agility and speed to actually do something, and potentially that they hold some responsibility for some of the social ills that they see.”
Brower has been looking at corporate social responsibility (CSR) since his PhD days and says there have been three historical phases to corporate do-good efforts. For most of the 20th century, CSR comprised donations to charities, hospitals and other causes that executives deemed worthy. By the early 1990s, however, CSR started to institutionalize across firms as a way to mitigate harm. Ben & Jerry’s stance [against artificial growth hormones](https://www.benjerry.com/whats-new/2014/corporate-social-responsibility-history) is one example. This was CSR 2.0.
Now, as social movements around gender, race and environmentalism go mainstream, CSR has shifted into a new phase, says Brower. “CSR 3.0 goes beyond a company having its house in order to focus on the broader societal impact the company has on the issues that people care about.”
## **The more things stay the same**
We may see signs of the shift from CSR 2.0 to 3.0 in some of the Smith survey results, says Brower. For example, one question asked respondents to identify which of the [United Nations Sustainability Development Goals](https://sdgs.un.org/goals) businesses should care about. Seventy per cent answered climate action, while only 53 per cent chose “responsible production and consumption.”
“It could be that people see responsible consumption and production almost as table stakes,” says Brower. In other words, firms should have already dealt with these CSR 2.0-type issues. “Climate action is still about doing less harm, but the expectation is increasingly about looking forward at the broader socio-environmental impact of business as a whole.”
So what should businesses do with results like these? Perhaps take them as a signal for how to proceed, says Brower. “One of the things I’ve been arguing in my recent work is that CSR 2.0 is a necessary condition for CSR 3.0. If your house is not in order and you attempt to engage in brand activism, you are probably going to get in trouble.”
Another lesson: Canadians think businesses should care about a lot of different social issues. But this shouldn’t be surprising either, says Brower. “It’s what we see in marketing generally—the market is fractured. And what that creates is an opportunity to niche specialize for different groups of people.”
In short, the survey is a reminder to think about the fundamentals of marketing, says Brower. “No corporation is going to be able to deal with all of these issues, nor should they most likely. It’s still really important to go back to the basics of understanding who your customers are, what issues matter to your constituency, and in what way they are likely to respond.”
Tags:

# [StartUps | Smith Magazine](https://smith.queensu.ca/magazine/startups-index.php?c=Communications) 
 _https://smith.queensu.ca/magazine/startups-index.php?c=Communications_

An ad agency with no employees. Instead, we have curated a global network of freelance professionals.
A​fter graduating from Commerce in 2014, Jacie deHoop, Ellen Hyslop and Roslyn McLarty, GDA'14, landed corporate jobs in Toronto.
Journal Prep provides academic researchers with services and resources to help them accelerate the academic publication process.
A digital personal branding and marketing tool for students that showcases their skills and personality.
**My company,** SWFTCharge provides a quick, portable and convenient phone-charging service for conferences, festivals, theme parks, sporting events and other large-scale venues.

# [How to Build Trusted Brands | Smith Business Insight](https://smith.queensu.ca/insight/content/How-to-Build-Trusted-Brands.php) 
 _https://smith.queensu.ca/insight/content/How-to-Build-Trusted-Brands.php_

**Jacqueline Prehogan, BCom’07, knows what really resonates** with people. And animals too! She helms two of the hottest pet businesses in Canada after all.
The first, [Canada Pooch](https://ca.canadapooch.com/), which Prehogan founded in 2011, makes and sells functional (and pretty doggone adorable) apparel and accessories for chic canines. The second, [Open Farm](https://openfarmpet.com/), which she’s run alongside her husband Isaac Langleben since 2014, manufactures ethically sourced premium dog and cat food. They’re [two of the fastest-growing consumer brands](https://www.theglobeandmail.com/business/rob-magazine/top-growing-companies/article-canadas-top-growing-companies-2023/) in Canada, each of which has earned enviable trust and loyalty.
Steering two pet-focused brands was not on Prehogan’s radar when she graduated from Smith School of Business with a bachelor’s degree in commerce. She didn’t even have plans to become an entrepreneur. While she’d been involved in the Advancing Canadian Entrepreneurship club (now known as [Enactus](https://www.queensenactus.ca/)) during her undergrad, she was working as an accountant and had enrolled in law school when her idea — to develop a pet apparel brand — took hold and wouldn’t leave. A few weeks, some prototypes and a whole lot of pavement-pounding later, it became clear: Her future was in paws, not law. 
In her roles as CEO at Canada Pooch and chief brand officer at Open Farm, she guides and drives the companies’ strategic brand focus. Being a brand-builder is another identifier Prehogan wouldn’t have given herself back in the day, but as she started to see her vision connect with Canada Pooch — and later Open Farm — customers, she realized she had a real knack for it. “I really didn’t think I was creative,” she says. “Only being thrown into it did I realize that I actually have a ton of creativity. It just took working on the right thing, with the right people, to unlock it.”
In this conversation with Smith Business Insight contributor Deborah Aarts, Prehogan shares a bit of what’s involved in capturing audience attention, cultivating true trust and building successful brands at a time when buyers have never been better informed and have never had more choice.
**The concept of a “brand” can feel a bit nebulous. What does it mean to you?**
 To me, it is a simple idea: Your brand is the feeling you create. Things like logos and colours and taglines are part of it, but those things evolve and change over time. The feeling that you give your audience tied to its reason for being and the value that delivers to consumers — that’s what ultimately drives a brand. 
**How does that manifest in your businesses?**
Both brands have a similar consumer and are focused on delivering unmatched quality and industry-leading innovation, but there are key differences.
Canada Pooch aims to support the experience of pet parents and their pets by making things seamless. We create products that help people solve some of the day-to-day challenges dog moms and dads face. The brand is function-forward, it’s innovative and it’s approachable. We’re providing innovative solutions.
Our mission at Open Farm is to do some good for animals and the planet, and since the business produces food, it’s all about trust. Our customers need to trust that our food is being made to the highest standards. We’re obsessed with it; we’re always working to be a change-maker in what we do inside our four walls and to continue the ripple effect of good through our supply chain. The brand is mission driven, caring, open and honest. We’re providing peace of mind.
**You’ve clearly put a lot of thought into this. What sparked that passion?**
The early days of Canada Pooch taught me that your brand is ultimately the secret sauce of what you do. You can work so hard and make the best product, but it can still be commoditized if there’s no way for consumers to recognize it. A good brand serves as a moat around what you do; it’s a lot more difficult to carve out a space for yourself if you don’t have one.
When we started Open Farm we decided to really invest in both brands, to build up trust and love with consumers through everything we do. And it kind of snowballed from there.
Left to right: Jacqueline Prehogan snuggles up with Teddy the Bernedoodle (left) and Maddie the pug mix (right)
**You operate in an industry that is both** [**extremely competitive**](https://www.arizton.com/market-reports/pet-care-market) **and** [**growing fast**](https://www.morganstanley.com/ideas/pet-care-industry-outlook-2030)**. How does an upstart brand make a mark in a context like that?**
I think it starts with differentiation. Fundamentally, what value is your brand adding?
Take our experiences with Open Farm. Pet food is a very saturated industry, with big players with deep pockets. There’s also a lot of what we think of as ‘me too’ products (copycats, essentially) and marketing fluff. When we were starting, most people in the industry told us, ‘Don’t even try. You can’t break in.’
We decided that our brand exists to create the healthiest food for pets — food that’s going to help them thrive. We do that in our own special way, which is all about maintaining the highest standards; we really go to the ends of the earth to source the best ingredients. That’s how our brand adds value and it’s how we differentiate it. 
**How do you impart something like that to new customers? You only have a tiny window to catch their attention and there’s not a lot of room for nuance in an Instagram ad or on a product label.**
You need to get good at introducing yourself to the consumer. You need to really know yourself as a brand — what you stand for, what you do and what you have to offer — and you need to be able to convey that. From there, put yourself in the shoes of your customer: Think about what makes them tick and what they need to see to believe that you can support their unique needs.
Pet parents just want to enjoy their pets, and that isn’t always easy. For instance, feeding pets can be confusing, depending on the age, activity level, health and the likes and dislikes of the animal. We see our role as giving pet parents peace of mind. When they choose Open Farm they know we’ve obsessed over every standard, every ingredient, every recipe, because we’ve communicated that in a way that’s easy for them to understand and — critically — because our product delivers on it. They can rest easy because they know they’re feeding their pet the best.
**Does it help that, as a pet parent yourself, you _are_ your audience?** 
Oh, my gosh, yes. Everything I’ve ever done in this industry is inspired by my own pets. You can look at research, you can bring in all the external knowledge in the world, but there is no substitute for applying your own experience.
Almost everyone on our team is obsessed with dogs and cats. If they don’t have pets themselves, someone in their family does. We have dogs and cats in both company offices every single day, doing everything from fitting or taste testing our products, to marketing and photography, to just hanging out. So, yes, we are fully immersed in pet life. It’s a blast and it also inspires our ideas.
**How does that immersion translate to brand loyalty among your customers?**
We work hard to make it clear that we are supporting each pet and pet parent on their entire journey and that we know that journey can evolve.
Also, we never sit back and coast. Ever. Both businesses maintain the mindset that we need to re-earn our spot feeding and clothing each pet every day. I think the downfall of a lot of brands comes from getting disconnected from that drive. You can start to think ‘We’re successful as is, we don’t need to work as hard.’ We’re kind of the opposite. We keep trying to raise the bar.
Tags:

# [Overview](https://smith.queensu.ca/about/partners/index.php) 
 _https://smith.queensu.ca/about/partners/index.php_

## Canada’s #1 Strategic 
Education Partner
Smith School of Business works closely with partners to build opportunities that serve objectives and enhance business education.
[Download Brochure](https://smith.queensu.ca/about/partners/Corporate-Engagement-at-Smith.pdf)
## We’re committed to working with our partners on innovative and meaningful initiatives
Smith established the first undergraduate business degree and continues to create ground-breaking programs in artificial intelligence, fintech, analytics, social impact, and more.
* Exceptional faculty
* 14+ undergraduate and graduate business degree programs
* 1500+ graduates per year
* 25+ professional development and corporate education programs
* Breakthrough research
* Thought leadership
## Our Featured Partners
## Experiential Learning
Dedicated to helping partners connect with students across our undergraduate and graduate programs, Experiential Learning provides organizations with valuable opportunities to work with student talent.
[Learn More](https://smith.queensu.ca/engage/index.php)

# [Impact of Giving  - Supporting our students](https://smith.queensu.ca/invest/thanks.php) 
 _https://smith.queensu.ca/invest/thanks.php_

## Supporting our students
Learn how donors, volunteers and student recipients are making a difference at Smith and beyond
### Building bridges: Alum marks the path to Smith Commerce
#### John Wilkin, BCom’94
A happy accident put John Wilkin on the path to a business education at Queen's and a successful career in law. Now, he wants to help ensure that the path to Smith is clearly marked and accessible for young people who aren't considering it an option.
[Read John’s story](https://smith.queensu.ca/invest/impact-of-giving/john-wilkin.php)
### A lifelong commitment to giving back
#### Ian Friendly, BCom’83
Going to Queen’s changed Ian Friendly’s life and career trajectory. That’s why he’s making sure today’s students have the same opportunities he did. Ian has been giving back to Queen’s almost since the day he graduated.
[Learn more](https://smith.queensu.ca/invest/impact-of-giving/ian-friendly.php)
### Giving and receiving support
#### Daniel Wang, Comm’26
Alumni giving helps the students of today succeed both at Smith and in their future careers. Meet Daniel Wang, and learn how he is benefitting from alumni support — and how he’s giving back too.
[Watch now](https://smith.queensu.ca/invest/impact-of-giving/daniel-wang.php)
### Coming full circle
#### Mila MacCuish, BCom’21 
Caitlin MacCuish, GDB’16, MBA’23, Artsci’16
Mila MacCuish and Caitlin MacCuish are Métis sisters who have found a unique way to help today’s students: support the very award that allowed Mila to study at Smith.
[Read more](https://smith.queensu.ca/invest/impact-of-giving/mila-caitlin-maccuish.php)
[Previous](#carouselTestimonials) [Next](#carouselTestimonials)

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?c=Centres) 
 _https://smith.queensu.ca/news_blog/archive.php?c=Centres_

[## Smith programs support the success of new ventures
](https://smith.queensu.ca/news_blog/2024/Smith-programs-support-the-success-of-new-ventures.php)
January 16, 2024
Kingston, Ont. – Four ventures with ties to Smith School of Business are starting the year off on a high note as winners of two of the business school’s competitions that foster and support entrepreneurship. 
[## 2022 Dare to Dream winners announced
](https://smith.queensu.ca/news_blog/2022/2022_Dare_to_Dream_winners_announced.php)
May 31, 2022
Kingston, Ont. – Four early-stage business ventures led by Smith School of Business students have been given a boost in funding from Smith’s Dare to Dream program.
[## Conflict Analytics Lab launches AI tool to streamline vaccine injury claims process
](https://smith.queensu.ca/news_blog/2021/2021_Conflict_Analytics_Lab_launches_Vaccine_Mediator_tool.php)
November 29, 2021
Kingston, Ont. – The Conflict Analytics Lab (CAL), a joint project between Queen’s Law and Smith School of Business, has launched an online dispute resolution tool for COVID-19 vaccination claims in partnership with researchers from the University of Oxford, University College Dublin and the British Institute of International and Comparative Law.
[## New Smith partnership provides Indigenous business training
](https://smith.queensu.ca/news_blog/2021/2021_Smith_Spalyan_partnership_delivers_Indigenous_business_training.php)
October 13, 2021
Kingston, Ont. – A new partnership between the Centre for Business Venturing (CBV) at Smith School of Business and Spalyan Education Group is bringing business, entrepreneurship and management training to six Indigenous communities in British Columbia.

# [Your Firm’s Most Undervalued Asset? Try Nature | Smith Business Insight](https://smith.queensu.ca/insight/content/Your-Firms-Most-Undervalued-Asset-Try-Nature.php) 
 _https://smith.queensu.ca/insight/content/Your-Firms-Most-Undervalued-Asset-Try-Nature.php_

**When you think of sustainability** and business, your mind likely zips to climate change. By now, companies and investors are well-versed in the imperative to decarbonize and pursue net-zero objectives — whether they want to or not. 
But the planet is also facing another environmental crisis — one of biodiversity loss. Three-quarters of Earth’s land surface has been [significantly altered by the actions of people](https://www.unep.org/facts-about-nature-crisis); 66 per cent of ocean area now shows the effects of human activity. With their habitats transformed, degraded and/or destroyed, monitored populations of wildlife have declined [by an average of 69 per cent](https://www.worldwildlife.org/press-releases/69-average-decline-in-wildlife-populations-since-1970-says-new-wwf-report#:~:text=WASHINGTON%2C%20D.C.%20\(October%2012%2C,WWF\)%20Living%20Planet%20Report%202022.) in the past 50 years. One million of the planet’s estimated eight million species of plants and animals [now face extinction](https://www.ipbes.net/news/Media-Release-Global-Assessment). 
This is very much a business matter. Economic activity is now operating beyond the threshold of safety [in six of the nine “planetary boundaries”](https://www.stockholmresilience.org/research/planetary-boundaries.html)  defined by the Stockholm Resilience Centre — zones within which humanity can thrive and sustain our development. More than half of global GDP is [moderately or highly dependent](https://www3.weforum.org/docs/WEF_New_Nature_Economy_Report_2020.pdf) on nature. The World Bank forecasts that ecosystem collapse will prompt annual declines in global GDP of [2.3 per cent by 2030](https://openknowledge.worldbank.org/server/api/core/bitstreams/9f0d9a3a-83ca-5c96-bd59-9b16f4e936d8/content). Moody’s has pegged the risk of nature loss to business [in the trillions](https://www.bnnbloomberg.ca/moody-s-has-a-1-9-trillion-warning-over-biodiversity-1.1824883). As the authors of a 2021 Boston Consulting Group report sum it up: “Biodiversity loss has massive implications for business.” 
It’s increasingly clear that a healthy economy hinges on a healthy living planet. Yet biodiversity remains something of a missing link in corporate environmental, social and governance (ESG) strategies. In fact, [fewer than one in four businesses](https://www.capgemini.com/news/press-releases/only-24-of-organizations-have-a-biodiversity-strategy-in-place/#:~:text=Currently%2C%20just%2016%25%20of%20organizations,only%2020%25%20for%20their%20operations.) have policies in place for how to measure, manage and mitigate their impacts and dependencies on the natural world. 
Smith Business Insight contributor Deborah Aarts spoke with Ryan Riordan, professor of finance and director of research at the [Institute for Sustainable Finance](https://smith.queensu.ca/centres/isf/index.php) housed at Smith School of Business, about the increasingly pressing need for businesses to recognize the value of biodiversity — and the competitive advantages of doing so.  
**To begin, what are we talking about when we talk about biodiversity?** 
From a sustainable finance perspective, what we’re talking about is healthy, intact, productive ecosystems that generate some sort of economic or social benefits for humanity. These benefits take all sorts of forms: It could be that we get clean air, that we get spaces for recreation, that we get clean water, that we have pollinated crops. 
**Those are all lovely things, but how do they add value from a business point of view?** 
Organizations are sitting on all these natural assets whose values are currently being reflected at zero on their balance sheets. Think about a company that owns some land that is not currently developed. They might look at that and see something that’s not producing any economic activity. But that land has great value. It’s doing a lot of things. It’s cleaning the air, it provides habitats, it might be a place for recreation. It has all these ancillary benefits. The problem is, until very recently, businesses had no framework to value that.
**How is the work of the Taskforce on Nature-related Financial Disclosures (TNFD) changing that?** 
The [TNFD](https://tnfd.global/) is a multinational coalition of industry experts that provides [a voluntary disclosure framework](https://tnfd.global/recommendations-of-the-tnfd/) for businesses and financial institutions around biodiversity. Its goal is to put some structure around how organizations can disclose and manage risks around everything related to their natural assets. You know the old adage that what gets measured gets done? In this case, it’s kind of like what gets measured gets protected, and what gets measured gets improved. 
The Institute for Sustainable Finance is, along with CPA Canada, the secretariat of the TNFD in Canada. We’re [pulling together resources](https://smith.queensu.ca/centres/isf/resources/TNFD-resources.php) for businesses. We’re helping to organize some [information sessions](https://smith.queensu.ca/centres/isf/events-index.php). We’re helping to collect questions and funnel them towards the global TNFD group. 
The TNFD only officially launched its disclosure framework late last year. Right now, we have [a handful of early adopters](https://www.theglobeandmail.com/business/article-nature-related-risk-disclosure-for-canadian-companies-may-be-years/) in Canada.
## Want to learn more?
The Institute for Sustainable Finance has resources about biodiversity and the work of the TNFD.
[View Resources](https://smith.queensu.ca/centres/isf/resources/TNFD-resources.php)
**A company’s impact on nature doesn’t seem to be as easily quantifiable as, say, the greenhouse gas emissions it produces. What is involved in accounting for biodiversity?** 
I think the first step is for organizations to recognize that, broadly defined, nature and ecosystems are useful inputs to economic activity. 
We have hundreds of years of understanding how to measure some parts of business. Think about a factory: We know how to tabulate what is useful inside it, and we know how to measure productivity. We know what goes into making something, how long it takes, what steps are involved, what machines or tools are used, how it’s delivered. It’s not hard to tally the value of all of the outputs that we get out of that factory, whether it’s money or number of units produced. We are very good at understanding how a factory produces economic benefits for humanity or for society. 
We can think of an ecosystem the same way. We can think about every one of its individual components and measure them as we would in a factory. We can quantify the value of things like biomass and species. We can start using nature as an asset that adds value instead of something to be bulldozed over. It’s a bit less straightforward, but it’s doable.
**Biodiversity does seem to get a lot less airtime than climate change and decarbonization. Is it safe to say nature isn’t talked about enough in business?** 
That’s a fair assessment. We’re in early, early days when it comes to businesses prioritizing biodiversity. Think of it this way: A lot of firms are still in the early stages related to decarbonization, and we’ve had carbon taxes for at least half a decade now — longer in some provinces. When it comes to nature, they’re much further behind. Of course, there are some companies that have been paying attention to nature forever, as part of their ethos. But for most others, it hasn’t really crept in yet. 
**Putting aside the motive that everyone loves butterflies and trees: Why should businesses add biodiversity to their already-long list of priorities — and why now?** 
I mean, I’m a pretty green guy, but you don’t even have to see it through that lens. 
Here is my pitch: Natural assets currently aren’t even reflected on the balance sheets of most companies, or on those of jurisdictions like municipalities, provinces and countries. Because they’re not really recognized as assets — real, financial assets — businesses aren’t really thinking much about how to protect them. Many businesses are sitting on a wealth of natural assets that they’re just ignoring. 
That means that companies that start thinking about biodiversity as something that has value have a chance to recognize an asset that most others don’t yet see. 
**So, does that make biodiversity a competitive advantage?** 
This is almost like an arbitrage opportunity. All you have to do is generate a little bit of information that other people don’t have and you’re going to have a better insight on the value of your own company — and in your competitors, and your industries and across industries. Of course, there’s no free money, and doing this isn’t free. But it’s as close to free as you can get. And that informational advantage is not going to be there forever, so take it while it’s there. 
If you can tell a story about how your company is caring for and investing in its resources, and if the markets hear it, it might help you to raise capital at better prices. You’ll be farther along when and if disclosure does ever become mandatory, or when large groups of investors start to really care about this stuff. It’s much easier to be credible if you’ve been doing it for a while. 
Then, of course, it really is the right thing to do. I mean, if you can make some money by doing something relatively straightforward, and it offers so much benefit to everyone — including the planet, and your kids, and my kids — it just seems to me like an easy win. 
**In Canada, biodiversity disclosure is all voluntary, for now at least. Is it mandatory anywhere else?** 
Not yet, at least not in any major jurisdiction. 
**Do you see that changing?** 
Either that’s going to change or the planet’s going to change. 
**Still, we know most companies struggle to do the right thing if they don’t _have_ to do the right thing. How do you create a sense of urgency?** 
It can be hard to put a fire under people for this type of thing, yes. That’s why I really like to tout the benefits businesses can get from doing this early. 
**On that note: What advice can you share for business leaders looking to start taking on the biodiversity crisis?** 
The scope of a lot of the conversation around biodiversity is big. But I’d challenge people to look for some small things that they can do at their own companies, or in their own industries, to address whatever is being unrecognized from a nature perspective. 
Maybe there’s a little field next to a factory. Maybe the plan is for the company to develop it in 10 years, so maybe it’s sitting barren and empty. Why don’t you just put in some trees or throw some seeds down? There are all sorts of little things you can do to increase the value of the natural assets that you already have, and these things can have other benefits, too. So I’d say: Think big, yes, but also think small. 
_The Institute for Sustainable Finance is hosting a webinar to explain the TNFD’s recommendations on April 25 at 12 p.m. ET. Learn more and register to attend_ [_here_](https://smith.queensu.ca/centres/isf/events/TNFD-Part-2.php)_._
Tags:

# [MMAI - Coaching](https://smith.queensu.ca/grad_studies/mmai/smith-experience/coaching_career.php) 
 _https://smith.queensu.ca/grad_studies/mmai/smith-experience/coaching_career.php_

## Coaching & 
Career Support
All Smith School of Business students have access to our outstanding coaching services.
Smith also provides a broad range of online resources for networking with alumni and industry partners through our Career Advancement Centre and SmithConnect.
[Class Profile](https://smith.queensu.ca/grad_studies/mmai/our-students/index.php)
**Team Coaches:** 
to support optimal functioning of project teams
**Executive Coaches:** 
to provide individual support to develop personal effectiveness
**Career coaches:** 
to assist with career objective-setting, and job-search strategy, as required

# [Our Name - Oct 2015](https://smith.queensu.ca/about/our-name.php) 
 _https://smith.queensu.ca/about/our-name.php_

## Our Name - Smith School of Business
On October 1, 2015, the School began a new chapter in its impressive history. In recognition of the generous gift of $50 million from Queen’s alumnus Stephen Smith, the School adopted a new name – Smith School of Business at Queen’s University.
This extraordinary gift, the largest gift ever made to a Canadian business school, enables the school to continue to transform business education, enhance the student experience, and attract the best and brightest talent from across Canada and around the world.
From establishing the first undergraduate business degree a century ago to creating ground-breaking programs and courses in emerging areas including artificial intelligence, fintech, analytics, cultural diversity, team dynamics, social impact and more, Smith is at the forefront of preparing graduates for the business marketplace. In addition to its rich tradition of academic and teaching excellence, Smith is known for delivering an outstanding learning and development experience. Small class sizes, personal attention, individual and team coaching, opportunities for specialization, and a deep commitment to student success characterize the Smith experience.
## Stephen J.R. Smith
Stephen Smith, BSc’72, LLD’17, is one of Canada’s leading entrepreneurs in the financial services industry. He is renowned for innovation in information technology and financial structuring in the Canadian mortgage industry. He earned a Bachelor of Science (Honours) in Electrical Engineering from Queen’s University (’72) and a Master of Science (Economics) from the London School of Economics and Political Science. In 2017, he received an honorary degree from Queen's University. Mr. Smith is the Chairman and CEO of Smith Financial Corporation, which has significant equity investments in a range of financial services businesses: First National Financial Corporation, Canada Guaranty Mortgage Insurance Corporation, Fairstone Bank of Canada, Peloton Capital Management, Equitable Bank, Glass Lewis & Co. and Home Capital Group.
## Naming Celebration
### October 1, 2015

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=201502) 
 _https://smith.queensu.ca/news_blog/archive.php?a=201502_

[## Three weekends in January — Six Commerce Society events
](https://smith.queensu.ca/news_blog/2015/2015-02-09-ComSoc.php)
February 9, 2015
Kingston, ON — Feb. 9, 2015 - January is the Commerce Society’s busiest month, with six competitions and conferences attracting hundreds of business student delegates and competitors from around the world.
[## 2014 Voluntary Sector Reporting Awards winners announced
](https://smith.queensu.ca/news_blog/2015/2015-02-06-VSRA.php)
February 6, 2015
Toronto, ON — Feb. 6, 2015 - Canada’s most prestigious charitable financial reporting awards program has selected its 2014 winners. The Voluntary Sector Reporting Awards (VSRAs) announced five winners from 15 finalists from across Canada today at an awards luncheon in Toronto.

# [Class Giving Stories](https://smith.queensu.ca/invest/class-giving/class-giving-stories/index.php) 
 _https://smith.queensu.ca/invest/class-giving/class-giving-stories/index.php_

We are pleased to announce that Jane Hutchings, BCom'21, GDA'21 and 2020-21 recipient of The Commerce 1986 Award in Memory of Jeffrey Brock has been selected as a 2022 Newfoundland and Labrador Rhodes Scholar recipient, earning her a prestigious scholarship to the University of Oxford.
In honor of their 10th reunion, the Commerce Class of 2007 established The Commerce 2007 Award in Memory of Darren James Bishop, and we are thrilled to announce the activation of their award and introduce you to their inaugural recipient. The BCom’07s are our youngest commerce class to establish and activate and endowed award!
We had the opportunity to get insights from Michael Gilbert, BCom’78, who, with classmates Michael Kehoe and the late Gia Steffensen, ran the most successful class giving campaign in Smith history, raising over $1.6 million.
The Commerce Class of 1991 raised an astounding $800K and counting in honour of their 25th reunion.
In celebration of their 30th reunion, the Commerce Class of 1986 established the Commerce 1986 Award in Memory of Jeffrey Brock, who was the President of ComSoc in his graduating year. This award is given to a recipient in their third or fourth year of Commerce that demonstrates similar quality
More

# [ISF - Advisory Council](https://smith.queensu.ca/centres/isf/research/advisory-council.php) 
 _https://smith.queensu.ca/centres/isf/research/advisory-council.php_

## Research Advisory Council
The RAC is comprised of leading practitioners and academics in sustainable finance research and innovation. The council will meet twice per year to discuss and provide input on the focus of the Institute’s research.
The council’s role is to:
* Share expertise about research opportunities, engagement and collaboration.
* Suggest responses to research opportunities that advance the strategic objectives of ISF.
* Review and provide input on new research projects that advance the strategic objectives of ISF.
* Provide feedback on research activities carried out by ISF and its partners.
* Publicize and aid in the dissemination of research findings.
Dominique is the Chief Financial Officer and Head of Sustainability at Lithium Royalty Corp. Prior to this role, Dominique served as Head of Sustainability Advisory at CIBC Capital Markets. She joined the Capital Markets division after a ten-year tenure at CIBC Asset Management, where she was portfolio manager of several funds, including real estate and social responsible investing mandates. During that time, she also led CIBC Asset Management’s efforts to incorporate environmental, social, and governance factors into all investment processes. Dominique’s prior experience includes investment banking, research, institutional equity sales, audit, and corporate advisory services at several well-known, international financial institutions and accounting firms. Dominique has a Master’s of Business Administration in accounting from the University of Toronto and Bachelor of Science degree in Engineering (civil environmental) from Queen’s University. Dominique is also a CFA charter holder. Dominique is fluent in English and French.
Murat Basarir has been part of various international sustainable finance focused initiatives, such as launching UK’s first wireless charged electric bus and working at Canada’s first retail green bond issuer.
Prior to his work in sustainable finance, he has led a nationwide energy efficiency campaign that was voted by the UK public as the Best Campaign at the Climate Week Awards.
At TD, he works with teams across the enterprise to ideate, structure and move forward ESG initiatives that support TD’s Climate Action Plan.
Murat holds a BSc and MSc in Mechanical Engineering from Queen’s University and an MPhil in Engineering from Cambridge University and has completed the Ignite programme at Stanford’s Graduate Business School.
Patrick Bryden joined Scotiabank GBM in Calgary in 2010 and has worked in the securities industry since 1997.
Mr. Bryden became Head of Environmental, Social, and Governance (ESG) Research in 2020 and previously ranked first nine times in the annual Brendan Wood International and Greenwich Associates institutional surveys as an energy analyst.
Mr. Bryden served on the Natural Gas Expert Group for the Alberta Royalty Review and advised the Province of Alberta on the calibration of its Modernized Royalty Framework.
Mr. Bryden has raised more than $145,000 for the Movember Foundation and Ovarian Cancer Canada in his time at Scotiabank GBM. He has a Bachelor of Arts (Honours) degree from the University of Calgary and was awarded the CFA designation in 2001.
Prior to joining COFI, Linda was the Executive Director of the Pembina Institute. Her other roles prior to that was Chief Sustainability Officer for Enbridge Inc., Vice-President of Sustainability for the Vancouver 2010 Winter Olympic Games, Vice-President of the Pacific Region for World Wildlife Fund (WWF) Canada, and Vice-President of Environmental Affairs for the BC Coastal Group of Weyerhaeuser Canada.
Linda has also been a Distinguished Fellow at the Liu Institute for Global Issues at the University of British Columbia (UBC) and has taught corporate social responsibility at UBC’s Sauder School of Business. She has served on several advisory groups to different levels of government on climate and energy issues, including as a member of the City of Vancouver's 2009 "Greenest City" Task Force, the 2015 Advisory Panel to the Province of Alberta on Climate Leadership, and the 2018 Generation Energy Council to the Government of Canada. She was recently appointed to Canada’s Net-Zero Advisory Body, which provides independent advice to the federal government on meeting requirements under Canada’s new Net-Zero Emissions Accountability Act.
Andrew is the Managing Director, Carbon Markets Advisory at TD Securities. In this role, he is responsible for advising clients on capital markets solutions related to participating in and exposure to global carbon markets.
Prior to this, he worked at TMX Group as the Director of Sustainable Finance where he was responsible for developing and executing TMX’s enterprise strategy for ESG products and carbon markets. Andrew began his career in foreign exchange at Lloyds Bank.
Andrew has a BSc, and an MBA in finance from the University of Toronto’s Rotman School of Management.
Samantha Hill is a senior member of CPP Investments’ Sustainable Investing team, where she oversees activities to consider material environmental, social and governance (ESG) matters in engagements with public companies, primarily on climate change, water and human rights, and works alongside investment colleagues to integrate ESG matters into investment activities. This includes leading ESG diligence efforts globally for direct equity investments across asset classes. Samantha is also one of several individuals contributing to enhancing CPP Investments’ efforts to embed climate change-related considerations in investment and asset management activities and better understand the investment implications across the Fund.
Prior to joining CPP Investments in 2007, Samantha worked in multiple roles within CIBC’s Commercial Banking division related to senior debt financing for national accounts and real estate.
Samantha holds an MBA from Dalhousie University in Halifax, where she completed a double major in Finance and Environmental Management.
Pyarali is a London, UK based ESG and sustainable finance specialist with over 25 years of experience. Early in his career he worked at two Canadian banks before joining EY Corporate Finance Canada where he led the Renewable Energy and Cleantech practice and was a senior member of the Real Estate and Public Sector teams. He spent 10 years in the EY Transaction Advisory Services group in Canada, the EY Global offices and in the UK holding positions of VP, Global Network Coordinator, and COO & Director. Since leaving EY UK he has advised investors and operating businesses on governance, strategic planning, operations, ESG integration and transaction due diligence, and was CEO and COO of a London-based circular economy business. Pyarali also has fifteen years of experience on the boards of two UK impact investors. He's a member of the Sustainability Committee of the Institute of Chartered Accountants for England and Wales and of the Advisory Council for the Centre for Building Sustainable Value at the Ivey Business School. Pyarali holds an MBA from the Ivey Business School, a master of international affairs from Columbia University, and several diplomas and certificates including in ESG investing, sustainability, clean energy, and impact monitoring and evaluation.
Andrew Karolyi is Professor of Finance and holder of the Harold Bierman Jr. Distinguished Professorship in Management at the Cornell SC Johnson College of Business. He currently serves as Dean of the College.
His research specializes in the area of investment management with a focus on the study of international financial markets. He has published extensively in peer-reviewed journals in Finance and Economics and has published several books and monographs. His book, Cracking the Emerging Markets Enigma, was published in 2015. The research has garnered a number of prizes and recognitions. He is a past recipient of the Michael Jensen Prize for Corporate Finance and Organizations, the Fama/DFA Prize for Capital Markets and Asset Pricing, and the William F. Sharpe Award for Scholarship in Finance. In 2017, he was elected as a Fellow of the Financial Management Association International.
Professor Karolyi served as Editor and then Executive Editor of the Review of Financial Studies from 2011 to 2018, one of the top tier journals in Finance. He is a past president of the Western Finance Association, past president and trustee of the Financial Management Association, and currently a member of board of directors of the American Finance Association. He also serves on several not-for-profit boards, including the Pacific Center for Asset Management, the Responsible Research in Business and Management Network, and the United Way of Tompkins County.
Professor Karolyi received his Bachelor of Arts (Honors) in Economics from [McGill University](https://www.mcgill.ca/) in 1983 and worked at [the Bank of Canada](https://www.bank-banque-canada.ca/index.html) for several years in their Research Department. He subsequently studied for his MBA and PhD degrees in Finance at [the Graduate School of Business of the University of Chicago.](https://www.uchicago.edu/)
Dr. Majerbi joined Gustavson School of Business in 2004 after completing her PhD in finance at McGill University. Her research interests include international asset pricing, financial crises, investments and risk management. Her recent work explores the benefits of financial system diversity for sustainable development and financial stability, impact investing and climate-related financial risks. Her research has been published in leading business journals and benefited from major research grants from national granting agencies.
Basma is passionate about sustainable finance and impact investing and integrates these themes into core finance courses in her graduate teaching at the MBA and MGB programs. Since 2009, she has overseen the calculation of the annual carbon footprint of Gustavson faculty, staff and students leading the way to her school becoming carbon neutral in 2017. She is a past recipient of the Gustavson Research Excellence Award, the MBA Best Professor of the Year Award, Gustavson Innovation Award, and the Gustvason Award for Excellence in Service.
Basma is also a Technical Advisor with the International Monetary Fund’s Institute for Capacity Development where she contributes to training of government officials in developing countries on topics related to financial development, financial inclusion, and other financial sector issues. She is a member the steering committee of the Canadian Sustainable Finance Network (CSFN) and is co-founder and co-chair of the International Workshop on Financial System Architecture and Stability (IWFSAS), an annual conference that focuses on topics related to sustainable finance.
Cathy Matthews, B. Comm '86; CPA, CA; Chair, Board of Directors, Queen's AMS '86. Former Managing Director, Investment Banking, TD Securities, Toronto, Vancouver, New York & London with industry specialization in renewable energy and project finance. Former Strategy Consultant, National Bank Financial.
Recently, Queen's University Council Trustee, Queen's Board of Trustees; Queen's Capital Assets and Finance Committee, Queen's Climate Change Action Task Force; Queen's Chancellor's Search Advisory Committee; and, Queen's University Council Executive Committee. Past Volunteer Board Member; Council for Human Development, Camp Oochigeas & New Haven Learning Centre. Executive Education: Harvard; London Business School & Wharton.
As Vice-President of Research, Guidance and Support, Rosemary leads CPA Canada’s research and thought leadership strategy, ensuring the Canadian CPA profession is well-equipped to respond to challenges and to meet evolving business and societal needs. Rosemary oversees a team of professionals who explore emerging issues, champion innovation, and produce insights that guide future directions for the profession. She engages with Canadian and international stakeholders, such as policymakers, standards setters, regulators, and global accountancy bodies, on issues impacting the public interest. Key areas of focus include the path to net-zero emissions; environmental, social and governance (ESG) issues; and data and technology. Previously, Rosemary held the role of director, Research, Guidance and Support. During this time, she managed research and thought leadership initiatives related to external reporting and capital markets.
Rosemary has significant expertise in sustainability reporting and sustainable finance issues and has delivered presentations to the International Sustainability Standards Board, Canadian Accounting Standards Board, Canadian Securities Administrators, and the federal government’s Expert Panel on Sustainable Finance and Sustainable Finance Action Council. Throughout her career, she has also garnered extensive public accounting experience. She spent seven years in PwC’s National Accounting Consulting Services group advising clients on regulatory matters and complex accounting and financial reporting matters under International Financial Reporting Standards and U.S. Generally Accepted Accounting Principles.
Jon Mitchell is the Chief Sustainability Officer at Suncor where he leads a team accountable for the development, stewardship, and integration of sustainability into Suncor’s strategy. He is responsible for driving Suncor’s sustainability performance, managing strategic sustainability issues, advancing collaboration, and developing leading environment, social and governance (ESG) practices.
Jon has lectured on sustainability and climate issues, regularly speaks on the energy transition, and is a member of several Advisory Boards, including the implementation committee of the Canadian Sustainability Standards Board (CSSB) and the Canadian Chamber of Commerce Net Zero Council. Throughout his career Jon has had the privilege of advising industry and government on how to establish and sustain climate leadership among energy-producing jurisdictions; how to steward air, land, and water resources; best practices on ESG disclosure; and where to invest in clean innovation.
Jon holds a Bachelor of Science (Honours) degree from The University of Guelph and a Master of Environmental Design (Environmental Science) from The University of Calgary. He has worked in the environment, climate, and sustainability fields for over 25 years.
Deborah Ng is the Head of ESG and Sustainability at Grantham, Mayo, van Otterloo (GMO). Deborah is responsible for leading and accelerating the firm’s ESG and sustainability-related initiatives. Specific areas of focus include working closely with the firm’s investment teams as they conduct innovative research and further integrate material ESG factors into their processes; partnering with the Investment Stewardship Group to expand issuer engagement activities and advancing the firm’s own sustainability goals.
Prior to joining GMO in May 2022. Deborah was Head of Responsible Investing at the Ontario Teachers' Pension Plan. She was responsible for key deliverables across a number of pillars, including: ESG and climate change thought leadership and innovation, ESG integration frameworks and tools, and corporate engagement. Prior to this Deborah was part of the Strategy and Asset Mix team where she focused on the research, evaluation, and introduction of innovative asset allocation strategies that are designed to help meet the Plan’s long-term liability objectives.
Deborah sits on the Investment Committee of the United Church of Canada Pension Plan, and on the Research Advisory Board for the Institute of Sustainable Finance, Queen’s University.
Deborah has a Master of Finance degree from the Rotman School of Management, University of Toronto, where she received the Director’s Award. She is also a CFA charter holder.
Chad Park is the Vice President, Sustainability & Citizenship for The Co-operators. In this role he leads the co-operative’s efforts to embed and integrate sustainability principles throughout the organization, including in its investment strategy and underwriting practices.
He also oversees The Co-operators nation-wide community investment and partnership programs, including the Cooperators Community Funds.
Prior to joining The Co-operators in June 2020, Chad played a leadership role with several sustainability-focused organizations and initiatives. He served for five years as the Founding Director and Lead Animator of the Energy Futures Lab, a diverse coalition of innovators and partner organizations working together to advance solutions for a transformative energy vision for Canada.
He has also served as Executive Director of The Natural Step Canada, a founding Board-member for the Future Fit Foundation in the United Kingdom, and a Board member of the Canadian Energy and Climate Nexus. Chad earned his masters degree as a Rotary Ambassadorial Scholar at the International Institute for Industrial Environmental Economics at Lund University in Sweden and completed the Oxford Social Finance Programme at Oxford University’s Saïd School of Business.
Dr. Janis Sarra served as UBC Presidential Distinguished Professor from 2014 to 2019, an appointment by the President to recognize a faculty member that has made outstanding contributions as a scholar and academic leader. Prior to this appointment, Dr. Sarra served as Director of the Wall Institute for Advanced Studies at UBC. Dr. Sarra is Professor of Law at the Peter A. Allard School of Law and founding Director of the National Centre for Business Law. She served as Associate Dean of the Allard School of Law until 2007, with oversight of development, strategic planning, alumni relations and communications. Dr. Sarra is the Principal Co-investigator of the [Canada Climate Law Initiative,](https://ccli.ubc.ca/) a research collaboration between UBC and York University and is Canadian investigator of the [Commonwealth Climate and Law Initiative](https://commonwealthclimatelaw.org/) at Oxford University.
Dr. Sarra’s research and teaching interests are in the areas of corporate finance, climate-related financial risk and corporate governance, banking law, securities law, contracts, commercial insolvency law and law and economics. In 2004, she was awarded the title of Distinguished University Scholar for her scholarship in corporate and securities law. She has published ten books and more than one hundred refereed articles in climate governance, corporate finance, corporate governance and management, securities law and commercial insolvency law.
Dr. Sarra also served as Senator of the University of British Columbia from 2003 to 2008. She is a board member of the International Insolvency Institute and a director of Assuris. She was previously Director of the Canadian Insolvency Foundation, a director of the Canadian Insolvency and Restructuring Professionals Association and on the board of the British Columbia Law Institute. For more than twelve years, Dr. Sarra served as a commercial arbitrator and labour mediator/arbitrator.
Dr. Sarra’s contributions to public policy development include: member of the Canadian delegation of the United Nations Commission on International Trade Law (UNCITRAL) Working Group V, 2008-2020, Vienna and New York; World Bank Insolvency and Creditors Rights Task Force, Working Group on Insolvency of Non-Bank Financial Institutions, 2009, Washington, DC; Experts Committee, Expert Witness, Senate Committee on Banking Trade and Commerce, Review of Insolvency Legislation, February, 2008, Ottawa; Member, Ontario Attorney General's Interministerial Task Force on Administrative Tribunals.
Hillary Thatcher is Senior Director, Project Development, Indigenous Infrastructure. Hillary leads the CIB’s Indigenous relationships and opportunities to engage with Indigenous communities. She is part of the team offering advice and making investments consistent in CIB’s priority initiatives.
Previously Director General of Innovation and Services at Indigenous Services Canada, Hillary spent 15 years with the Ontario government in senior roles across Indigenous Affairs, Energy and Infrastructure, and Natural Resources. Hillary has a proven track record of building linkages among government, industry, and Indigenous interests.
Hillary is Métis and has been an active member of the urban Indigenous community of Toronto through her volunteer roles at the Native Canadian Centre of Toronto, Red Sky Performance, and the Downie Wenjak Fund. Hillary graduated from Concordia University in Montreal and the University of Victoria.
Richard Talbot is Chief Operating Officer, Investments at iA Investment Management, an asset manager with $100 billion under management. In this role, he is responsible for leading the implementation of a new strategic vision for an investment department where Responsible Investment is a key priority. Previously, Richard had a variety of senior leadership roles at RBC Capital Markets, a top-10 global investment bank including Chief Operating Officer, Co-Head of Global Research and Managing Director, Telecom Services Research.
Richard is the Co-Chair and Co-Founder of the Industry Standards Reporting Research Council, which works to create international standards for the reporting of alternative performance measures, a gap that is not covered by audited GAAP financial information. Within the local community, Richard is a board member of Second Harvest Food Rescue – an organization which is expanding beyond the greater Toronto area to become a national food rescue organization. He is also a board governor and Treasurer of Royal St. George’s College in Toronto.
Richard is a past director of RBC subsidiary companies, the CFA Society Toronto and currently chairs CFAST’s Advisory Council. He is a Chartered Professional Accountant with an FCPA, FCA designation and a Chartered Financial Analyst. Richard holds undergraduate and graduate degrees in business administration from the Ivey Business School.
Myha Truong-Regan is the Head of Climate Research at RBC’s Climate Action Institute. Prior to joining RBC, Myha was a senior economist with the Ontario Securities Commission (OSC), where her work was focused on regulatory strategy and research. Myha also had careers as an urban planner, where her focus was on environmental and social policy, and a strategy and marketing consultant, where her focus was on real estate development and consumer packaged goods.
Myha holds an MBA from the Rotman School of Management, at the University of Toronto, and Bachelor of Environmental Studies degree from the University of Waterloo.
John Uhren is Head, Sustainable Finance, Products and Strategy, at BMO. He leads product development and strategic initiatives across the enterprise, including raising capital and providing sustainable finance opportunities to clients. John is also a member of BMO’s Energy Transition Group and the CSA Group’s Transition and Sustainable Finance Technical Committee.
Prior to joining the Sustainable Finance team, John was Senior Counsel and Director in Capital Markets Legal at BMO. John was co-head of BMO’s Pro Bono Committee, and in 2017 won Lexpert’s Rising Star Award as a top Canadian lawyer under 40.
John founded Feet Forward Organization in 2013, a Canadian registered charity that partners with NGO agencies in South Africa to assist refugees, asylum-seekers and newly landed immigrants. He is currently a board member of Dress for Success Toronto.
As the CFO, Davinder is responsible for ensuring Peel remains financially sustainable while continuing to deliver a suite of cost-effective and responsive business services to support the organization.
Davinder has worked at the executive leadership level since 2006. She comes to Peel Region from the Chartered Professional Accountants of Canada where she was the Executive Director, Accounting for Sustainability (A4S) Canada and Director, Strategy, Risk and Performance Management. In this role, she led a team to conduct technical research on emerging and current issues related to the disruptors of technology, economy, sustainability, finance, strategy and risk and their impact on society, business and governments. Davinder also managed large private and public CFOs to incorporate sustainability into everyday decision-making and led the A4S network of CFOs in Canada and abroad to address global finance challenges. Davinder's past roles include Director, Global Infrastructure Advisory, KPMG LLP, and Director, Strategic Oversight and Partnership Management and Director of Strategic Planning and Stakeholder Relations, Ontario Power Generation.
A Chartered Professional Accountant, Davinder holds an Honours Co-op Bachelor of Arts in Chartered Accountancy from the University of Waterloo and the Executive Leadership Program diploma from the Schulich School of Business. She actively contributes to several boards and organizations including the Institute for Sustainable Finance, the Women in Energy Transformation Series, Capitals Hubs Canada and BGC Canada.
Erica Wieder is Manager of Investor Relations at the Ontario Financing Authority (OFA), the crown agency tasked with conducting borrowing, investment and financial risk management for the Province of Ontario.
At the OFA, Erica develops multi-faceted strategies to drive investor engagement to promote Ontario’s bonds to institutional fixed income investors domestically and abroad. Erica has been involved in Ontario’s Green Bond program, currently the largest in Canada, since its inauguration in 2014. She leads the Province’s Impact Reporting through the publication of an annual Green Bond newsletter, helping advance the program and distinguish Ontario as a leader in impact reporting with wide recognition in Canada and abroad.
Erica also spearheads the Green Bonds dedicated space on the OFA website, which is well recognized throughout the industry, and other marketing initiatives. Previously, Erica worked in policy development at the Insurance Bureau of Canada (IBC), the industry association representing the property and casualty insurance industry in Canada, and an investment bank in Argentina. Erica holds an M.A. in Economics from Western University (UWO), and a B.A. in Economics from the University of Buenos Aires.

# [CEISI - Our Team](https://smith.queensu.ca/centres/ceisi/our-team.php) 
 _https://smith.queensu.ca/centres/ceisi/our-team.php_

## Elspeth Murray 
Director
[elspeth.murray@queensu.ca](mailto:elspeth.murray@queensu.ca)
Elspeth Murray has served as the Associate Dean - MBA and Master’s Programs from 2012-2022 and has been a professor of Strategy and Entrepreneurship at Smith School of Business since 1996. She also holds the CIBC Fellowship in Entrepreneurship, and founded Smith's Centre for Business Venturing. She is the Director of the Centre for Entrepreneurship, Innovation & Social Impact.
Prior to joining Smith, she worked in industry for 7 years for several firms including IBM, and Canadian Tire. As an integral part of her work in the strategy and new venture fields, Dr. Murray specializes in the management of change.
## JP Shearer 
Associate Director
[john-paul.shearer@queensu.ca](mailto:john-paul.shearer@queensu.ca)
JP Shearer is Associate Director of the Centre for Entrepreneurship, Innovation & Social Impact, working to accelerate the success of entrepreneurs, intrapreneurs, and innovators.
JP has spent much of his time at Smith School of Business dedicated to the development of excellence in people through coaching and mentoring. In addition to his current role, he is an academic advisor to the Full-time MBA, MBA Americas and Executive MBA programs.
JP holds an Executive MBA (2003) from the University of Glasgow, Scotland.

# [Support for ESG expertise at Smith](https://smith.queensu.ca/yearinreview/features/esg-expertise.php) 
 _https://smith.queensu.ca/yearinreview/features/esg-expertise.php_

Feature
A $2.5-million alumni gift promises to have a profound impact on environmental, social and governance education for students
Mike Quinn, BCom’88, and Francisca Quinn believe it is critical for the next generation of business leaders to understand climate change and sustainable development concepts.
That’s why in April 2023 they made a $2.5-million gift through The Quinn Family Future Foundation to establish the Quinn Environmental, Social and Governance (ESG) Professorship at Smith.
The gift will enable the school to hire an ESG scholar who will play a leadership role in the development of the ESG curriculum across programs to further develop the next generation of business leaders.
“Revitalizing our curriculum will better prepare our students to positively contribute to an inclusive, diverse and sustainable society,” says Wanda Costen, dean of Smith School of Business. “Smith is a key provider of talent for today’s businesses, so we must offer exceptional learning experiences to equip students to be fluent in sustainability concepts and strategy.”
Francisca Quinn and Mike Quinn, BCom’88
Sustainability is already a key strategic goal at Queen’s. The university is committed to furthering the United Nation’s 17 Sustainable Development Goals (SDGs). Queen’s was recently ranked in the top 10 of the [_Times Higher Education_ (THE) Impact rankings,](https://www.queensu.ca/gazette/stories/queen-s-maintains-top-10-global-position-times-higher-education-impact-rankings) which measured the actions of more than 1,500 post-secondary institutions that are trying to advance the UN’s SDGs.
The Quinns have dedicated their careers to sustainable development. Francisca is the president and founder of [Quinn+Partners](https://www.quinnandpartners.com/) (a North American environmental, social and governance advisory firm) and Michael is the co-founder of [RP Investment Advisors LP.](https://rpia.ca/our-firm/our-team/bio/mike-quinn)
“Climate change and social issues are not only significant threats to Canadian business, they can also be tremendous opportunities for organizations and entrepreneurs,” says Francisca Quinn. “We want to equip every student at Smith to expertly navigate ESG, whether in business strategy, accounting, finance, technology or organizational systems.”
Mike Quinn’s Commerce degree benefited him tremendously in his career and he is happy to help his alma mater by giving back. “I’m very honoured and excited to be able to contribute to Smith School of Business writing its next chapter,” he says.

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=202105) 
 _https://smith.queensu.ca/news_blog/archive.php?a=202105_

[## Miele-Smith case competition offers students unique opportunity
](https://smith.queensu.ca/news_blog/2021/2021_Miele_Smith_Case_Competition.php)
May 6, 2021
Kingston, Ont. – Smith School of Business students from across all programs were invited to compete in the inaugural Miele-Smith virtual case competition this spring. Over 150 Smith students signed up to develop innovative ideas to a challenge presented by the appliance manufacturing company.

# [CEISI - Overview](https://smith.queensu.ca/centres/ceisi/founders-pledge/index.php) 
 _https://smith.queensu.ca/centres/ceisi/founders-pledge/index.php_

## Founders’ Pledge
Support the next generation of entrepreneurs, intrapreneurs, and innovators at Smith School of Business and help accelerate their success.
## What is the pledge?
Make a personal commitment to support Smith once your business has taken off or you have a successful exit. Sign up for the pledge and when you’re ready, we’ll work with you to determine the right time and amount for your gift. Together, we’ll also help you decide where best to direct your gift at Smith to achieve your desired impact.
## Why pledge?
Your gift will help support excellence in education and increase the odds of success for future entrepreneurs. Join the community of Smith alumni who have already pledged their commitment to support the school. By thinking about your future giving at an early stage, you’re inspiring others to do the same and helping our Smith entrepreneur network thrive.
## Founders’ Pledge Members
**Somen Mondal, MBA’06** 
_Chair,_ Smith Founders’ Pledge 
_GM, Talent Intelligence,_ Ceridian 
_Co-founder and CEO,_ ideal (acquired) 
_CEO,_ Field ID (acquired) 
[@somenmondal](https://twitter.com/somenmondal?lang=en)
**Tom Kinnear, BCom'66, LLD'02, PhD** 
_Honorary Chair,_ Smith Founders’ Pledge 
_Serial Entrepreneur and President,_ Venture Michigan Fund
**Travis Ratnam, MBA’11** 
_Co-founder and CEO,_ Knowledgehook Inc. 
[@knowledgehook](https://twitter.com/knowledgehook?lang=en)
**Marcus Daniels, AMBA’05** 
_Founding Partner and CEO,_ Highline BETA 
[@marcusdaniels](https://twitter.com/marcusdaniels?lang=en)
**Robbie Mitchnick, Ryan Peterson, Cord McGee, Donald Gawel, all BCom’13** 
_Co-founders,_ Q4Q Beer Company Ltd 
[@thenaughtyotter](https://www.instagram.com/thenaughtyotter/?hl=en)
**David Jackson, BCom’91** 
_Owner and CEO,_ Hydropool Hot Tubs and Swim Spas 
[@Hydropool](https://twitter.com/hydropool)
**Mitch Gudgeon, MBA’13** 
_Co-Founder & CEO,_ TalentFit AI 
[@TalentFit\_me](https://twitter.com/talentfit_me)
**Jacie DeHoop, BCom'14; Ellen Hyslop, BCom'14; and Roslyn McLarty, BCom'14, GDA'14** 
_Co-Founders,_ The Gist
**Evan Hall, BScH’11, MBA’17** 
_CEO & Co-Founder,_ Wittaya Aqua 
[@WittayaAqua](https://twitter.com/wittayaaqua)
**Peter Willson, BSc(Eng)'92** 
_Chairman and CEO,_ Willson International 
[@WillsonInt](https://twitter.com/WillsonInt)
**Ahmed Shehata, BCom’03** 
_General Counsel and Head of Corporate Development,_ MediPharm Labs
**Lisa Orr, BCom'10, AMBA'16** 
_Founder and Designer,_ LaBroga 
_Founder,_ Orr Etiquette
**Jake Dancyger, BCom'15** 
_Co-CEO,_ Clariti
**Cyrus Symoom, BCom'15** 
_Co-CEO,_ Clariti
**Josh Barr, BCom’10** 
_Co-Founder,_ brüst
**Robin Kovitz, BCom’02** 
_President & Co-Founder,_ Baskits Inc.
**Mark Balovnev, BCom’19** 
_Co-founder and CEO_, Educhain (acquired)
**Karn Saroya, BCom’08** 
_Co-founder & CEO_, Cover
**Natalie Gray, BCom'09** 
_Co-founder, Product & Design,_ Cover
**Jenny Lemieux, MMAI’20** 
_Co-founder & CEO_, Vivid Machines

# [MMAI - Overview](https://smith.queensu.ca/grad_studies/mmai/index.php) 
 _https://smith.queensu.ca/grad_studies/mmai/index.php_

### Now a Pathways University for MITx MicroMaster in Statistics and Data Science.
## Master of Management 
in Artificial Intelligence
Beginning each year in May, Smith's Master of Management in Artificial Intelligence allows you to earn a world-class degree in just 12 months without leaving your current job.
The potential of artificial intelligence is extraordinary. The power to transform operations, customer experiences, and product and service design is exponential. These opportunities cut across every sector.
Harnessing AI’s potential for competitive performance requires a new type of professional. One who not only understands the capacity of the science, but has the expertise to apply it to organizational needs and strategies, and who can navigate the ethical, economic and societal implications.
### This program is for:
**Emerging Enthusiasts:** These young MMAI students are taking their first steps into AI and analytics, bringing fresh perspectives and a thirst for knowledge. They often pursue roles like Data Scientists, Data Consultants, or AI Innovators. They come from different educational background, from STEM/CS or Business.
**Career Changers/Catalysts:** This diverse group, including Career Catalysts and Career Changers, is on a mission to reshape their careers with AI. They aspire to excel as Manager-Data Science, Senior Data Scientists, or AI Strategists. They come from business and commerce background — sometimes from Arts as well.
**Career Shapers:** Students in this category actively craft their professional paths within Analytics or AI, blending existing experience with MMAI's knowledge. They frequently ascend to positions like Director of Data Science, Analytics Architects, or ML Pioneers. Mostly from CS, Math, Stats, Physics background — sometimes from Medical background as well.
**Visionary Pioneers:** Seasoned professionals with substantial expertise who aspire to lead AI innovation and drive industry transformation, often found in VP and C-suite roles as AI Visionaries. Come from all backgrounds with a strong experience of over 15 years.
Smith's MMAI program is recognized by the [Vector Institute](https://vectorinstitute.ai/) for Artificial Intelligence as delivering a curriculum that equips its graduates with the skills and competencies sought by industry. All students are eligible for [Vector Institute Scholarships](https://vectorinstitute.ai/aimasters/) valued at $17,500.
### New Scholarships Available
Smith School of Business introduces scholarships for Black students and Indigenous students in all MBA, Professional Masters, and Graduate Diploma programs.
## Key Features
### Skills Coverage
Provides the critical mix of analytics capabilities with strategy and business management expertise in order to lead projects, business units, and organizations.
[View the curriculum](https://smith.queensu.ca/grad_studies/mmai/program/)  
### Expert Leadership
Learn from our expert faculty who are some of the best management educators in the world and industry specialists and practitioners who teach from real market experience.
[Meet the faculty](https://smith.queensu.ca/grad_studies/mmai/program/faculty.php)  
### Advisory Board
Dedicated analytics advisory board ensures alignment of the program content to business needs, and contributes insights and networking opportunities for students.
[Meet the advisory board](https://smith.queensu.ca/grad_studies/mmai/advisory-board.php)  
### Real World Data
Class discussions and assignments use corporate data sets, allowing you to identify real insights and make better decisions.
### Scotiabank Centre for Customer Analytics
Brings together faculty, students, and practitioners to collaborate on applied research projects as well as events, conferences, workshops, and competitions.
### Special Events
Special speakers, events, business networking, coaching and career support is provided throughout the program.
## Smith Analytics & AI Advisory Board
Our dedicated analytics advisory board ensures alignment of the program content to business needs, and contributes insights and networking opportunities for students.
**Mark Shafer**
_Senior Vice President, Decision Science & Integration_ 
Walt Disney Parks and Resorts
**Pavel Abdur-Rahman**
_Managing Director_ 
Bluevale Capital Group
**Jane Ho**
_AVP, Enterprise Data & Analytics Strategy_ 
TD Bank
**Lori Bieda**
_Chief Data and Analytics Officer, North American Personal and Business Bank_ 
BMO
> “The MMAI program elevates knowledge and skills in management and Artificial Intelligence to drive change and influence the strategic direction of organizations. The program’s curriculum and faculty prepare future AI leaders to stay abreast of rapidly growing AI technology and build key foundations in ethics, strategy, and innovation. The MMAI network, including the leading AI faculty members, are individuals with a passion for AI, and the knowledge sharing continues even after graduation.”
Theebak Sothilingam, MMAI 
Manager, Data Science 
Intact Data Lab (R&D)

# [Goodes Hall Benefactor Wall](https://smith.queensu.ca/invest/recognition/goodes-hall-wall.php) 
 _https://smith.queensu.ca/invest/recognition/goodes-hall-wall.php_

The Goodes Hall Benefactor Wall recognizes all donors who have contributed $10,000 or more to Goodes Hall, including gifts toward the original construction of the building in 2002 as well as the 2012 west wing expansion. This wall is located in the original Goodes Hall building and celebrates the commitment of donors to ensuring that Smith students, faculty and alumni have access to a world-class facility that continues to be outfitted with the latest in teaching and learning technology.
Contributions are recognized at the following levels:
* Level 1: $1,000,000 +
* Level 2: $500,000 - $999,999
* Level 3: $250,000 - $499,999
* Level 4: $100,000 - $249,999
* Level 5: $10,000 - $99,999

# [ISF - Mandate](https://smith.queensu.ca/centres/isf/mandate.php) 
 _https://smith.queensu.ca/centres/isf/mandate.php_

## Institute for Sustainable Finance
The Institute for Sustainable Finance is the first-ever cross-cutting and collaborative hub in Canada that fuses academia, the private sector, and government with the singular focus of increasing Canada’s sustainable finance capacity. The institute's mission is to align mainstream financial markets with Canada’s transition to a prosperous sustainable economy.
By investing in education, professional training, research, and partnerships, we will help to create the critical conditions for Canadian leadership on sustainable finance – at home and abroad.
Housed at Smith School of Business at Queen’s University, the Institute will fill the gap of relevant data, expertise, and business-oriented solutions for sustainable finance. By aligning financial knowledge and tools with climate change imperatives, we will foster Canada’s leadership in the shift to a low-carbon global economy.
## Our Focus
### Research
Generate innovative and relevant research on sustainable finance and effectively communicate this research to all pertinent stakeholders.
[Learn more about research](https://smith.queensu.ca/centres/isf/research/index.php)  
### Collaboration
Serve as a platform for collaboration between government, academia, and industry.
### Outreach
To be visible in sustainable finance issues and to clearly and effectively communicate the relevance of sustainability developments to the market.
## Progress & Impact Reports
The Institute for Sustainable Finance’s Progress & Impact Reports provide a thorough annual review of the ISF’s activities and achievements across the four pillars of Research, Education, Collaboration and Outreach.
## A Critical Opportunity for Canada
Canada is warming twice as fact as the rest of the world, according to the federal government’s 2019 climate report. We are at a pivotal moment when we can both protect our markets and investments from risk while refocusing them to tap into new and unprecedented opportunities.
The transition to a low-carbon economy is already underway. Global players are currently leading on sustainable finance, defining the tools and writing the rules that will determine how capital flows. Canada has the means and the opportunity to be an innovation shaper – not taker – to inform these decisions to benefit our economy.
The [Canadian Expert Panel for Sustainable Finance’s 2019 report](https://www.canada.ca/en/environment-climate-change/services/climate-change/expert-panel-sustainable-finance.html) makes a clear call for authoritative and decision-useful climate information and a supportive and climate-informed ecosystem of professional services providers.
Closing this innovation gap will ensure we catch up and protect Canada’s economy from risks, while capitalizing on increased opportunities for growth and prosperity.

# [Can Investing Drive Social Impact? | Smith Business Insight](https://smith.queensu.ca/insight/content/Can-Investing-Drive-Social-Impact.php) 
 _https://smith.queensu.ca/insight/content/Can-Investing-Drive-Social-Impact.php_

**What role can private investment play** in addressing social problems? Should it be involved at all? 
These are big questions that touch on several of today’s most relevant business issues: increasing environmental, social and governance (ESG) expectations, heightened interest in sustainable finance, changing attitudes towards public policy, and the very role of business in society. 
They’re questions Wenjue Knutsen thinks about a lot. As an associate professor who studies non-profits and social enterprises for both Smith School of Business and the Queen’s University School of Policy Studies, she’s noticed growing interest over the last decade in what’s broadly known as “social impact investing”—generally speaking, the practice of directing private capital to public good, with the expectation of returns. 
In conversation with contributor Deborah Aarts, Knutsen explains how social impact investing works and why its promise of a “blended return” is gaining currency.  
**What exactly are we talking about when we discuss social impact investing?** 
Essentially, social impact investing is a financing tool that provides funds or investments to social enterprises, which is a big umbrella term that refers to organizations that simultaneously pursue business and social impact activities. 
Some of these are non-profits that require income to achieve financial sustainability and independence; others are for-profit businesses that generate revenue from products or services that further a social mission, such as a company that sells organic fertilizer. What unites them is their focus on a double bottom line: the nature and extent of the investor’s returns often depends, at least in part, on the recipient organization’s ability to deliver on its social mandate.
That’s part of what makes it so exciting to me: Traditionally, most investors are in the game to get a financial return, first and foremost. Here, it’s a totally different animal. They’re also looking at the social mission and the social impact of the organization they’re funding. 
**Can you give me an example of what this looks like in practice?** 
Sure! Social impact investments can be led by pretty much any investment institution, from fund managers to financial institutions to family offices. 
A good example that comes to mind is based in Brazil. In 2009, a group of socially-minded young entrepreneurs there started an organization called [Vox Capital](https://store.hbr.org/product/vox-capital-pioneering-impact-investing-in-brazil/417051?fromSkuRelated=SKE189&ab=store_idp_relatedpanel_-_vox_capital_pioneering_impact_investing_in_brazil_417051), with the promise of a “blended return.” They raised money for the fund from banks, private investors and families with similar values. They then made a series of 20 investments in startup social enterprises working to fundamentally change peoples’ lives, through improving such things as health care, housing and education. 
What makes this different from typical ethical investing funds can be seen through the nature of the returns: For example, a significant proportion of the fee that Vox draws is dependent on whether investees have reached measurable targets related to social impact. This shows social impact investing’s commitment to social causes. In comparison, the primary objective of ethical investing or socially responsible investing is still financial returns. 
**This sort of funding clearly fills a gap, but what’s really in it for investors? Is it just the warm and fuzzy feeling that comes from doing good?** 
It can be helpful to think of it in financial terms, but in a different way than you might think. Say you’re financially secure, with an annual budget set aside for doing good in the world. If you make a donation, that money is gone for you, aside from a small amount you’ll get back on your tax return. It’s a one-time, one-way transaction. 
But if, instead, you divert that money into a social impact investment fund that supports organizations doing social good, you stand to not only keep your principal but, hopefully, to make a return on it. Your money can therefore also be recycled and used repeatedly. You can help one group of people now, and another in the future, and so on.  
**The issue of returns is intriguing. Your work cites** [**a 2020 survey of social impact investors**](https://thegiin.org/publication/research/impinv-survey-2020/)**, in which a majority said they expect returns at or close to market rates. But skeptics might counter that it’s unrealistic to expect competitive returns while also prioritizing social impact—that some trade-off is inevitable. What do you think is a reasonable return for investors in the social impact space?** 
Research in the social impact investing space is still limited, so we don’t have aggregated data, but we can point to individual cases. For example, with Vox Capital in Brazil: A few years into operations, their goal for returns was the rate of inflation, plus six per cent. They also suggested that, perhaps, a return of four per cent would be too low, but 20 per cent would be too high. But it depends on what kind of organizations the investment is supporting. 
There are definite risks in this space. And, as with all investments, there’s a chance that the financial return will be zero. And you have to be honest about this possibility. But the difference here is that a social impact investor does not just look at the numbers. They balance the financial risk with what they’re looking for in terms of social impact. 
**This is the kind of thing that would once have been considered a niche investment strategy. Do you see interest in social impact investing growing beyond that?** 
Yes. In fact, late last year, the [Global Impact Investing Network](https://thegiin.org/) estimated the size of the worldwide impact investing market to be US$1.164 trillion, the first time that figure has topped the US$1 trillion mark. It’s still not fully mainstream yet, but it’s playing a bigger role in our economy. 
**Why do you think that is?** 
There are several reasons, but three main ones come to mind: First, lots of people say our society’s going downwards. But I think our business world is definitely going upwards, at least in terms of developing conscientiousness related to social impact. You can’t find a big-name company that does not have a corporate social responsibility practice. That’s a big change.
Second, we’re moving to a place where blended values—mixing profit and social good—are becoming more and more common. People are looking for meaning in their life and in their work. 
Third, our society has a lot of unfulfilled gaps related to social issues. People are aging and we have higher demands related to our quality of life. That’s when social impact investing can try to take off some of the pressure. 
**Related to that point: You’ve also looked at social impact bonds (SIBs), in which investor groups raise money and fund agencies and non-profits to provide new types of social services on behalf of governments. At first glance, this seems to be privatizing what should be a public responsibility. Is it really?** 
No, I don’t think so. SIBs are complicated, but I think of them as a way for investor groups to fund a pilot project for the government. These tend to be intervention or preventative services, like initiatives meant to prevent people from committing crimes or entering the foster-care system. 
The investor group can fund a project, and if the agency providing services hits an established target—say, 22 out of 30-ish at-risk children in a preventative program stay with their mothers, as was the case with the [Sweet Dreams](https://innovationsask.ca/news/the-sweet-dreams-initiative) initiative in Saskatchewan, the first SIB in Canada—the government will reimburse basically all the money that the private investor put forward, plus, usually, a percentage return. But if they don’t hit the target, that means the project doesn’t work—the pilot failed. The investor may be out of its money, but the government is not. In fact, it has just saved a lot more money by not implementing a program that doesn’t work broadly. 
So the SIB is not filling a gap in the social safety net with private interests, so much as it is giving governments a chance to lessen their risk around new approaches to delivering social services, and, if successful, to lower participation in—and costs related to—systems like foster care and justice. 
**Got it. Finally: Let’s pretend I’m a hard-nosed Milton Friedman devotee who believes the purpose of business is to make money, and nothing else. What’s your pitch to make me care about social impact investing?** 
Here’s what I’d say: What’s the purpose of your life? What’s the purpose of your business? Is it really just about wanting more money? Isn’t that getting boring? 
A lot of people get into social impact investing because they’re looking for meaning. And it doesn’t have to be hard. There are lots of ways you can make a social impact without you lifting a finger. All you need to do is put the money with somebody who will do the work for you. 
Think about what you care about the most in this world. Think of the social impact your investments could make towards that. You may be able to do a lot more with social impact investing than with traditional philanthropy. So I’d say: Think cautiously, think carefully, but really think about it.
Tags:

# [Invest](https://smith.queensu.ca/invest/index.php) 
 _https://smith.queensu.ca/invest/index.php_

## Invest in Smith
In the age of COVID-19, the world has shifted rapidly, with uncertainty and disruption across all aspects of Higher Education, including teaching and research. We have had to change how we provide learning and conduct research at an extraordinary pace and scale. At Smith, we thank all our supporters for their leadership in helping us continue to engage in teaching excellence and research.
Borden Chair of Leadership, and Professor of Organizational Behaviour, Smith School of Business.
Smith School of Business is committed to ensuring access to all students with the talent and potential to lead and succeed in business, contribute to their communities, and positively impact society on a broader scale. Having the resources to offer financial support to those students through admission bursaries and awards is vital to upholding that commitment. The Commerce Bursary Fund ensures Smith is better able to recruit a wide array of exceptional students with the diverse perspectives, skills, and capabilities needed to succeed in business. Through the support of our alumni and friends, we are able to ensure talented students with financial need have access to the best resources, education and unparalleled opportunities possible to explore, and reach, their full potential.
## Investment Priorities

# [ISF - Advisory Board](https://smith.queensu.ca/centres/isf/advisory-board.php) 
 _https://smith.queensu.ca/centres/isf/advisory-board.php_

The Advisory Board was created to establish and drive the Institute’s mission and to identify the potential for collaboration with other engaged parties across the country. It includes a mix of practitioners and academics.
Roger is a member of the Young Presidents’ Organization, a Trustee of the Douglas University Institute for Mental Health Foundation and a Director of the Cedars Cancer Foundation.
Currently serving as the President and Chief Executive Officer of Addenda Capital, he is responsible for the development and deployment of the company’s business strategy and operations. He joined Addenda Capital as Chief Operating Officer and Chief Financial Officer in 2013, before being appointed President and Chief Operating Officer in 2015.
He previously worked at McLean Budden Limited (1999 to 2011), holding several senior management positions before being appointed President in 2006 and Chief Executive Officer in 2008.
Tabatha is the President and CEO of Canadian Council for Aboriginal Business. She is an Anishnaabe Kwe from Nipissing First Nation. As CCAB’s president and CEO she is committed to help rebuild and strengthen the path toward reconciliation and a prosperous Indigenous economy to benefit all Canadians. With a focus on Indigenous economic development, Tabatha often works with various heads of organizations, companies, government officials and departments, notably her role with the federal government’s COVID-19 Supply Council. She serves the Indigenous community through her commitment, duty, and support to Indigenous business and the economy. An electrical engineer, Tabatha informs Canada’s energy sector by participating on the boards of Ontario’s electricity system operator IESO, the Positive Energy Advisory Council, the MARS Energy Advisory Council, and the C.D. Howe Institute’s Energy Policy program.
A member of several other boards and committees, including Queens University Engineering Circle of Advisors, Centennial College Aboriginal Education Council, Wigwamen Housing, and the Ontario Chamber of Commerce, Tabatha is dedicated to diversity and removing systematic barriers to improve opportunities and business competitiveness across all industry sectors.
Recently appointed to the Catalyst CEO advisory board in Canada, Tabatha collaborates with some of the world's most powerful CEOs and leading companies to help build workplaces that support women.
Tabatha is a proud mom of two boys and can often be found in a hockey arena, at the baseball diamond, or on the lacrosse field.
Andy is a member of the Board of Directors of Royal Bank of Canada. Prior to that he spent most of his career at Goldman Sachs & Co, which he joined in 1985 in New York. He served in a variety of progressively more senior leadership roles within the organization during his 30-year career including as Senior Strategy Officer of the firm globally from 2012 – 2014, as Head or co-Head of the Global Financial Institutions Group in both London and New York from 2002 – 2012, and as co- Chair of the Firmwide Commitments Committee (primarily overseeing the firm’s equity underwriting activities) from 2011 – 2015.
He is currently a member of the Federal government’s Expert Panel on Sustainable Finance. He holds a B. Comm from Queens University (1981) and graduated with an MBA from the Ivey Business School at Western University in 1985. He is Chair of the Ivey Business School Advisory Board, is a Board Member of Evergreen, and sits on the Advisory Board of ArcTern Ventures. He lives in Toronto with his family.
Alexandra Conliffe is the Chief Executive Officer at the McCall MacBain Foundation. She has previously served as the Vice President of Philanthropy and Organizational Learning and for more than a decade in building and implementing programs and public policy in the non-profit and public sectors, with a focus on environment and global development. Her contributions range from her role as Canada’s agriculture negotiator at the United Nations Climate Change negotiations while a Senior Policy Analyst at Agriculture and Agri-Food Canada to studying the impacts of environmental and climate change on rural livelihoods in Uzbekistan through her doctoral research.
Prior to joining the Foundation, Alex was Director of Policy Innovation at the Brookfield Institute for Innovation + Entrepreneurship and VP Operations at Engineers Without Borders Canada. She holds a PhD in Geography and an MSc in Environmental Change and Management from the University of Oxford, where she studied as a Rhodes Scholar. Alex obtained a BEng from McGill University, where she studied as a Loran Scholar. She is a member of the McGill Engineering Faculty Advancement Board.
Ehren Cory bring his strong leadership approach, infrastructure expertise and track-record of delivering results by partnering with the private and public sectors to the Canada Infrastructure Bank (CIB).
As Chief Executive Officer, he is focused on the CIB’s strategic direction including implementing the $10B Growth Plan to accelerate infrastructure investment in Canada and building the CIB as a results-oriented organization.
Prior to joining the CIB, Ehren was the President & CEO of Infrastructure Ontario, a Provincial Crown Agency responsible for financing, building, and enhancing the value of the province’s infrastructure and real estate assets. In addition to his four years as CEO, he also spent four years with the Agency in executive roles responsible for the successful transaction structuring, tendering, and delivery of billions of dollars in infrastructure projects.
Prior to joining Infrastructure Ontario, Ehren was a partner at McKinsey & Company in Toronto, where he served as a leader in the Public Sector and Capital Projects practices, advising clients in both the private and public sectors. Ehren is a graduate of the MBA program at INSEAD in Fontainebleau France, where he graduated with distinction. He also received an Honours degree in Business Administration (HBA) from the University of Western Ontario.
Nicolina is Program Director at the McConnell Foundation since 2014. She is involved in many key portfolios, including their focus area on net-zero and inclusion and sustainable finance work. She is also contributing to their strategy for communities' resilience, mental health collaborative projects and specific investments in the Montreal area where McConnell is based. She sits on the board of Imagine Canada and is part of the Public policy committee. Prior to working at the Foundation, she was Science and Innovation Officer with the British Consulate-General in Montréal. She also coordinated Ashoka Canada’s fellow selection process and worked as a consultant to several environmental and international development organizations. She has a PhD in environmental sciences, on the links between farming practices, deforestation and eco-health in Brazilian Amazonia.
Jonathan Hackett is the Co-Head, BMO Energy Transition Group and Head, Sustainable Finance and Managing Director. In these roles he advises clients on opportunities as they navigate the transition to a low carbon economy, supports clients in navigating the impact of ESG on their access to capital, and advises on sustainable financing structures. Jonathan’s team also includes BMO’s $250MM impact investment fund which has a mandate to invest in companies that are producing solutions in the sustainability and energy transition space. Prior to joining BMO in 2017, Jonathan was a principal with the Boston Consulting Group and also a researcher in residence at the Perimeter Institute for Theoretical Physics where he completed his doctoral research in Quantum Gravity and Topology.
Yrjo Koskinen the BMO Professor of Sustainable and Transition Finance at the Haskayne School of Business. He served as the Associate Dean of Research and Business Impact from 2017 to 2022. He has previously been a faculty member at Stockholm School of Economics, Boston University’s Questrom School of Business, and the Wharton School of the University of Pennsylvania. He holds an MSc degree in Economics from the University of Helsinki, and a PhD in Management (Finance) from INSEAD. Prior to his academic career,  Yrjö worked as a financial journalist, asset manager and as an economist at the Bank of Finland.
Yrjo currently serves on the advisory board of the Institute of Sustainable Finance at Queen’s University and on the steering committee for the Canadian Sustainable Finance Network. He is also a fellow at the Nordic Initiative in Corporate Economics and a research member at the European Corporate Governance Institute. He is the past co-president of the Northern Finance Association.
Yrjo’s main research areas are corporate finance and governance, and sustainable finance. His current research focuses on environmental, social and governance (ESG) issues and how they affect trading and prices in financial markets. His research has been published in the leading finance and management journals, such as the Journal of Financial Economics, Review of Financial Studies, Management Science, Journal of Financial and Quantitative Analysis, and Review of Finance. He is the recipient of the Standard Life Investments Finance Prize for his research on corporate social responsibility and firm risk.
Kikelomo Lawal is the global leader for CIBC’s Legal, Corporate Secretary, Ombudsman and Privacy Office functions, and related policies and programs. She is also responsible for leading the development of the environmental, social and governance strategy across the bank. Kikelomo has 25 years of progressive leadership experience, including legal expertise as both a trial lawyer and a transactional lawyer.
Prior to joining CIBC, Kikelomo was Chief Legal Officer, Ombudsman and Corporate Secretary at Interac Corporation, and, prior to that, she practiced law at firms on Bay Street in Toronto and Wall Street in New York City.
A mentor to many, Kikelomo contributes her time as a Board member and advisor to various organizations. In 2020, she was recognized as one of WXN’s “Top 100 Most Powerful Women in Canada”. In 2019, she was named one of the 25 Most Influential Women in Payments, and in 2018 she was shortlisted for the National Post General Counsel of the Year Award. Kikelomo is a graduate of Harvard Law School and holds a Bachelor of Arts in Politics from New York University.
Jim is Chancellor Emeritus of Queen’s University, and former President and CEO of the Ontario Teachers' Pension Plan, one of the world's largest plans.
Previously, Mr. Leech was president and CEO of Unicorp Canada Corporation, one of Canada's first public merchant banks, and Union Energy Inc., then one of North America's largest integrated energy companies. Mr. Leech is: a Senior Advisor with McKinsey & Company; Chair Emeritus, UHN Foundation; on the Investment Committee of the MasterCard Foundation; the former Honorary Colonel of 32 Signal Regiment, Canadian Forces; Board member of Historica Canada; and a founding director of Right To Play International.
Mr. Leech has been a member of Queen's Board of Trustees, University Council, and Chair of Smith School of Business Advisory Board. In 2013, he co-authored The Third Rail, Confronting our Pension Failures, a best-selling book that received the 2013-2014 National Business Book Award.
In 2012, he was awarded the Queen's Diamond Jubilee medal in recognition of his work with the True Patriot Love Foundation; in 2014, was invested as a Member of the Order of Canada for his contributions to Canada as an innovator in pension management, for his writings on the subject of retirement funding, and for his community involvement; in 2018 was awarded the Canadian Decoration for his military service; and in 2019 was awarded the Order of Ontario for his pioneering work in pension management, philanthropic leadership and public service.
Mr. Leech holds a B.Sc. (Hons. Math and Physics) and an LL.D from the Royal Military College of Canada and an MBA from Queen's University. He is also a graduate of the Institute of Corporate Directors.
Bruce is one of Canada’s most influential leaders and thinkers in the environment sector. Bruce boasts an expertise on toxic substances, green energy, forest conservation, and environmental philanthropy that is second to none.
Lourie is the President of The Ivey Foundation, a private charitable foundation focusing on environmental policy change; a director of the Ontario Power Authority; a director of the Ontario Trillium Foundation; and a Chair of the Board of Environmental Defense Canada.
He is also the founder of a number of for-profit and not-for-profit organizations including Summerhill Group, a prominent market transformations consultancy specializing in energy conservation and renewable energy; the Sustainability Network; the Enerquality Corporation; and the Canadian Environmental Grantmakers’ Network. He was also the founding executive director of the Canadian Energy Efficiency Alliance and the founding president of the Clean Air Foundation. Many of the organizations he helped create are now regarded as models in their field.
Lesley Marks is Chief Investment Officer (CIO) of Equities for Mackenzie Investments. She oversees approximately 110 investment professionals who are involved in the day-to-day management of Mackenzie funds across the firm’s 12 equity boutiques. As CIO, Lesley is responsible for more than $65-billion of Mackenzie’s assets under management.
Lesley is a seasoned investment leader with more than 25 years of experience across asset and wealth management, including 22 years at the Bank of Montreal. During her tenure at BMO, Lesley was a CIO in both Asset Management and Wealth Management and prior to that had an extensive successful track record as a portfolio manager of Canadian equity portfolios.
Lesley is a Chartered Financial Analyst (CFA), holds a Bachelor of Commerce from Queen’s University and an MBA from the Richard Ivey School of Business.
Andrea leads Addenda’s stewardship efforts which includes active engagement with companies and issuers on Environmental, Social and Governance (ESG) matters to enhance the long-term value of investments for clients. This also includes actively promoting sustainable financial markets by collaborating with experts and engaging with standard-setters and policy-makers to create a more sustainable and net-zero aligned economy and market.
Previously, Andrea was the Vice President of The Ivey Foundation. She brings over 20 years of experience managing environment and sustainability issues in the public, private, investment, and non-government sectors in Canada and the U.S. Prior to Ivey, Andrea was the Vice-President of the Corporate Program at Ceres, where she led Ceres’ work with more than 80 companies on sustainability issues such as climate, energy, water, and supply chains.
She was the lead author of The 21st Century Corporation: The Ceres Roadmap for Sustainability and corporate benchmarking reports based on this framework. Andrea also serves on the board of the International Institute for Sustainable Development (IISD) Experimental Lakes Area, and the Advisory Boards for the Canada Climate Law Initiative, Peter A. Allard School of Law, University of British Columbia, and the Institute for Sustainable Finance, Smith School of Business, Queen’s University.
Lindsay Patrick is Managing Director and Head of Strategy, Marketing and Sustainability at RBC Capital Markets and a member of the firm’s Operating Committee.
Lindsay is responsible for the advancement of the RBC Capital Markets’ business, brand, and marketing strategy, supporting the firm’s overall growth and performance ambitions. She is a senior adviser on ESG matters to the Group Executive and the wider RBC enterprise, providing insight and guidance in respect of our Capital Markets client base and the transition to net zero. Lindsay also oversees the Sustainable Finance Group, and with her global team, spearheads the provision of solutions and advice for RBC’s institutional and corporate clients across all areas of sustainable finance that incorporates both environmental and social perspectives.
Lindsay has over two decades experience in investment banking, spanning trading floors across North America, Europe, Australia, and Asia. She began her career with RBC Capital Markets in Investment Banking in Toronto and spent 10 years across variety of positions in Global Equities with a global bank in London before returning to RBC Capital Markets in 2016.
Lindsay is passionate about talent development and is active in advancing important initiatives related to Diversity and Inclusion.  Within RBC, she is a mentor to numerous colleagues, supporting their growth and development across the bank.
Lindsay received her MBA with Honours in Finance from The Wharton School at the University of Pennsylvania, her BBA with Honours in International Business from Bishop’s University, is a CFA Charterholder and completed the CFA Certificate in ESG Investing. Lindsay sits on the Advisory Board for the Institute of Sustainable Finance and is recognized as leader in sustainability in Canada as a Clean50 Honoree. She is an active volunteer within her local community and serves on the Board Directors for the Oakville Community Foundation. Lindsay is married and the proud mother of four boys.
Based in Toronto and with a national mandate, David Pinsonneault leads TD Business Banking which includes the segments of Small Business Banking, Commercial Banking, National Accounts, Agriculture, TD Equipment Finance (leasing), Merchant Solutions (credit card payment systems and online payment solutions) and Financial Restructuring.
David joined TD Bank Group in February 2017. He previously led TD Business Banking Quebec and Atlantic Regions from 2009 to 2014 as Senior Vice President.
David joined TD Bank Group after a 16-year career at National Bank of Canada where he held various management positions in business development, risk management and projects. This led him to become head of Business Banking and the International sector. Before becoming a banker, David taught finance at HEC Montreal.
David holds a B.A.A. from the University of Sherbrooke, a graduate degree in commerce, administration and finance from the École Supérieure de Commerce de Poitiers in France and an M.Sc. in finance from HEC Montreal.
Outside of work, David enjoys supporting causes related to entrepreneurship, diversity, and sustainability initiatives. He is currently Chairman of the TD Sustainable Finance Executive Council, member of the Advisory Board of the Institute for Sustainable Finance (Queen's University), member of the TD Inclusion & Diversity Leadership Council, member of the Board of Governors of the School of Management of the Sherbrooke University and a founding member of Ontario Global 100. He was a member of the Board of Directors and chair of the Audit Committee of the Beauce Entrepreneurship School, founding member of Quebec Global 100, Governors of Finance Montreal and chaired the Quebec chapter of TD Friends of the Environment Foundation.
Jennifer Reynolds is the CEO of Women Corporate Directors Foundation (WCD). WCD is the world's largest network of women corporate board directors, with more than 2500 members serving on more than 8,500 public and private boards around the globe.
Jennifer’s 25 year career in the financial services industry has included senior roles in investment banking, venture capital, and global risk management. Prior to joining WCD, Jennifer served as the President & CEO of Toronto Finance International (TFI), a public-private partnership which promotes and develops Canada’s financial services sector, and serves as the international representative for the Toronto financial centre. Prior to joining TFI, Jennifer was the President & CEO of Women in Capital Markets (WCM), Canada’s largest industry association and advocacy group for women in the financial sector.
Jennifer is a former Director on the Board of Citibank Canada, current Director on the Board of BF&M Insurance Group Ltd, Director on the Board of the Canada Development Investment Corporation ("CDEV"), and a Director on the Board of Women’s College Hospital Foundation. Jennifer is the Co-Chair of the UN convened Financial Centres for Sustainability (FC4S) network and also serves on the Advisory Council for the Institute of Sustainable Finance. In 2015 and 2017, she was named a Women's Executive Network (WXN) Canada's Most Powerful Women: Top 100 Award Winner.
Jennifer is a graduate of the Harvard Business School Women's Leadership program, and she received her MBA from McGill University, as well as a Bachelor of Arts with a double major in Economics and Political Science from McGill University. Jennifer also holds the Institute of Corporate Directors Designation, ICD.D.
Pamela is the president and CEO of CPA Canada. Prior to assuming this role, she was the chief financial and corporate strategy officer at Payments Canada. She also served as chief financial officer and head of finance and employer services for the Workplace Safety and Insurance Board.
In 2016, Pamela was named a Fellow of the profession and in 2019, she was honored as Canada’s CFO of the Year.
Today, Pamela sits on the City of Toronto Investment Board, the board of Michael Garron Hospital and the University of Waterloo’s School of Accounting and Finance advisory council.She is an active and founding member of the advisory board for the Institute for Sustainable Finance. Pamela was also a founding member of the Canadian Chapter of the Accounting for Sustainability CFO Leadership Network.
Craig Stewart leads national work on disaster resilience and climate change at the Insurance Bureau of Canada (IBC) - the industry association representing the property and casualty insurance industry in Canada. IBC’s members employ over 122,000 Canadians and paid out $9.8 billion in property claims in 2016, primarily due to severe weather and wildfire. Previous to his work with IBC, Craig directed the Ottawa Bureau and Arctic program for WWF Canada, handled pandemic liaison, trade liaison and humanitarian donations for GlaxoSmithKline (Canada) Ltd., directed a $60 million federal/provincial/territorial program at Natural Resources Canada to elevate the Canadian geospatial industry and founded the Miistakis Institute at the University of Calgary. Craig holds a Master of Science from the University of Calgary, and a Bachelor of Arts in political science from the University of Toronto. He is the author of two atlases on the Rocky Mountains of Alberta, British Columbia and Montana.
Meigan Terry is the Senior Vice President and Chief Sustainability, Social Impact and Communications Officer at Scotiabank. In this role, she leads the strategic execution of the company’s Environmental, Social and Governance (ESG) and sustainability strategy, ScotiaRISE, the Bank’s social impact program as well as Scotiabank’s enterprise-wide stakeholder communications in support of the Bank’s strategy.
Meigan joined Scotiabank in 2018. Over the course of her career at the Bank, she has expanded her mandate and delivered a number of critical initiatives including: the creation of ScotiaRISE, our 10-year initiative to invest $500 million to foster economic resilience among disadvantaged groups; Spark, our Employee Giving and Volunteering platform and, Scotiabank’s Climate Strategy.
Throughout her career, she has delivered social impact, sustainability, global communications, brand management, corporate affairs, and employee engagement for iconic global brands. Prior to joining Scotiabank, she was Senior Vice President, Corporate Affairs and Communications with Virgin Atlantic in the U.K. where she managed all aspects of communications, brand management, public policy, government affairs and social media. Meigan also led Virgin Atlantic’s sustainability, environment and community investment programs, in addition to acting as executive sponsor for the Virgin Atlantic Foundation. Meigan has also held senior communications roles at BlackBerry, and WPP Consultancy Hill & Knowlton in London.
Meigan chairs Scotiabank’s Climate Steering Committee and serves on the Advisory Board for the Institute for Sustainable Finance (Queen’s University).
Dr Walker is the founder of the Emerging Risks Information Center, which conducts targeted research on environmental, technological, and societal risks that affect our world today. Since its inception, the Center has employed over twenty Ph.D., Master’s, and undergraduate students who serve as research assistants and co-editors/co-authors on various research projects
Dr. Walker was awarded an Outstanding Teaching Award from Washington State University and a Fellowship for Experienced Researchers from the Alexander von Humboldt Foundation, Germany. Dr. Walker has served as Laurentian Bank Professor in Integrated Risk Management (2010-2015), Chair of the Finance Department (2011-2014), Director/Co-director of the David O’Brien Centre for Sustainable Enterprise (2015-2017), and as Associate Dean, Research and Research Programs (2016-2017).
In addition, he has been an active member of Finance Montréal, the steering committee of the Montreal chapter of the Professional Risk Managers’ International Association (PRMIA), the academic advisory board of the MMI/Morningstar Sustainable Investing Initiative, the advisory board for Palgrave Macmillan’s Future Earth book series on sustainability, the advisory board of Concordia’s Institute of Aerospace Design & Innovation (CIADI), and the advisory board of Concordia’s Institute for Water, Energy and Sustainable Systems.
Barbara Zvan is the Inaugural President and Chief Executive Officer of the University Pension Plan Ontario (UPP) and former Chief Risk and Strategy Officer for the Ontario Teachers' Pension Plan. Recognized as a leading voice on sustainable investing and an ambassador for defined benefit pensions, Barbara is known for her efforts to bring institutional strength to complex challenges and forge new collaborative pathways for innovation and growth. She serves on the boards of various global institutions and associations focused on pension management, risk and responsible investing, including the Global Risk Institute, Responsible Investment Association and the advisory board of the Institute of Sustainable Finance at Smith School of Business. She was appointed to the Government of Canada’s Expert Panel on Sustainable Finance, is a member of the Advisory Committee for the new ‘Investing to Address Climate Change’ Charter and played a significant role in creating the G7 Investor Leadership Network.
Barbara is a Fellow of the Society of Actuaries and the Canadian Institute of Actuaries, a holder of the Institute of Corporate Directors designation (ICD.D) and has a Master of Mathematics degree from the University of Waterloo. She is an honouree of Canada's 2020 Clean50 and Canada's 2008 Top 40 Under 40.

# [Getting on board | Smith Magazine](https://smith.queensu.ca/magazine/issues/spring-2024/features/getting-on-board.php) 
 _https://smith.queensu.ca/magazine/issues/spring-2024/features/getting-on-board.php_

Patricia McLeod’s (EMBA’11) board awakening came nearly 15 years ago at a moment that was, on paper, pretty awkward. She had a demanding day job as an associate general counsel and compliance officer. She was finishing her Executive MBA at Smith. She had young children to wrangle, a new house under construction and a raft of volunteer commitments. Her daily to-do list would make Taylor Swift seem like a slacker. Why on earth would she add a part-time gig — an unpaid one, at that — to the mix?
* * *
Yet when McLeod saw an ad soliciting applications for a volunteer board director at the non-profit Calgary Economic Development, her mind lit up. The board was hoping to fill the role with someone younger; she was in her early 40s. They were looking for someone with energy experience; she worked at a power company. They wanted legal expertise; she had a decade and a half of practice. More than that, the opportunity promised the challenge that her insatiably curious brain craved. “It was that chance I’d been looking for to apply the concepts that I was learning and experiences that I was having to a context different from law,” she reflects. “So I thought, ‘OK, I’ll throw my hat in.’ ” She consulted her mentors, prepared a detailed application, practised (and nailed) the interviews and — much to her delight — was offered the role.
She quickly found board work more than made up for the sleep and TV sacrificed to fit it in her schedule. “For the first time, I was using my whole brain, which can be both detail-oriented and big-picture,” McLeod says. “It made me realize I wanted to be at the table where people make and test deals, where they strategize, where they push buttons.”
The feeling was addictive. In fact, over the next few years, McLeod tapered her legal work and replaced it with board service — some volunteer roles, but also, increasingly, paid positions. In 2017, a year after earning her first corporate board chair appointment, she decided to focus full-time on board work. To date, she’s served on more than two dozen; she just accepted her eighth chair position. “I just love it,” she enthuses.
Board service has some clear benefits. It can round out your resumé, bolster your professional network, up your likelihood of promotion, and — if you land a spot on a corporate board — pay handsomely. Because the board oversees the overall direction of the organization, it offers opportunities to engage in wide-lens problem-solving that can be hard to find in the weeds of a day job; all while often contributing to causes and efforts you really care about.
Yet, the process of securing a meaningful board gig can seem vague and confusing. So we spoke to accomplished Smith alumni with a rich range of board experiences to demystify the process.
## Tally your experiences
One quandary facing would-be directors is how to start. Not many boards — even small, volunteer ones — will appoint a director with no experience. That can place newbies in an awkward chicken-or-egg position.
But the experience many boards want can come from different places, says McLeod. While you’re unlikely to land a high-profile corporate directorship without having done the job elsewhere, non-profits, industry associations and community groups are often open to considering your passion and potential — as long as you show proof of your ability to work well with others. “Look for any situation where you’ve sat at a table with groups of people with different perspectives to try and get consensus for a decision or execute on a project,” McLeod advises. Think of that time you volunteered to plan an industry association conference or that cross-functional project team you helped lead at your work. These experiences demonstrate an ability to collaborate towards a common goal, McLeod says, and are a great way to show your skills, gain references and build confidence.
> “Many veteran directors recommend creating a “board resumé” that is specifically devoted to selling why you’d be a strong director”
It’s a good idea to not only take inventory of these experiences but also to learn how to communicate them. Many veteran directors recommend creating a “board resumé” specifically devoted to selling why you’d be a strong director. The better you get at communicating your suitability, the more successful you’ll be.
## Hone your skills
There are some things you don’t need to know to be an effective director. For instance, you don’t need to be an expert in the finer points of business law or governance processes (at least, not at first). Nor do you need to be well-versed in the industry or community the organization serves. “If you’re in a position of being considered for a director role, the assumption is that you’re going to lean in and come up that learning curve,” says
**Hazel Claxton, BCom’83**, a retired executive who now sits on five corporate and non-profit boards. It’s important, she says, to recognize where your skills and experiences match up with what the organization needs most — that “you can connect the dots and bring relevant constructive insights from your experience in other sectors.”
What _do_ you need? Ideally, your financial literacy is strong enough to understand the levers most relevant to the economics of an organization and assess the integrity of financial reporting. Curiosity and critical thinking are also crucial. You must be able to ask tough questions and respond with conviction when you don’t get satisfactory answers. And you need excellent time-management skills: You’ll be tasked with reviewing and interpreting high volumes of information about all manner of organizational imperatives. That can’t be done by scanning a few emails before a meeting.
“You can’t just be passive and expect to be spoon-fed,” explains Claxton. It is your duty, she says, to seek out information, to take real time to assess the issues at play and to consider how it all adds up.
## Put your hand up
You might dream of a situation in which a board chair taps you on the shoulder and implores you to please accept a seat. Or one in which your application simply dazzles the recruitment committee. Those things do happen. But it’s more likely that you’ll need to hustle to make it known you’re willing to serve. Especially if you haven’t done much of it.
“You kind of have to be your own headhunter,” says **JP Gladu, EMBA’12,** founder and principal of the strategic consultancy Mokwateh. Gladu currently sits on four boards, including that of the non-profit Institute of Corporate Directors, which educates and represents Canadian directors and boards. Having been through the board recruiting process many times, on both sides of the table, he’s seen how fortune favours the bold.
Be prepared to do a lot of old-fashioned smithqueens.com/magazine 31 networking. Let past and present colleagues, mentors and industry connections know you’re open to board opportunities. (A well-crafted LinkedIn post can do wonders.) Research the executive search firms who’ve worked with boards you’d like to join and reach out to recruiters to get on their radars (most keep “evergreen” lists of good candidates). And show up to relevant industry, organizational and charitable events. “It really is about relationships, relationships, relationships,” Gladu explains. “You never know who in what circle has a connection, and who can make an introduction. Showing interest and showing face is very important.”
## Find the right fit
New directors are often so eager for experience they’ll go all-in on the first opportunity. It’s worth taking a beat to think about how you want to serve, says **Bettina Pierre-Gilles, EMBA’14,** an accomplished entrepreneur and finance executive with extensive experience on both corporate and non-profit boards. “You need to treat it like you would a regular career opportunity. You don’t just take the first job that’s offered to you because you’re desperate,” she says. “You need to make sure that there is a fit.”
What makes a board role a fit depends on how your objectives mesh with what the organization needs, says Pierre-Gilles. Will the position allow you to apply your skills and knowledge? Will it teach you things you want to learn? Will it propel you to another board? Will it allow you to contribute to something you really care about? If you can’t answer “yes” to at least one of these questions, you’re probably better off holding out for something different. “You have to put in the effort to know what it is that you want, and what value you are willing to add,” Pierre-Gilles advises. “Once you know that, focus your energy on boards who are looking for it.”
## Understand the risks
A final factor to consider: Board service is not just a serious commitment. If you’re not careful, it can be a potential risk.
“When you’re interviewing for a board position, remember: The organization is evaluating you, but you also need to evaluate it,” explains **Bertrand Malsch,** the PWC/Tom O’Neill Professor of Accounting at Smith, who researches governance in professional service firms. “Because when you take the position, you become legally responsible for a lot of the things that can go wrong in the organization.”
In Canada, corporate board directors hold both duty of care and fiduciary duty of loyalty. That means you’re legally on the hook to put the interests of the company first and to keep on top of what’s going on. (You really can’t skip the reading — and there is a lot of reading.) It’s less intense for non-profit directors, but even then, a bit of prudence will go a long way to minimize risk.
Malsch recommends you review the organization’s financial statements to look for anything confusing or potentially fishy. In the interview process, ask about current disputes or lawsuits that might pose problems down the line. Explain that you understand that this may be confidential information, but that you cannot responsibly proceed without doing your due diligence. (If you get pushback, consider it a red flag.) Also, take note of the dynamic between other board members. Is there excessive conflict or groupthink? Either can be problems. “People are so eager to become board members because it carries so much symbolic capital and recognition,” Malsch says. “But that should never cause you to underestimate the risks. They are material. And your reputation depends on it.”
Indeed, with great power comes great responsibility, as any Spider-Man fan will tell you. But when you get it right — when you contribute to a board that challenges an organization to be the best version of itself and challenges you to be the best version of yourself — it’s worth every bit of effort expended to get there. “When you get that,” reports Gladu, “it’s wonderful.”
## We live to serve
Our star panel of Smith alumni hold positions and serve on a variety of boards
* * *
### Hazel Claxton, BCom’83
Retired human resources executive, formerly at PwC and Morneau Shepell
**First Board:** Shaw Festival (director)
**Current Boards:** Allied Properties REIT (trustee), Bank of Montreal (director), Telus (director), Unity Health Toronto (director), University Pension Plan Ontario (trustee)
“Serving on a board is a privilege. If you’re going to occupy one of the rare seats at the table, know that it comes with a lot of responsibility. It’s not about cachet. It’s about learning. It’s about carrying out your responsibilities in the best way possible. It’s about stepping up.”
* * *
### Patricia McLeod, EMBA’11
General counsel and compliance officer turned full-time board chair and director
**First Board:** Calgary Economic Development (director, then vice-chair)
**Current Boards:** City of Calgary Green Line Board (director), FutEra Power Corp. (chair), MINDD Bra Company (director), Pieridae Energy Ltd. (chair), Quantum Algorithms Institute (incoming chair)
“Board work can involve some fairly routine duties, like approving financials, or become really intense, like having to handle a crisis or a black swan event. But sometimes you have the extraordinary moment of getting to say, ‘I think we just made a strategic decision that will support the long-term sustainability of this organization.’ That’s the sweet spot on the tennis racquet of governance.”
* * *
### JP Gladu, EMBA’12
Founder and principal, Mokwateh
**First Board:** Lake Nipigon Forest Management Inc. (director)
**Current Boards:** Broden Mining (director), Canada’s Forest Trust (chair), Institute of Corporate Directors (director), Suncor (director)
“When you spend time with your fellow directors, who have so much to offer, and share your learnings with them, it creates such great diversity of brain power and strategy power. You’re constantly learning, and I find you bring that experience into your own life — professionally and personally.”
* * *
### Bettina Pierre- Gilles, EMBA’14
Founder, president and CEO, Luxeum Renewables Group; president and CEO, Pierre- Gilles & Associates Professional Corporation
**First Board:** Poplar Point Energy Ltd. (director and treasurer)
**Current Boards:** Bow Valley College (governor), Piikani Investment Corporation (chair), Queen’s University (trustee), Renewable Energy Transition Inc. (audit committee chair)
“Being on a board is not simply about deploying your expertise and knowledge and experience. My gosh, you learn so much from your fellow board members. You learn so much about the inner workings of organizations. It forces you to think in a holistic way.”

# [Mystery queen | Smith Magazine](https://smith.queensu.ca/magazine/issues/spring-2024/my_other_cv/mystery-queen.php) 
 _https://smith.queensu.ca/magazine/issues/spring-2024/my_other_cv/mystery-queen.php_

Melodie Campbell wrote her first novel on a dare. Since then the Burlington, Ont.-based author has written 17 of them. Many are in the mystery genre, including _The Goddaughter_ comedic crime-caper series and her latest novel, _The Merry Widow Murders._ She’s also scored bestsellers in fantasy with the Rowena series.
**What’s your hometown?** 
Toronto mainly, West Vancouver for high school.
**When you were growing up, what did you want to be?** 
A mystery writer! First I wanted to be Carolyn Keene \[author of Nancy Drew books\]. Then Agatha Christie. Instead, I became a director of marketing, which some people might say is criminal.
**What was your first job?** 
Bell Canada, in the toll plant, where the long-distance switching machines were located. Talk about being thrown headfirst into the world of men! Yes, I was probably a token experiment, but it went pretty well for both of us. Bless them for seeing my potential.
**Why did you start writing novels?** 
I was at the bar of the Toronto Press Club, and a well-known male _Toronto Star_ columnist said to me, “You’re a humour columnist, you’ve won a slew of short story awards. Why don’t you write a novel?” I answered, “Because they might make me write a second one!” So he dared me. I have avoided scotch ever since.
**What’s the hardest part about writing a book?** 
The length of time it takes. I can write a crime short story in a week. I love writing short stories — I’ve had over 60 published. A novel takes me 1,000 hours to write with edits, so about a year. That’s an incredible amount of time, memory, dedication and coffee.
**Any advice for aspiring novelists?** 
Write the book you wish someone else would write, so you can read it.
**What’s your biggest-ever career mistake?** 
In 1993, I had a wacky play performed in Toronto. A television producer was in the audience. He came up to me after and said, “You are completely nuts. I’d like you to come to Los Angeles and write pilots for me.” We kicked around a deal that I ended up declining because it would have meant moving my husband and two preschoolers to the States. Besides, who had ever heard of HBO in 1993? This has to be the worst mistake ever made by someone not legally insane.
**What’s your career highlight so far?** 
A crowd of students cornered me to say I was their “rock star” for writing _The Goddaughter_ series. That beats out all 10 crime fiction awards I’ve received.
**Name someone you admire.** 
Agatha Christie. She was the best, and she wrote in a time when women had an even harder time getting published. A close second is Dorothy Parker, for her wit and sheer bloody guts.
**Your favourite all-time book?** 
The entire Inspector Montalbano series by Andrea Camilleri.
**What are you reading now?** 
I’m making my way through the Bryant and May series by Christopher Fowler. Crime with great Brit humour.
**Your favourite all-time movies?** 
All zany comedies: _The Wrong Box; the Russians Are Coming; The Pink Panther; Best in Show._ I love satire.
**What’s your motto?** 
Recent studies show approximately 40 per cent of writers are manic-depressive; the rest of us just drink.
**What trait do you most admire in others?** 
Compassion, hands down.
**What do you do when you’re not working?** 
All writers dream of the day they can give up their day job and make writing their work. Trouble is, when you do that, you lose your hobby! But if you’re talking about interests, I’ve always been mad about cars. My first car was a Triumph Spitfire; my second, a Lotus Europa. I’ve had two Corvettes. And I have my motorcycle licence.
**What’s the best advice you ever got?** 
If you want to be admired, get a dog.
**What is your most treasured possession?** 
Probably my Arthur Ellis Award statue for excellence in crime writing from the Crime Writers of Canada, followed by the Derringer Award medal from the Short Mystery Fiction Society in the U.S.
**What’s one thing most people don’t know about you?** 
I got my start writing comedy. I wrote standup for comedians and did some standup myself but didn’t like a liquored-up crowd. From there, I was offered a newspaper humour column, and that led me to humorous fiction.
**What’s your best Queen’s memory?** 
Science Formal ’76 with my late husband David Campbell, BSc(Eng)’76. We were together for 40 years. Many kind classmates sent condolences after Dave died, but **Michael O’Connell, BCom’78,** helped me find my way back from grief. We were married two years ago. I will always be grateful that Queen’s brought us together.
**Who was a favourite professor?** 
Carl Lawrence was the most influential because he prepared me for how challenging it would be for a woman in business in the late 1970s. You might say he demonstrated how tough it would be.
**Your favourite travel destination?** 
England.
**What’s on your playlist right now?** 
Rachmaninoff, Elgar, Ella Fitzgerald, PDQ Bach, Great Big Sea.
**What’s your idea of perfect happiness?** 
A dinner party for eight, with clever, witty friends. I love great conversation.

# [Smith welcomes new faculty](https://smith.queensu.ca/news_blog/2023/Smith-welcomes-new-faculty.php) 
 _https://smith.queensu.ca/news_blog/2023/Smith-welcomes-new-faculty.php_

Faculty and staff recently had the opportunity to get to know some of the new faculty during the business school's annual retreat.
**Kingston, Ont.** – Ten new faculty have joined the business school’s outstanding roster of teachers and researchers in recent months.
The new assistant and associate professors bring a diverse set of experiences and backgrounds to the school, plus expertise in strategy, marketing, accounting, finance, economics, digital technology and management analytics. Here's more on each one:
**Bhargav Gopal** 
Assistant Professor of Business Economics
Bhargav Gopal grew up in Los Angeles and came to Smith over the summer after earning his PhD in economics at Columbia University. Gopal is an applied microeconomist whose research is at the intersection of finance, labour, law and economics. He has a specific interest in how government intervention in labour markets can improve societal outcomes.
In a recent paper, Gopal examined why there are still so few women on corporate boards. More specifically, he looked at the effects of a 2018 California law requiring at least one woman on boards. Within one year of that law taking effect, the number of all-male boards was cut by 30 percentage points, with no reduction to a firm’s value, operating performance or shareholder returns. So why weren’t there already more women on boards? Gopal says he found that many women who were clearly qualified to serve “were more likely to be ‘out of network’, in the sense of not having prior employment experience or connections with existing board members.”
Gopal will teach in the Commerce program. In his spare time, he enjoys playing basketball and hiking.
**Sarah Burrows** 
Assistant Professor of Strategy
Sarah Burrows grew up in Montreal and attended university there, earning an undergraduate degree in psychology at Concordia, followed by a Master of Science in Management at the university’s John Molson School of Business. To earn her PhD in management, she headed to the University of Central Florida. Now, she says, she’s delighted to be back in Canada, having joined Smith’s faculty over the summer.
Burrows’s research connects two areas: entrepreneurship and family business. She says her background in psychology comes in handy examining how family dynamics influence the management of companies and how families nurture entrepreneurship across generations. “Family-owned businesses represent most businesses worldwide. It intrigues me that the majority of business owners choose to mix family and business. And my research investigates how families successfully manage that.”
Burrows will teach in the Commerce program. Her favourite hobby is cooking. “I was raised in a large Italian family, and I was always taught that cooking is a great way to show others you care for them.”
**Beste Kucukyazici** 
Associate Professor of Management Analytics
Beste Kucukyazici isn’t a new face at Goodes Hall. For the past year, she’s been an adjunct assistant professor and the lead of the school’s health-care analytics initiative. On Sept. 1, she became an associate professor of management analytics. Before Smith, she was an assistant professor in the departments of accounting and information systems and supply chain management at Michigan State University’s Eli Broad College. She grew up in Turkey and earned her PhD in operations management at McGill University’s Desautels Faculty of Management.
Kucukyazici’s current research centres on developing and applying prescriptive analytics in health care. In one recent paper, Kucukyazici and a colleague looked at how people who’ve suffered a stroke are taken to hospital and triaged. In those situations, every second counts, so they developed an analytical model to help improve the system so that patients get the care they need. Analytics, she says “can save lives and significantly improve patient quality of life.”
Kucukyazici teaches in the Commerce and MBA programs. Her hobbies include travel, reading and salsa dancing.
**Edem Klobodu** 
Assistant Professor of Marketing
Edem Klobodu arrived at Smith over the summer from the University of North Carolina’s Kenan-Flagler Business School, where he was a postdoctoral research associate. He grew up in Ghana and completed his undergraduate and master’s degrees there. He earned his PhD in marketing at the University of Texas at San Antonio.
Klobodu studies financial inclusion and the role of marketing among underprivileged consumers in financial services. “My research operates at the intersection of marketing and policy, allowing me to derive marketing implications from economic impacts.” Much of his work is based around mobile money and how it lets underprivileged consumers take part in the formal financial sector. “I have the chance to research a consumer group — specifically, consumers at the bottom of the pyramid — that hasn’t received much attention in the marketing literature. By focusing solely on studying them, I am able to find unique solutions to enhance their well-being,” he says.
Klobodu will teach marketing to Commerce students. Outside of work, he enjoys waterfront walks and playing board games with his family.
**Yulia Nevskaya** 
Assistant Professor of Marketing
Before she arrived at Smith over the summer, Yulia Nevskaya was an assistant professor of marketing at Olin Business School at Washington University in St. Louis. She grew up in Kostroma, Russia and earned her PhD at the University of Rochester, studying quantitative marketing. She studies how consumers respond to purchase stimulants, such as advertising, loyalty programs, social media influencers and online reviews.
Nevskaya has paid particular attention to online video games. “This is the number one entertainment industry in the world, surpassing the movie industry and major sports leagues combined,” she says. But many worry gamers are playing too much. So Nevskaya and a colleague looked at how to make games less addictive by, for example, alerting gamers to time spent playing, or limiting their playing time. They found these strategies ineffective. “However, specific revisions to the rewards schedule help in taming excessive gaming, without any losses to the game developer’s revenues,” she says.
Nevskaya will teach in the Commerce program and teach a doctoral seminar. In her spare time, she enjoys nature walks and travelling.
**Abayomi Baiyere** 
Associate Professor of Digital Technology
The world is going digital and Abayomi Baiyere is right at the centre of its research. His studies cover digital transformation, digital disruption and the societal impact of digitalization. “The why's, how's, what's and implications of digital innovation and digital transformation are exciting as each layer uncovered reveals several other layers waiting to be unearthed,” he says. One of Baiyere’s ongoing research projects investigates how organizations can assess the digital capabilities they need to match their digital transformation goals — something many firms struggle with.
Baiyere grew up in Nigeria. Before academia, he worked for companies such as SAP and ABN AMRO Bank and as an entrepreneur. He earned his PhD in information systems science at the University of Turku in Finland. Prior to joining the faculty at Smith, Baiyere was an associate professor at Copenhagen Business School in Denmark. He is an associate editor of _Information Systems Journal_ (ISJ) and sits on the editorial board of _Information and Organization_.
Baiyere teaches on the PhD and Master of Digital Product Management programs. As for hobbies, he says, “I like speed chess, steady walks and slow swimming.”
**Cory Hinds** 
Assistant Professor of Accounting
Cory Hinds grew up in Sacramento, California. He joined the faculty at Smith over the summer after earning his PhD in accounting at the University of Iowa. His research focuses on judgment and decision-making in financial markets. That includes looking at what influences retail and professional investment choices.
Hinds says he enjoys this area of study because “what I learn can have meaningful and practical implications for the welfare of individual investors and the efforts of regulators who are tasked with protecting those investors.” In his dissertation, for example, Hinds found that when the stock market does well, individual investors get overconfident. “However, I find that providing investors with a market benchmark, such as the return of the S&P 500 index, helps to reduce this market-induced overconfidence and improves investors’ judgments.”
Hinds will teach in the Commerce program. He enjoys watching sports, travelling, doing crossword puzzles and spending time with his wife and three children.
**Alison Taylor** 
Assistant Professor of Finance
Alison Taylor’s area of study is a timely one: climate risk and financial stability. “Currently, there are a lot of policy discussions by central banks about whether climate change could pose a risk to financial stability and if central banks should take action,” she says. Her research aims to contribute to that discussion and understand how investors and firms adapt to climate-change risks.
In one project, Taylor looked at whether U.S. banks hit hard by the 2007-08 financial crisis were more responsive or less responsive to hurricane risks in the household mortgage market. If financially distressed banks take on a larger hurricane risk, “this could increase the risk of financial instability if a large hurricane hits since they don’t have as much of a financial buffer to absorb a negative shock,” she says. Taylor, who grew up in Kingston and earned her PhD in economics at the University of Toronto, started at Smith over the summer.
She will teach finance to Commerce students. In her spare time, she enjoys running and rock climbing.
**Juan Francisco Chavez R.** 
Assistant Professor of Strategy and Organizations
Juan Francisco Chavez R. was born and raised in Peru. He’s also lived in the United States, the Netherlands and Canada. Chavez is passionate about sustainability and social entrepreneurship. Before he arrived at Smith this summer, he was an instructor in sustainability courses at the University of Victoria’s Gustavson School of Business in British Columbia. He earned his PhD there in international management and organization.
Chavez’s research covers sustainability, organizational theory and strategic management, investigating how to create value for both organizations and stakeholders in a diverse and pluralistic society. “If we think that the purpose of business is to create value, and if we are committed to creating a positive impact in society, it is important to first understand that value and impact are notions that can be defined differently by different people,” he says.
Chavez will teach on the Business for Good class in the Commerce program. Outside work, he enjoys hiking, camping, playing squash and watching movies.
**Alina Yue Wang** 
Assistant Professor of Business Economics
Alina Yue Wang’s research lies at the intersection of political economy and economic history. “I find the development of human capital, the origins of social conflicts and political selection in public administration particularly intriguing,” she says. Wang was born in Tokyo and grew up in Japan, Singapore and China. She earned her PhD in economics at the University of Hong Kong’s business school. Wang is a postdoctoral research fellow at the Kellogg School of Management at Northwestern University and will start at Smith in 2024.
One of Wang’s research projects, “Foreign Education, Ideology, and the Fall of Imperial China”, draws upon historical events to understand the nuanced role of human capital in political transformation. Wang and a colleague looked at how the Chinese Qing government’s intent to build a modern nation-state — by sending the country’s best talent to study in Japan starting in 1899 — led to its unexpected demise and ended 2,000 years of imperial rule in China.
Wang is a music lover and is especially fond of classical and country music and has amassed a large vinyl record collection. She is also a certified mixologist.

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=201911) 
 _https://smith.queensu.ca/news_blog/archive.php?a=201911_

[## New prize honours late Smith professor Jeff McGill
](https://smith.queensu.ca/news_blog/2019/2019_Jeff_McGill_Award.php)
November 25, 2019
Kingston, Ont. – For Smith professor Jeff McGill, recognition from the Revenue Management and Pricing (RMP) Section of the Institute for Operations Research and the Management Sciences (INFORMS) was a special highlight. In 2008, McGill won the Historical Research Prize. In 2013, he won the Practice Prize (with Smith colleagues Yuri Levin and Mikhail Nediak).
[## Dr. Brenda Brouwer appointed Interim Dean
](https://smith.queensu.ca/news_blog/2019/2019_Brenda_Brouwer_Interim_Dean.php)
November 13, 2019
Kingston, Ont. – On November 13, 2019, Brenda Brouwer was appointed Interim Dean of Smith School of Business, effective November 18, 2019. Dr. Brouwer takes over from Teri Shearer who served temporarily as Interim Dean succeeding David Saunders.
[## Smith alumni named to Top 40 Under 40
](https://smith.queensu.ca/news_blog/2019/2019_Top_40_Under_40.php)
November 12, 2019
Toronto, Ont. – Four Smith alumni were recognized last week at an event celebrating young Canadian business leaders. The four are among Canada’s Top 40 Under 40 for 2019.
[## Smith Launches First-Ever Program on edX Global Learning Platform
](https://smith.queensu.ca/news_blog/2019/2019_edX_partnership.php)
November 7, 2019
Kingston, Ont. – Canada’s Smith School of Business at Queen’s University will launch its first program on edX, the trusted learning platform, in January 2020. The Professional Certificate in Enterprise Sales is designed to develop critical skills in professional sales. Smith’s will be the first professional sales course on the edX platform.

# [New inductees for Smith Faculty Hall of Fame announced](https://smith.queensu.ca/news_blog/2016/2016-09-22_Faculty_Hall_of_Fame.php) 
 _https://smith.queensu.ca/news_blog/2016/2016-09-22_Faculty_Hall_of_Fame.php_

Kingston, ON – September 22, 2016— Outstanding research, exceptional mentoring and excellent teaching are just a few of the accomplishments of the 2016 Faculty Hall of Fame inductees. 
Established in 2009, the Faculty Hall of Fame recognizes Smith School of Business faculty members who made significant contributions to the school during their tenure.
Recipients are chosen by a selection committee comprised of the Dean, senior university leaders and alumni, as well as current faculty and students. This year’s inductees are:
R.G.R (Gordon) Cassidy: 1972-1997 
R.H (Bob) Crandall: 1961-1990 
R.L (Rick) Jackson: 1974-2014 
C.A (Carl) Lawrence: 1963-1991 
J.E (Ev) Smyth: 1946-1961
All inductees will honoured at a ceremony in Goodes Hall on October 11. Pen and ink portraits of each member will be displayed in Goodes Hall.
To learn more about the contributions of these inspirational professors, visit the Faculty Hall of Fame website.

# [Smith Magazine | Spring 2024 | Smith Magazine](https://smith.queensu.ca/magazine/index.php) 
 _https://smith.queensu.ca/magazine/index.php_

 feature
Sam Effah, MMIE’21, was an explosive sprinter who wowed crowds and broke records. Now he’s helping to grow the next generation of Canadian athletes
 feature
Joining a board can seriously boost your career. But how do you land a seat? And what should you know first? We asked Smith experts for advice
 Connect
A career in cosmetics took Tim Coolican, BCom’01, around the world. Now he’s taking an upstart beauty brand global too
 Connect
A curious mind has taken Julie Ioffe, MBA’20, from neuroscience to high finance and Europe’s economic capital. Here, she explains how she got there
 Connect
Six Smith PhD alumni teaching at universities across Canada and around the world tell us about their research and what key questions they are trying to answer
 Connect
A BCom’92 grad gives us a tour of the region of sport, wine and natural beauty
 My Other CV
In this issue, mystery author Melodie Campbell, BCom’78, answers our alternative resumé questions, from her best advice to aspiring authors to her biggest career mistake
## Insight
## Smith HQ
## Dean's Message

# [Top 20 Class Endowments](https://smith.queensu.ca/invest/class-giving/university-wide-top-20-class-endowments.php) 
 _https://smith.queensu.ca/invest/class-giving/university-wide-top-20-class-endowments.php_

Each year, thousands of Queen's graduates return to campus to reunite and celebrate with classmates. Whether it is their 5th or their 50th reunion, many classes take this opportunity to pay tribute to Queen's by giving back with a reunion class gift.
Annual class gifts support much-needed student bursaries and scholarships, library acquisitions, leading-edge technology, and other academic programs and projects that enable Queen's to deliver a first-rate academic experience and an exceptional learning environment to a diverse group of future leaders.
The key to a successful class giving campaign is the support of a Class Giving Committee. The more people you have engaged in the fundraising process, the easier it will be to get the rest of your class involved as donors.
**Ranking**
**Class fund name**
**Class**
**Balance 
(as of April 30th, 2024)**
1
The Science 1959 Admission Award
[Class of Science 1959](https://www.givetoqueens.ca/project/view/265)
$7,516,335
2
The Science 1948 1/2 Mature Student Entrance Bursary
[Class of Science 1948](https://www.givetoqueens.ca/project/view/395)
$2,102,561
3
The Commerce '48 Admission Award
[Class of Commerce 1948](https://givetoqueens.ca/project/view/bcom48)
$1,525,913
4
The Science 1957 Key Bursary
[Class of Science 1957](https://www.givetoqueens.ca/project/view/344)
$1,443,307
5
The Science 1968 Admission Bursary in Applied Science
[Class of Science 1968](https://www.givetoqueens.ca/project/view/355)
$1,420,460
6
The BCom 1980 Award
[Class of Commerce 1980](https://www.givetoqueens.ca/bcom80)
$1,356,756
7
The Science 1956 Entrance Bursary in Applied Science
[Class of Science 1956](https://www.givetoqueens.ca/project/view/337)
$1,184,904
8
Science '51 Entrance Bursary
[Class of Science 1951](#https://givetoqueens.ca/project/view/416)
$1,172,390
9
Commerce 1981 Entrance Scholarship
[Class of Commerce 1981](https://givetoqueens.ca/project/view/bcom81)
$1,114,760
10
The Science 1965 Entrance Award
[Class of Science 1965](https://www.givetoqueens.ca/project/view/351)
$1,103,651
11
The Commerce 1988 Honorary Award
[Class of Commerce 1988](https://www.givetoqueens.ca/bcom88)
$961,377
12
The BCom 1995 Award
[Class of Commerce 1995](https://www.givetoqueens.ca/bcom95)
$892,047
13
The BCom 1991 Award
[Class of Commerce 1991](https://www.givetoqueens.ca/bcom91)
$822,772
14
Science '44 40th Year Fund
[Class of Science 1944](https://www.givetoqueens.ca/project/view/339)
$815,197
15
Science 1972 50th Reunion Award
[Class of Science 1972](#https://givetoqueens.ca/project/view/358)
$812,072
16
The Science '50 Entrance Bursary
[Class of Science 1950](https://www.givetoqueens.ca/project/view/415)
$751,893
17
The Commerce 1993 Admission Award
[Class of Commerce 1993](https://www.givetoqueens.ca/project/view/297)
$740,010
18
The Commerce 1989 Award
[Class of Commerce 1989](https://givetoqueens.ca/project/view/bcom89)
$693,797
19
The Science 1982 Fund
[Class of Science 1982](https://www.givetoqueens.ca/project/view/367)
$633,285
20
Meds '62 Bursary
[Medicine Class of 1962](#https://givetoqueens.ca/project/view/160/1058)
$524,408

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=202205) 
 _https://smith.queensu.ca/news_blog/archive.php?a=202205_

[## 2022 Dare to Dream winners announced
](https://smith.queensu.ca/news_blog/2022/2022_Dare_to_Dream_winners_announced.php)
May 31, 2022
Kingston, Ont. – Four early-stage business ventures led by Smith School of Business students have been given a boost in funding from Smith’s Dare to Dream program.
[## New issue of Smith Magazine is now out
](https://smith.queensu.ca/news_blog/2022/2022_Smith_Magazine_Spring_2022_Issue_Out_Now.php)
May 11, 2022
Kingston, Ont. – The latest issue of Smith Magazine is now available—with an all-new print magazine look. This issue includes feature stories, alumni profiles, school news and insights from faculty and alumni experts.

# [Year in Review 2023](https://smith.queensu.ca/yearinreview/index.php) 
 _https://smith.queensu.ca/yearinreview/index.php_

### Exploring the role of 
business now
What place does the corporate world have in society today? With climate change, political instability, income inequality and the need for racial justice and Indigenous reconciliation, the role of businesses is shifting. This year we explored corporate impact and the important position companies have in society today.
[Read more about Exploring the role of business now](https://smith.queensu.ca/yearinreview/features/business-now.php)

# [Recognizing Your Generosity](https://smith.queensu.ca/invest/recognition/index.php) 
 _https://smith.queensu.ca/invest/recognition/index.php_

Your generosity has a vital and lasting impact on our students, faculty, and alumni. It enables us to attract the best and brightest students and top-tier faculty, providing them with exceptional experiences. It supports innovative research and its timely dissemination, benefitting the communities in which we all live. It helps us build strong and enduring alumni networks that keep our graduates connected to the latest business news and leaders around the world. Your investment had also helped us build the new Goodes Hall expansion, a leading-edge and technology-enabled research, teaching, and learning facility.
We could not do any of this without your support. That’s why it’s important to us to recognize and thank you for your generosity and trust, and to assure you that we do not take this responsibility lightly. We are grateful for every gift.
To show our gratitude for your contributions, we have created a number of ways to recognize your support:
* All donors to Smith School of Business are recognized annually on the Cumulative Giving list in the Smith [**Year in Review**](https://smith.queensu.ca/yearinreview/index.php). The online edition recognizes all gifts made during the fiscal year while the print edition reflects gifts of $1000 and more made during the fiscal year
*  Smith School of Business [**Class Giving Wall**](https://smith.queensu.ca/invest/class-giving/class-recognition.php) recognizes the remarkable commitments, generosity and participation of our top classes
* The **[Goodes Hall Benefactor Wall](https://smith.queensu.ca/invest/recognition/goodes-hall-wall.php)** recognizes donors who have contributed $10,000 or more to the building of Goodes Hall
* Smith School of Business [**Cumulative Giving Benefactor Wall**](https://smith.queensu.ca/invest/recognition/cumulative-giving-wall.php) recognizes with gratitude donors who have made a cumulative lifetime philanthropic commitment of $100,000 or more
* All donors who have given more than $100,000 are showcased on the [**Queen's University Benefactor Wall**](http://www.queensu.ca/alumni/supporting-queens/recognition/appreciation-societies) located in Joseph S. Stauffer Library
Queen's also recognizes the generous contributions of donors through its **[Donor Appreciation Societies](http://www.queensu.ca/alumni/supporting-queens/recognition/appreciation-societies)**

# [A focus on EDII](https://smith.queensu.ca/yearinreview/2021-2022/edii.php) 
 _https://smith.queensu.ca/yearinreview/2021-2022/edii.php_

Feature
Access, equity and inclusion are an important part of Smith’s future and the key to developing the next generation of business leaders and global citizens.
Diverse workplaces are more innovative and produce better results. [Research has time and time again](https://smith.queensu.ca/insight/content/How-Diversity-Builds-Tough-Competitors.php) proven that true. It’s not just corporate offices that benefit from a strong culture of equity, diversity, inclusion and indigenization (EDII). Universities and business schools do too—and they must become leaders in the field.
That’s one reason that last spring Smith School of Business unveiled a new [EDII Strategy and Action Plan](https://smith.queensu.ca/about/EDII/index.php), which was developed with the input of school alumni, students, staff and faculty. The strategy recognizes that access, equity and inclusion are vital to our school’s future and to developing graduates with the broad knowledge, skills and perspectives needed to contribute meaningfully to society as well as advancements in business.
Smith’s new dean, Wanda Costen, says that EDII is an important part of Smith’s ability to make a positive difference in Canada and the world. As she told [Smith Magazine last summer:](https://smith.queensu.ca/magazine/issues/fall-2021/features/wanda-costen.php) “I look at success in terms of the impact that we can have as an organization. The university’s focus on the [United Nations’ Sustainable Development Goals](https://www.queensu.ca/principal/actioning-sustainable-development-goals) really sends the message about how everything we’re doing on this campus is going to be geared towards impact—globally, but also in our own local communities . . . If we ask ourselves what the role of business education is in a global society, I’m hoping that we’re developing the kinds of leaders that recognize business for good.”
## Support for students
Creating impact and implementing Smith’s EDII strategy takes time, of course. Over this past year, we’ve taken positive steps toward that future. A good start has been to provide more opportunities for diverse candidates to get a Smith education. To help achieve that goal, several admission awards were created during our 2021-2022 fiscal year. These include:
[**Three new undergraduate awards**](https://smith.queensu.ca/yearinreview/2021-2022/highlights/edii-financial-aid.php) to improve access to business education for under-represented communities: The Wright Family Award, established by Susan and Jay Wright, BCom’81, looks to increase the representation of Indigenous business leaders in corporate Canada; the Commerce Oportunidad Award is aimed at Latin American students; and the Darren N. Costen Award (established by Dean Costen and named in honour of her son) aims to address the under-representation of Black students in the Commerce program and to alleviate the economic strain faced by students who are the first people in their families to attend university.
[**Two new awards for Black and Indigenous students:**](https://smith.queensu.ca/yearinreview/2021-2022/highlights/bipoc-scholarships.php) the Smith School of Business Scholarship for Black Students and Smith School of Business Scholarship for Indigenous Students. These are awarded annually across 13 Smith programs.
Supporting students goes beyond admission awards, however. For example, two Commerce student clubs—the Smith Black Business Association and Q+—have launched mentorship programs with help from alumni. A new EDII club was also formed. The EDII Club for Smith professional master’s students hopes to increase awareness about EDII challenges and present educational opportunities for professional graduate students.
Another initiative to help students comes from the school’s Centre for International Management (CIM). CIM worked with colleagues across Queen’s, student interns, student clubs and other universities to launch “Diversity Abroad.” The program provides resources to Smith students going on international exchange. Areas of focus include 2SLGBTQ+, faith communities, Indigenous students, mental health, racialized students and students with disabilities. The goal is to ensure outgoing exchange students are well-prepared for and feel supported while on exchange.
## Leaders in diversity
It’s nearly impossible for an organization to bring about meaningful change without having people in positions to make it happen. At Smith, several new people and jobs are helping to foster EDII within the school and beyond.
One of those is the dean: Wanda Costen brings her own lived experiences to Smith and was among the first generation of women to attend West Point. Costen’s research expertise covers women and leadership, strategic human resources, racial and gender inequality in organizations, managing diversity, and ethnic minority student experiences. She has also consulted on EDII issues in the public and private sectors with corporations and government.
Smith has also created a new staff position: director of equity, diversity and inclusion. This new role has responsibility for the implementation and progress of the school’s EDII Strategy and Action Plan—working closely with the dean, school administrators, and academic and student leaders to advance EDII in the teaching, learning and work environments and will serve as an expert resource on EDII-related matters.
Finally, last summer, a new faculty member was brought aboard with specialized research expertise in diversity and inclusion: [Ed Ng is the Smith Professor of Equity & Inclusion in Business](https://www.queensu.ca/gazette/stories/what-we-need-build-more-inclusive-future) and his research focuses on managing diversity for organizational competitiveness, the future of work and managing across generations. Ng’s work offers [useful lessons for business leaders](https://smith.queensu.ca/insight/content/Reading-the-CEOs-Mind-on-Diversity.php) and in January a webinar on Smith Business Insight that he led—[“Diversity at Work: How Leaders Can Drive Change”](https://smith.queensu.ca/insight/content/Diversity-at-Work-How-Leaders-Can-Drive-Change.php)—drew an audience of more than 400 business people from across Canada.
## Career development
Developing future leaders starts in school, and continues as students begin their careers. Through Smith’s Career Advancement Centre (CAC), the school is providing a number of opportunities for diverse students in the workplace.
In April 2022, for example, the Equity, Diversity, Inclusion, and Indigenization Internship (EDI3) program was launched. It’s aimed at first, second and third-year Commerce students from equity-deserving groups who are seeking a summer work experience. Fifty-seven students signed up to secure a summer internship. They will be paired with dedicated mentors who can offer career advice and guidance through monthly meetings.
For the second year, the CAC also hosted a Diversity Clubs fair to connect Smith’s corporate partners with [student diversity groups.](https://smith.queensu.ca/recruiting/diversity.php) The goal of the fair is to give student clubs exposure and support for their initiatives and events with corporate partners. At the same time, the fair allows companies to get involved with the student groups and identify talent. To help corporations further, the CAC has created a [best practices guide](https://smith.queensu.ca/recruiting/diversity.php) for employers on attracting and engaging with students from diverse and under-represented groups.
In 2021, the CAC launched a career preparation program for international students to help them navigate the unique challenges of job acquisition in the Canadian market. The eight-session program focuses on the tactical requirements needed to achieve career success in a safe and inclusive environment and to build confidence while optimizing performance.
The CAC has also hosted events to promote women in leadership. Last year's series called [“She Leads”](https://smith.queensu.ca/magazine/issues/fall-2021/news/no-doubt.php) focused on the unique challenges women face in securing leadership positions. Session topics for students included: “How to find your voice”, “The confidence gap in women” and “Shedding light on the experience of LGBTQ+ women”. All the events were hosted with the help of Smith’s corporate partners.
## Moving forward
There’s more to come of course as Smith continues to make EDII a priority. It’s worth noting that several initiatives over the past year have received recognition from outside the school. The Canadian Association of Career Educators & Employers (CCAEE) recently presented Smith with its 2021-2022 [Excellence in Innovation Award – Diversity.](https://www.cacee.com/Past_Award_Recipients.html) The award recognizes exceptional diversity initiatives that engage diverse populations, offer best practices for outreach programs, develop a diverse candidate pool, or enhance the retention level of diverse populations.
Last fall, two Commerce faculty—Lindsay (Kawennenhá:wi) Brant and Kate Rowbotham—were recognized by the Aspen Institute Business & Society Program’s Ideas Worth Teaching Awards. Their course, “Relationships and Reconciliation in Business and Beyond”, was [one of eight winning finalists](https://smith.queensu.ca/yearinreview/2021-2022/highlights/commerce-award.php) as part of the program that draws attention to new ideas about the role of business in creating a sustainable, inclusive society. The course is taught in Smith’s Commerce program and an abridged version with instructor Ann Deer was delivered to MBA and professional graduate students as part of a Summer Enrichment program last summer.
“Post-secondary education is essential for improving society,” says Dean Costen. “I believe business education has a responsibility to develop talent with the capabilities and desire to address social problems while creating economic sustainability in their communities. Our role is to create learning experiences that challenge students’ world views, biases, and beliefs to develop open-minded, courageous leaders willing to take risks for the greater good.”

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?c=Press%20Release) 
 _https://smith.queensu.ca/news_blog/archive.php?c=Press%20Release_

[## Smith welcomes Apitipi Anicinapek Nation for custom leadership program
](https://smith.queensu.ca/news_blog/2023/Smith-welcomes-Apitipi-Anicinapek-Nation-for-custom-leadership-program.php)
July 18, 2023
Kingston, Ont. – Queen’s Executive Education at Smith School of Business welcomed members of the Apitipi Anicinapek Nation, an Anicinape community whose members have lived on their traditional territory for over 8,000 years, to Queen’s campus for a custom leadership program in late June.
[## Smith and Desjardins partner to enrich FinTech learning opportunities for master's students
](https://smith.queensu.ca/news_blog/2023/Smith-Desjardins-partner-to-enrich-Fintech-learning-opportunities.php)
May 4, 2023
Toronto, Ont. — Technology has undeniably changed how financial markets and institutions function. The need for professionals with knowledge in emerging topics in the financial sector is the basis for an exciting new partnership between Queen’s University and Desjardins Group that will provide Smith School of Business students with valuable interactive learning opportunities.
[## Smith joins global responsible leadership alliance
](https://smith.queensu.ca/news_blog/2023/Smith-Joins-Global-Responsible-Leadership-Alliance.php)
March 16, 2023
Kingston, ON – March 16, 2023 – Smith School of Business is pleased to announce that it has joined a global alliance of business schools dedicated to promoting responsible leadership, research and education.
[## Smith MBA ranked among Top 75 in the world
](https://smith.queensu.ca/news_blog/2023/2023_Smith_MBA_ranking.php)
February 13, 2023
Kingston, Ont. – The Financial Times has ranked the Full-Time MBA at Smith School of Business in the top 75 in its annual ranking of global MBA programs.

# [Smith Business News Archive - Queen's University](https://smith.queensu.ca/news_blog/archive.php?a=201501) 
 _https://smith.queensu.ca/news_blog/archive.php?a=201501_

The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.

# [Our Insight Topics | Smith Business Insight](https://smith.queensu.ca/insight/tag.php?tid=pricing) 
 _https://smith.queensu.ca/insight/tag.php?tid=pricing_

 Smith Business Insight - Our Insight Topics 
[Skip to main content](#main-content)
Smith  
* [About](#)
 
 [Smith Home](/index.php)[Profile](/about/index.php)[News](/news_blog/index.php)[The Dean](/about/dean.php)[Strategic Plan](/about/strategic-plan.php)[Equity, Diversity, Inclusion & Indigenization](/about/EDII/index.php)[Learning Environment](/about/learning_environment.php)[Partnerships](/about/partners/index.php) [Services](/about/services.php) [SmithStore _​_](http://smithqueens.com/smithstore) [Queen's University _​_](https://queensu.ca)
 
* [Learning](#)
 
 [Explore Our Programs](/academic_programs/index.php)[Undergraduate Programs](/academic_programs/undergraduate.php) [MBA Programs](/mba_programs/index.php) [Graduate Programs](/grad_studies/index.php) [Executive Education](/executiveeducation/index.php)[Certificates](/academic_programs/certificates.php)[International](/international/index.php)[SmithEdge](/smithedge/index.php)[Academic Integrity](/about/academic_integrity/index.php)
 
* [Insights & Research](#)
 
 [Smith Business Insight](/insight/index.php) [Research](/research/index.php) [Publications](/about/publications.php) [Centres](/centres/index.php)
 
* [Faculty](#)
 
 [Meet Our Faculty](/faculty_and_research/faculty.php) [Join Our Ranks](/faculty_and_research/Join_Our_Ranks.php)
 
* [Alumni & Giving](#)
 
 [Give to Smith](https://smith.queensu.ca/invest/) [Alumni](/alumni/index.php)
 
* [Recruit & Engage](#)
 
 [Recruiting](/recruiting/index.php) [Partnerships](/about/partners/index.php) [Work with Students](/engage/index.php) [Smith Business Consulting](/centres/business-consulting/index.php)
 
Fresh ideas from [Smith School of Business](/index.php)
* [Topics](#)
 
 ### Categories
 
 * [Leadership](/insight/sections.php?sid=Leadership)
 * [Teams](/insight/sections.php?sid=Teams)
 * [Diversity](/insight/sections.php?sid=Diversity)
 * [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
 * [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
 * [Social Impact](/insight/sections.php?sid=Social%20Impact)
 * [Marketing](/insight/sections.php?sid=Marketing)
 * [Strategy](/insight/sections.php?sid=Strategy)
 * [Finance](/insight/sections.php?sid=Finance)
 
 ### Collections
 
 * [Our Emotions at Work](/insight/collection/Our-Emotions-at-Work.php)
 * [Speaking of Economics](/insight/collection/Speaking-of-Economics.php)
 * [The Age of Corporate Purpose](/insight/collection/the-age-of-corporate-purpose.php)
 * [How To Make Hybrid Work](/insight/collection/how-to-make-hybrid-work.php)
 * [All Collections](/insight/collections.php)
 
 ### Subscribe to Our Newsletter
 
 Cutting-edge research and expert advice delivered straight to your inbox.
 
 [Subscribe](/insight/newsletter.php)
 
* [Webinars](/insight/webinars.php)
* [Podcast](/insight/podcast/index.php)
* [Videos](/insight/video.php)
* [About](/insight/about.php)
Search
# pricing
## [Why You Shouldn’t Put a Price on a Great Gift](/insight/content/Why-You-Shouldnt-Put-a-Price-on-a-Great-Gift.php)
Those expensive gifts you like to give may be sowing the seeds of suspicion
[Load More](#)
## Editor’s Picks
1. [The New Rules of Public Speaking](/insight/content/The-New-Rules-of-Public-Speaking.php)
2. [The Untapped Potential of Customer Loyalty Plans](/insight/content/The-Untapped-Potential-of-Customer-Loyalty-Plans.php)
3. [How to Build Trusted Brands](/insight/content/How-to-Build-Trusted-Brands.php)
4. [How Catfish Effects Drive Stock Market Reform](/insight/content/How-Catfish-Effects-Drive-Stock-Market-Reform.php)
[Topics](#nav-menu-topics)
* [Leadership](/insight/sections.php?sid=Leadership)
* [Teams](/insight/sections.php?sid=Teams)
* [Diversity](/insight/sections.php?sid=Diversity)
* [Analytics-AI](/insight/sections.php?sid=Analytics-AI)
* [Entrepreneurship](/insight/sections.php?sid=Entrepreneurship)
* [Social Impact](/insight/sections.php?sid=Social%20Impact)
* [Marketing](/insight/sections.php?sid=Marketing)
* [Strategy](/insight/sections.php?sid=Strategy)
* [Finance](/insight/sections.php?sid=Finance)
[Collections](/insight/collections.php)
[Webinars](/insight/webinars.php)
[Podcast](/insight/podcast/index.php)
[Videos](/insight/video.php)
[About](/insight/about.php)
## Kingston
Goodes Hall 
Queen's University 
Kingston, Ontario 
Canada K7L 3N6
[1.877.533.2330](tel:+18775332330)
## Toronto
Simcoe Place 
200 Front Street West 
30th Floor
[416.365.7141](tel:+14163657141)
## Smith Programs
* [Undergraduate Programs](/academic_programs/undergraduate.php)
* [MBA Programs](/mba_programs/index.php)
* [Graduate Programs](/grad_studies/index.php)
* [Executive Education](/executiveeducation/index.php)
## Directories
* [Contact Us](/about/contact.php)
* [Smith Centres](/centres/index.php)
* [Smith Services](/about/services.php)
## Connect with Smith
* [Facebook](https://www.facebook.com/smithbusiness)
* [Instagram](https://www.instagram.com/smithbusiness/)
* [Twitter X](https://twitter.com/smithbusiness)
* [Linkedin](https://www.linkedin.com/company/smith-school-of-business-at-queen's-university)
* [WeChat](https://mp.weixin.qq.com/s/SoosIZFmLD0D01aSGJzgLw)
The Smith School of Business Kingston campus is situated on traditional Anishinaabe and Haudenosaunee Territory. 
SmithToronto is situated on the traditional territory of the Huron-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River.
* [Give to Smith](/invest/ "Give to Smith")
* [Careers](/about/careers/ "Careers at Smith")
* [Program Portals](/academic_programs/student-portals.php "Program Portals")
* [Privacy](http://www.queensu.ca/accessandprivacy/privacy/notice-collection "Privacy")
© Smith School of Business

# [Smith alum selected for 2019 class of Schwarzman Scholars](https://smith.queensu.ca/news_blog/2017/2017_Heather_Evans_Scholarship.php) 
 _https://smith.queensu.ca/news_blog/2017/2017_Heather_Evans_Scholarship.php_

Heather Evans, BCom'16, at the G7 Youth Summit in Rome.
**Kingston, ON —** Heather Evans, BCom’16, was standing in her parents' kitchen in Kingston last month when she found out she’d been named to the Schwarzman Scholars program. 
The timing couldn’t have been better. Heather, who works for the Ontario government in Toronto, was in town to speak the next day on a Women in Tech panel, hosted by the Queen’s Startup Summit.
“Goodes Hall was home to me for four years, and there was nothing better than getting to share the news of this exciting opportunity in person with people who really helped me,” Heather says, referring to Smith professors and staff.
Heather is one of 142 people worldwide, selected from over 4,000 applications, to attend the master’s degree program at Schwarzman College, Tsinghua University, in Beijing.
Inspired by the prestigious Rhodes Scholarship, the Schwarzman Scholars program aims to prepare future leaders for a world in which an understanding of China’s role in global trends is essential.
Heather first learned about Schwarzman during her fourth year in Queen’s Commerce. She even thought of applying, but held off to pursue other opportunities that might make her a stronger candidate later on.
Initially, Heather wanted to go into foreign affairs. But she developed an interest in startups as a participant in the Queen’s Innovation Centre Summer Initiative (QICSI). She and teammates Chris Labelle, BCom’14, Derek Vogt, Sc’14, Mitchell Debora, Sc’14, and Danny Lloyd, Sc’16, launched Mosaic Manufacturing, winner of the 2014 QICSI Pitch Competition.
Her second venture was Spreza, a speech transcription software technology. It launched as part of The Next 36_,_ a Canadian entrepreneurial leadership program. “When I was accepted into The Next 36 it made sense for me to really try and push myself and see what I could do with startups,” Heather explains.
But a year ago Spreza went open source, and within days Heather accepted a contract position with the Ontario government in the Disruptive Technologies Unit of the Research Science and Strategy Division.
“I joke that one of the worst weeks of my life turned into the best possible opportunity,” she says. Today she’s Senior Advisor of Advanced Technologies with the Ontario Ministry of Economic Development and Growth.
Heather says her experience working for the government, particularly leading the Canadian delegation to the G7 Youth Summit in Rome earlier this year, inspired her to look again at the Schwarzman Scholar program.
“I don’t know what I want to do with my career still, but China’s economy is growing faster than any other country in the world. I think it would be a really big missed opportunity if I didn’t invest time now in understanding a little bit more of what’s going on and building some relationships there.”
At Schwarzman, Heather’s studies will include a one-year Master of Global Affairs with concentration in one of three disciplines: public policy, economics and business or international studies. She’ll also get first-hand experiences — internships, mentoring, extensive travel and networking — to learn about China and its role in the world. She’ll be joined by students from 39 countries and 97 universities. The class of 2019 starts next August.
“The opportunity to live with people who have such different experiences than my own is really exciting,” Heather says. “It’s a big, diverse mix, so I’m really excited to live with them, to learn from them and with them, and to travel China with them.”

