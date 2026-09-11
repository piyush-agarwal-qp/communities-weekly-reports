# weekly error report — 2026-09-04 to 2026-09-10

**date range:** 2026-09-04 → 2026-09-10
**total errors:** 76
**clusters:** 10

---

## summary table

| # | sev | root cause | count | dc | side | dates |
|---|-----|-----------|-------|-----|------|-------|
| 1 | high | java.lang.NullPointerException: Cannot invoke "com.surveyconsole.micropanel.prof | 42 | US | other | 2026-09-05 → 2026-09-09 |
| 2 | medium | javax.servlet.jsp.JspException: No getter method available for property disableM | 8 | EU+US | other | 2026-09-04 → 2026-09-07 |
| 3 | medium | java.lang.IndexOutOfBoundsException: Index 0 out of bounds for length 0 | 6 | US | other | 2026-09-04 → 2026-09-09 |
| 4 | medium | Cannot invoke "String.length()" because "ipAddress" is nulljava.lang.NullPointer | 6 | US | other | 2026-09-09 |
| 5 | medium | org.json.JSONException: JSONObject["sampleLimit"] is not an int. | 4 | EU+US | portal | 2026-09-07 → 2026-09-08 |
| 6 | low | java.lang.NullPointerException: Cannot invoke "javax.mail.Address.toString()" be | 2 | EU | other | 2026-09-09 |
| 7 | low | javax.mail.internet.AddressException: Illegal address in string ``'' | 2 | EU | other | 2026-09-09 |
| 8 | low | java.lang.NullPointerException: Cannot invoke "com.surveyconsole.batch.Processin | 2 | EU | panel | 2026-09-08 |
| 9 | low | You have an error in your SQL syntax; check the manual that corresponds to your  | 2 | EU | other | 2026-09-08 |
| 10 | low | com.surveyconsole.infra.SurveyNotFoundException: Survey not found for surveyId:  | 2 | US | other | 2026-09-05 |

---

## dc & side breakdown

| dc | portal | panel | other |
|----|--------|-------|-------|
| us | 1 | 0 | 5 |
| eu | 1 | 1 | 4 |

---

## cluster details

### 1. java.lang.NullPointerException: Cannot invoke "com.surveyconsole.micro *(high, 42 hits)*

**dc / side:** us · other
**endpoint:** `survey-angular.panel.profile.ajs.iron.PanelProfileAJSHandler-GetProfileFieldByID`
**dates:** 2026-09-05 → 2026-09-09
**affected hosts:** pvqpadminapp2.se, qprun3.questionpro.net, qprun6
**error ids (sample 5/42):** 2696986, 2651680, 2651677, 2651669, 2651668

**request context:**

- referer: `https://admin.questionpro.com/a/showPanelProfile.do?lcfpn=false`
- ip: `122.170.252.177` (IN)

**root cause:**
```
java.lang.NullPointerException: Cannot invoke "com.surveyconsole.micropanel.profile.PanelMemberCustomField.updatePanelLanguageVersion(com.surveyconsole.micropanel.PanelLanguageVersion)" because "customField" is null
```

**codebase frames:**
```
at com.surveyconsole.micropanel.profile.service.iron.CustomFieldServiceImpl.getCustomField(CustomFieldServiceImpl.java:128)
at com.surveyconsole.angular.panel.profile.service.iron.PanelProfileService.getProfileField(PanelProfileService.java:87)
at com.surveyconsole.angular.panel.profile.ajs.iron.PanelProfileAJSHandler.apiGetProfileFieldByID(PanelProfileAJSHandler.java:227)
```

---

### 2. javax.servlet.jsp.JspException: No getter method available for propert *(medium, 8 hits)*

**dc / side:** eu + us · other
**endpoint:** `/a/updateSurveySecurity.do`
**dates:** 2026-09-04 → 2026-09-07
**affected hosts:** pveuqpweb1.questionpro.net, qpweb1.questionpro.net
**error ids (sample 5/8):** 2662153, 2662152, 2662151, 2641560, 2662153

**request context:**

- referer: `https://eu.questionpro.com/a/updateSurveySecurity.do?mode=display&lcfln=false`

