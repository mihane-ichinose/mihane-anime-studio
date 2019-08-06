# Mihane Anime Studio
> 欢迎使用！本系统——MAS是根据原JST Comic Studio书面系统及JST原版手抄第一、二版汇集改编而成的电子番组在线信息系统。
## Introduction
**Mihane Anime Studio** (*abbrev. **MAS***) is a website based on a database file written in the form of Google Sheet. The website could check all contents in the database and give back the data from it.
To visit the webpage:

[Mihane Anime Studio - MAS](http://mihane.cc/)
## Version Features
### Beta 1.0.3
#### 2019.08.06
- New prompt interface: 'Sweet Alert' has been added to the webpage.
- Change normal div searching result into 'Owl Carousel' method, which can show results into horizontally scrollable boxes.
  - Number of results has been limited to 10 at most. The old issue of body height has been solved.
- Change the JQuery resource from Google to CDNJS to solve issues that may possibly happen in some region.
  - The google API to link Google Sheet still cannot be solved in these regions.
### Beta 1.0.2
#### 2019.08.05
- Fuzzy search supported when search by Anime name.
  - Issue found: Body cannot dynamically change its height when the list is relatively long.
## Built With
- [IntelliJ IDEA](https://www.jetbrains.com/idea/) - The web framework used
## Acknowledgements
- [Sweet Alert](https://sweetalert.js.org/)
- [Owl Carousel 2](https://owlcarousel2.github.io/OwlCarousel2/)
## Author
- [Mihane Ichinose](https://space.bilibili.com/5049780?from=search&seid=7121011517825966874)
