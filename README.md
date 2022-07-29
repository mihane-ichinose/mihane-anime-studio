# Mihane Anime Studio
> 欢迎使用！本系统——MAS是根据原JST Comic Studio书面系统及JST原版手抄第一、二版汇集改编而成的电子番组在线信息系统。
## Introduction
**Mihane Anime Studio** (*abbrev. **MAS***) is a website based on a database file written in the form of Google Sheet. The website could check all contents in the database and give back the data from it.
To visit the webpage:

[Mihane Anime Studio - MAS](http://mihane.cc/)
# New Features
## Universal
### Version 2.0
#### 2022.07.20
- This new universal version release has changed the website structure completely. The website no longer runs on GitHub server. New features need Python script to run with Flask framework and deployed onto Heroku as web app.
- Added anime list with BiliBili styling and fetches info from AGE Anime. The anime list is updated every time when user visit the page.
#### 2022.07.26
- Hotfix: Fit columns of anime list to some devices that has narrow width such as smartphones. Fixed the issue that date on top cannot be seen in the same page.
- Added date and time when the info fetched on the top of the anime list.
#### 2022.07.30
- Hotfix: Prevented resubmission confirmation to pop up when user refresh the anime list page to provide a flawless experience.
## Mobile Version
### Version 1.0.3m
#### 2021.04.13
- Added new filtering for starred bangumi to show current trending.
### Version 1.0.2m
#### 2020.07.03
- Fixed a bug where non-decided season bangumi would occur in every filtering result.
- Added new filtering for non-decided season bangumi.
### Version 1.0.1m
#### 2020.06.24
- New mobile version webpage has been released! Now all mobile devices will redirect to this webpage by default.
- Cancelled the import from Owl Carousel in mobile page version.
## PC Version
### Version 1.2.4
#### 2021.04.13
- Added new filtering for starred bangumi to show current trending.
### Version 1.2.3
#### 2020.07.13
- Fixed a bug where using Enter when searching would refresh the webpage.
- Improved user performance on searching including Enter shortcut.
### Version 1.2.2
#### 2020.07.03
- Imported jQuery Mousewheel Plugin for smooth sliding experience in owl carousel.
- Fixed a bug where non-decided season bangumi would occur in every filtering result.
- Added new filtering for non-decided season bangumi.
### Version 1.2.1
#### 2020.06.24
- Entrance to mobile version added.
### Version 1.2.0
#### 2020.06.05
- Abandoned the iframe quotage at the index page, changed to jQuery method to improve the table view to fit best theme.
### Version 1.1.0a
#### 2020.05.20
- Improved system clock viewing.
### Version 1.1.0
#### 2020.04.21
- Finished the development of 'All Bangumi' page, the feature of filtering year and season of bangumi is now possible!
- Improved user interface.
### Version 1.0.5b
#### 2020.04.12
- Change the background of top banner without quoting other websites.
- Fixed a bug when non-url coding exists in some Bangumi names, OPs and EDs.
### Version 1.0.5a
#### 2020.04.08
- Added link to OP & EDs to the Netease Music seaching page.
### Version 1.0.5
#### 2020.04.08
- Improved UI colouring.
- Depreciate old menu and created a new navigation bar.
### Version 1.0.4
#### 2020.04.07
##### Due to non-standard git format previously (no git init), all commits before this version has been forced wiped... Apologies.
- Improved the format of the searching result in carousel.
- Add a new subpage for update log in the webpage.
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
- [Sublime Text 3](https://www.sublimetext.com/3) - Alternative develop tool
## Acknowledgements
- [Sweet Alert](https://sweetalert.js.org/)
- [Owl Carousel 2](https://owlcarousel2.github.io/OwlCarousel2/)
- [jQuery-Mousewheel](https://github.com/jquery/jquery-mousewheel/)
- [Baidu Baike](https://baike.baidu.com/)
- [Netease Music](https://music.163.com/)
- [BiliBili](https://www.bilibili.com/)
- [AGE Anime](https://www.agemys.cc/)
## Author
- [Mihane Ichinose](https://space.bilibili.com/5049780?from=search&seid=7121011517825966874)