**root cause:**
```
javax.servlet.jsp.JspException: No getter method available for property disableMultipleSessions for bean under name ExtendedSurveyFinishForm
```

**codebase frames:**
```
at com.bhaskaran.ui.tag.uiComponents.CheckboxTag.doStartTag(CheckboxTag.java:27)
at com.surveyconsole.application.logs.filter.MDCFilter.filter(MDCFilter.java:26)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
at com.surveyconsole.intercom.IntercomAppFilter.filter(IntercomAppFilter.java:28)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
at com.surveyconsole.infra.XSSPreventionFilter.filter(XSSPreventionFilter.java:132)
```

---

### 3. java.lang.IndexOutOfBoundsException: Index 0 out of bounds for length  *(medium, 6 hits)*

**dc / side:** us · other
**endpoint:** `/a/loadResponse.do`
**dates:** 2026-09-04 → 2026-09-09
**affected hosts:** qpweb2.questionpro.net, qpweb3.questionpro.net
**error ids (sample 5/6):** 2686352, 2656827, 2645804, 2686352, 2656827

**request context:**

- referer: `https://www.questionpro.com/a/frame.do?mode=viewIndividual&surveyID=DOXycgwYRZPkP5MXMSbm6wPqFZdVELtgg8k.JPpAVXM-&responseSetID=2jb17DrkYAaOKHU8dbwE7BPpHl6J.4c6NdIS1GwyJy4-`
- params: `surveyID=13719778&responseSetID=142742715`

**root cause:**
```
java.lang.IndexOutOfBoundsException: Index 0 out of bounds for length 0
```

**codebase frames:**
```
at com.surveyconsole.html.TEXTLoader.loadInternal(TEXTLoader.java:44)
at com.surveyconsole.html.Loader.load(Loader.java:36)
at com.surveyconsole.analysis.ResponseLoader.loadData(ResponseLoader.java:832)
at com.surveyconsole.analysis.ResponseLoader.loadSectionResponse(ResponseLoader.java:776)
at com.surveyconsole.analysis.ResponseLoader.load(ResponseLoader.java:718)
at com.surveyconsole.analysis.ResponseLoader.load(ResponseLoader.java:695)
```

---

### 4. Cannot invoke "String.length()" because "ipAddress" is nulljava.lang.N *(medium, 6 hits)*

**dc / side:** us · other
**endpoint:** `/a/showQPointIncentive.do`
**dates:** 2026-09-09
**affected hosts:** pvqpadminapp2.se
**error ids (sample 5/6):** 2685702, 2685197, 2685193, 2685702, 2685197

**request context:**

- referer: `https://admin.questionpro.com/a/showQPointIncentive.do?lcfpn=false`
- params: `ajax=true&engine=dojo&lcfpn=true&_suid=178894906433309349655757249588`

**root cause:**
```
Cannot invoke "String.length()" because "ipAddress" is nulljava.lang.NullPointerException: Cannot invoke "String.length()" because "ipAddress" is null
```

**codebase frames:**
```
at com.surveyconsole.micropanel.reward.QPointRewardApprovalLog.setIpAddress(QPointRewardApprovalLog.java:144)
at com.surveyconsole.micropanel.reward.QPointRewardApprovalLogHelper.populateObject(QPointRewardApprovalLogHelper.java:348)
at com.surveyconsole.micropanel.Panel$137.buildObject(Panel.java:13526)
at com.bhaskaran.database.PreparedConnectionCommand.processResultSet(PreparedConnectionCommand.java:104)
at com.bhaskaran.database.PreparedConnectionCommand.executeWithConnection(PreparedConnectionCommand.java:55)
at com.bhaskaran.database.ConnectionCommand.execute(ConnectionCommand.java:66)
```

---

### 5. org.json.JSONException: JSONObject["sampleLimit"] is not an int. *(medium, 4 hits)*

**dc / side:** eu + us · portal
**endpoint:** `/a/showPanelProject.do`
**dates:** 2026-09-07 → 2026-09-08
**affected hosts:** pveuqprun2.questionpro.net, qpweb1.questionpro.net
**error ids (sample 4/4):** 2670587, 2660904, 2670587, 2660904

**request context:**

- referer: `https://www.questionpro.com/a/showPanelProject.do?lcfpn=false`
- ip: `2402:e280:3eb4:352:7309:f39:782d:278f` (IN)

**root cause:**
```
org.json.JSONException: JSONObject["sampleLimit"] is not an int.
```

**codebase frames:**
```
at com.surveyconsole.micropanel.project.PanelProjectDeliveryOption.isValidSampleLimitSelected(PanelProjectDeliveryOption.java:217)
at com.surveyconsole.micropanel.project.PanelProjectDeliveryOption.isSampleSelectionEnabledAndInValidSampleLimitSelected(PanelProjectDeliveryOption.java:192)
at com.surveyconsole.micropanel.project.PanelProjectDeliveryOption.fromJSON(PanelProjectDeliveryOption.java:177)
at com.surveyconsole.micropanel.project.PanelProjectCampaign.populateFormWithDeliveryDetail(PanelProjectCampaign.java:131)
at com.surveyconsole.micropanel.project.PanelProjectCampaign.createBatchFromJSON(PanelProjectCampaign.java:51)
at com.surveyconsole.angular.panel.PanelFilterAJSHandler.apiSendSurveyToFilteredMember(PanelFilterAJSHandler.java:116)
```

---

### 6. java.lang.NullPointerException: Cannot invoke "javax.mail.Address.toSt *(low, 2 hits)*

**dc / side:** eu · other
**endpoint:** `(unknown)`
**dates:** 2026-09-09
**affected hosts:** pveuadminapp1.questionpro.net
**error ids (sample 2/2):** 2689976, 2689976

**root cause:**
```
java.lang.NullPointerException: Cannot invoke "javax.mail.Address.toString()" because "<parameter1>[<local3>]" is null
```

**codebase frames:**
```
at com.surveyconsole.micropanel.PanelMember.addReplyToEmail(PanelMember.java:3793)
at com.surveyconsole.micropanel.PanelMember.sendEmail(PanelMember.java:3721)
at com.surveyconsole.micropanel.PanelMember.sendEmail(PanelMember.java:3652)
at com.surveyconsole.micropanel.PanelMember.sendDoubleOptIntVerification(PanelMember.java:2441)
at com.surveyconsole.micropanel.PanelMember.sendMemberNotificationEmail(PanelMember.java:4102)
at com.surveyconsole.micropanel.BulkInsertPanelMemberProcessor$3.runLogged(BulkInsertPanelMemberProcessor.java:617)
```

---

### 7. javax.mail.internet.AddressException: Illegal address in string ``'' *(low, 2 hits)*

**dc / side:** eu · other
**endpoint:** `(unknown)`
**dates:** 2026-09-09
**affected hosts:** pveuadminapp1.questionpro.net
**error ids (sample 2/2):** 2689975, 2689975

**root cause:**
```
javax.mail.internet.AddressException: Illegal address in string ``''
```

**codebase frames:**
```
at com.surveyconsole.micropanel.send.preference.SMTPEmailAddressManager.getReplyToEmail(SMTPEmailAddressManager.java:58)
at com.surveyconsole.micropanel.PanelMember$ContactOptions.updateSMTPPreferenceEmails(PanelMember.java:4157)
at com.surveyconsole.micropanel.PanelMember$ContactOptions.initializeCommunitiesEmailsConfig(PanelMember.java:4148)
at com.surveyconsole.micropanel.PanelMember$ContactOptions.<init>(PanelMember.java:4141)
at com.surveyconsole.micropanel.PanelMember.sendDoubleOptIntVerification(PanelMember.java:2430)
at com.surveyconsole.micropanel.PanelMember.sendMemberNotificationEmail(PanelMember.java:4102)
```

---

### 8. java.lang.NullPointerException: Cannot invoke "com.surveyconsole.batch *(low, 2 hits)*

**dc / side:** eu · panel
**endpoint:** `/a/showPanelProjectHistory.do`
**dates:** 2026-09-08
**affected hosts:** pveuqprun3.questionpro.net
**error ids (sample 2/2):** 2670196, 2670196

**request context:**

- referer: `https://onepoll.questionpro.eu/a/showPanelProjectHistory.do?lcfpn=false`

**root cause:**
```
java.lang.NullPointerException: Cannot invoke "com.surveyconsole.batch.ProcessingItem.getClassName()" because "<local34>" is null
```

**codebase frames:**
```
at com.surveyconsole.application.logs.filter.MDCFilter.filter(MDCFilter.java:26)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
at com.surveyconsole.intercom.IntercomAppFilter.filter(IntercomAppFilter.java:28)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
at com.surveyconsole.infra.XSSPreventionFilter.filter(XSSPreventionFilter.java:132)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
```

---

### 9. You have an error in your SQL syntax; check the manual that correspond *(low, 2 hits)*

**dc / side:** eu · other
**endpoint:** `/a/showPanelSegment.do`
**dates:** 2026-09-08
**affected hosts:** pveuqpweb4.questionpro.net
**error ids (sample 2/2):** 2670161, 2670161

**request context:**

- referer: `https://eu.questionpro.com/a/showPanelSample.do?lcfpn=false`
- params: `ajax=true&engine=dojo&mode=count&segmentID=1602638435`

**root cause:**
```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '))' at line 1
```

**codebase frames:**
```
at com.bhaskaran.database.PreparedConnectionCommand.executeWithConnection(PreparedConnectionCommand.java:75)
at com.bhaskaran.database.ConnectionCommand.execute(ConnectionCommand.java:66)
at com.bhaskaran.database.PreparedConnectionCommand.execute(PreparedConnectionCommand.java:117)
at com.bhaskaran.database.CountCommand.executeLong(CountCommand.java:31)
at com.surveyconsole.micropanel.Panel.getPanelMemberCount(Panel.java:4825)
at com.surveyconsole.micropanel.PanelSegment.getCount(PanelSegment.java:85)
```

---

### 10. com.surveyconsole.infra.SurveyNotFoundException: Survey not found for  *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `/a/SurveyPreview`
**dates:** 2026-09-05
**affected hosts:** qprun3.questionpro.net
**error ids (sample 2/2):** 2651524, 2651524

**request context:**

- referer: `https://utep.questionpro.com/cs/ui/su/edit-survey/surveys/13776044?lang=1`
- params: `surveyId=13776044`

**root cause:**
```
com.surveyconsole.infra.SurveyNotFoundException: Survey not found for surveyId: 13776044
```

**codebase frames:**
```
at com.surveyconsole.user.User.getEditableSurvey(User.java:4448)
at com.surveyconsole.user.SurveyPreviewServlet.validateRequestOrThrow(SurveyPreviewServlet.java:114)
at com.surveyconsole.user.SurveyPreviewServlet.refreshActiveSurveyInSessionAndGet(SurveyPreviewServlet.java:87)
at com.surveyconsole.user.SurveyPreviewServlet.doServiceUser(SurveyPreviewServlet.java:33)
at com.surveyconsole.user.UserAccessServletAdapter.doService(UserAccessServletAdapter.java:31)
at com.bhaskaran.ui.ServletAdapter.lambda$doPost$0(ServletAdapter.java:200)
```

---

## pdm report

```
76 errors logged (2026-09-04 → 2026-09-10)

us dc — 0 panel, 1 portal
eu dc — 1 panel, 1 portal
```

---

## engineering update

```
76 errors | panel-0, portal-1 (us) | panel-1, portal-1 (eu)

~ 42  : [2026-09-05→2026-09-09] java.lang.nullpointerexception: cannot invoke "com.surveyconsole.micropanel.profile.panelmembercusto — survey-angular.panel.profile.ajs.iron.PanelProfileAJSHandler-GetProfileFieldByID
~ 8   : [2026-09-04→2026-09-07] javax.servlet.jsp.jspexception: no getter method available for property disablemultiplesessions for  — /a/updateSurveySecurity.do
~ 6   : [2026-09-04→2026-09-09] java.lang.indexoutofboundsexception: index 0 out of bounds for length 0 — /a/loadResponse.do
~ 6   : [2026-09-09] cannot invoke "string.length()" because "ipaddress" is nulljava.lang.nullpointerexception: cannot in — /a/showQPointIncentive.do
```