# weekly error report — 2026-08-28 to 2026-09-03

**date range:** 2026-08-28 → 2026-09-03
**total errors:** 30
**clusters:** 7

---

## summary table

| # | sev | root cause | count | dc | side | dates |
|---|-----|-----------|-------|-----|------|-------|
| 1 | high | Cannot invoke "String.length()" because "ipAddress" is nulljava.lang.NullPointer | 10 | US | other | 2026-09-01 |
| 2 | medium | java.lang.NullPointerException: Cannot invoke "com.surveyconsole.infra.Survey.ge | 6 | US | other | 2026-09-02 |
| 3 | medium | org.json.JSONException: JSONObject["title"] not found. | 4 | EU | portal | 2026-09-01 → 2026-09-02 |
| 4 | medium | Root Exception : | 4 | US | panel | 2026-09-02 |
| 5 | low | com.surveyconsole.batch.error.ProcessingItemRejectedException: Rejected! Another | 2 | US | other | 2026-09-02 |
| 6 | low | java.lang.NullPointerException: Cannot invoke "com.surveyconsole.infra.Survey.ge | 2 | US | other | 2026-08-28 |
| 7 | low | java.lang.IndexOutOfBoundsException: Index 0 out of bounds for length 0 | 2 | US | other | 2026-08-28 |

---

## dc & side breakdown

| dc | portal | panel | other |
|----|--------|-------|-------|
| us | 0 | 1 | 5 |
| eu | 1 | 0 | 0 |

---

## cluster details

### 1. Cannot invoke "String.length()" because "ipAddress" is nulljava.lang.N *(high, 10 hits)*

**dc / side:** us · other
**endpoint:** `/a/showQPointIncentive.do`
**dates:** 2026-09-01
**affected hosts:** pvqpadminapp1.se
**error ids (sample 5/10):** 2617744, 2617734, 2606829, 2606815, 2606812

**request context:**

- referer: `https://admin.questionpro.com/a/showQPointIncentive.do?lcfpn=false`
- params: `ajax=true&engine=dojo&lcfpn=true&_suid=178833042963206373076912000619`

**root cause:**
```
Cannot invoke "String.length()" because "ipAddress" is nulljava.lang.NullPointerException: Cannot invoke "String.length()" because "ipAddress" is null
```

**codebase frames:**
```
at com.surveyconsole.micropanel.reward.QPointRewardApprovalLog.setIpAddress(QPointRewardApprovalLog.java:144)
at com.surveyconsole.micropanel.reward.QPointRewardApprovalLogHelper.populateObject(QPointRewardApprovalLogHelper.java:348)
at com.surveyconsole.micropanel.Panel$137.buildObject(Panel.java:13527)
at com.bhaskaran.database.PreparedConnectionCommand.processResultSet(PreparedConnectionCommand.java:104)
at com.bhaskaran.database.PreparedConnectionCommand.executeWithConnection(PreparedConnectionCommand.java:55)
at com.bhaskaran.database.ConnectionCommand.execute(ConnectionCommand.java:66)
```

---

### 2. java.lang.NullPointerException: Cannot invoke "com.surveyconsole.infra *(medium, 6 hits)*

**dc / side:** us · other
**endpoint:** `/a/showPanelPollReport.do`
**dates:** 2026-09-02
**affected hosts:** qpweb1.questionpro.net
**error ids (sample 5/6):** 2624531, 2624525, 2624520, 2624531, 2624525

**request context:**

- referer: `https://www.questionpro.com/a/showPanelPollSetup.do`
- params: `ajax=true&engine=dojo&pollID=13771227`

**root cause:**
```
java.lang.NullPointerException: Cannot invoke "com.surveyconsole.infra.Survey.getSection(long)" because "poll" is null
```

**codebase frames:**
```
at com.surveyconsole.micropanel.polls.PanelPollResultStats.<init>(PanelPollResultStats.java:50)
at com.surveyconsole.micropanel.polls.ShowPanelPollReportAction.doPerform(ShowPanelPollReportAction.java:49)
at com.bhaskaran.ui.ActionAdapter.lambda$perform$0(ActionAdapter.java:299)
at com.bhaskaran.performance.iron.PerformanceLogUtil.executeWithLoggingIfPossible(PerformanceLogUtil.java:34)
at com.bhaskaran.ui.ActionAdapter.perform(ActionAdapter.java:298)
at com.surveyconsole.application.logs.filter.MDCFilter.filter(MDCFilter.java:26)
```

---

### 3. org.json.JSONException: JSONObject["title"] not found. *(medium, 4 hits)*

**dc / side:** eu · portal
**endpoint:** `survey-angular.panel.portal.PortalDashBoardAJSHandler-GetSurveyDetails`
**dates:** 2026-09-01 → 2026-09-02
**affected hosts:** pveuqprun2.questionpro.net
**error ids (sample 4/4):** 2622063, 2617227, 2622063, 2617227

**request context:**

- referer: `https://codeo.questionpro.eu/a/showPanelMemberDashBoard.do?lppn=false`
- ip: `2401:4900:88fa:a117:fc7b:b6d4:5136:9ef7` (IN)

**root cause:**
```
org.json.JSONException: JSONObject["title"] not found.
```

**codebase frames:**
```
at com.surveyconsole.micropanel.portal.landing.PortalDashBoardSurveyFetcher.getSurveyJSONArray(PortalDashBoardSurveyFetcher.java:58)
at com.surveyconsole.micropanel.portal.landing.PortalDashBoardSurveyFetcher.toJSONForSurvey(PortalDashBoardSurveyFetcher.java:30)
at com.surveyconsole.angular.panel.portal.PortalDashBoardAJSHandler.apiGetSurveyDetails(PortalDashBoardAJSHandler.java:26)
```

---

### 4. Root Exception : *(medium, 4 hits)*

**dc / side:** us · panel
**endpoint:** `/a/pushNotificationToMember.do`
**dates:** 2026-09-02
**affected hosts:** qpweb1.questionpro.net
**error ids (sample 4/4):** 2621499, 2621497, 2621499, 2621497

**request context:**

- referer: `https://www.questionpro.com/a/showPanelUserReport.do?lcfpn=false`
- params: `ajax=true&engine=dojo&panelMemberID=17406243&panelLogID=179945746`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.httputil.HttpUtility.readMultipleLineResponse(HttpUtility.java:148)
at com.surveyconsole.httputil.HttpUtility.getMultipleLineResponseAsString(HttpUtility.java:162)
at com.surveyconsole.micropanel.surveyswipe.pushnotification.PushNotificationService.sendPushNotification(PushNotificationService.java:31)
at com.surveyconsole.micropanel.surveyswipe.pushnotification.PanelPushNotificationService.sendNotification(PanelPushNotificationService.java:32)
at com.surveyconsole.micropanel.PanelLog.sendNativeAppNotification(PanelLog.java:1177)
at com.surveyconsole.micropanel.PanelLog.pushNotification(PanelLog.java:1164)
```

---

### 5. com.surveyconsole.batch.error.ProcessingItemRejectedException: Rejecte *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-09-02
**affected hosts:** qpweb3.questionpro.net
**error ids (sample 2/2):** 2625028, 2625028

**root cause:**
```
com.surveyconsole.batch.error.ProcessingItemRejectedException: Rejected! Another process already in progress
```

**codebase frames:**
```
at com.surveyconsole.batch.LongProcessHandler.startProcessingForCommunities(LongProcessHandler.java:101)
at com.surveyconsole.micropanel.broadcast.SendBroadcastHandler.processBroadcastNotification(SendBroadcastHandler.java:39)
at com.surveyconsole.micropanel.broadcast.SendBroadcastHandler.sendBroadcastNotification(SendBroadcastHandler.java:30)
at com.surveyconsole.micropanel.analysis.SendBroadcastNotificationAction.doPerformBroadcast(SendBroadcastNotificationAction.java:63)
at com.surveyconsole.micropanel.PanelBroadcastEmailAction.doPerform(PanelBroadcastEmailAction.java:44)
at com.bhaskaran.ui.ActionAdapter.lambda$perform$0(ActionAdapter.java:299)
```

---

### 6. java.lang.NullPointerException: Cannot invoke "com.surveyconsole.infra *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `/a/updateGlobalAgeVerificationSetting.do`
**dates:** 2026-08-28
**affected hosts:** qpweb2.questionpro.net
**error ids (sample 2/2):** 2575404, 2575404

**request context:**

- referer: `https://www.questionpro.com/a/showUpgradeUser.do?payment=creditCardUpdate`
- params: `ajax=true&engine=dojo&ageVerification=true`

**root cause:**
```
java.lang.NullPointerException: Cannot invoke "com.surveyconsole.infra.Survey.getResultDataSource()" because the return value of "com.surveyconsole.user.User.getActiveSurvey()" is null
```

**codebase frames:**
```
at com.surveyconsole.useradmin.surveysetting.UpdateGlobalAgeVerificationSettingAction.doPerform(UpdateGlobalAgeVerificationSettingAction.java:43)
at com.bhaskaran.ui.ActionAdapter.lambda$perform$0(ActionAdapter.java:299)
at com.bhaskaran.performance.iron.PerformanceLogUtil.executeWithLoggingIfPossible(PerformanceLogUtil.java:34)
at com.bhaskaran.ui.ActionAdapter.perform(ActionAdapter.java:298)
at com.surveyconsole.application.logs.filter.MDCFilter.filter(MDCFilter.java:26)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
```

---

### 7. java.lang.IndexOutOfBoundsException: Index 0 out of bounds for length  *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `/a/loadResponse.do`
**dates:** 2026-08-28
**affected hosts:** qpweb2.questionpro.net
**error ids (sample 2/2):** 2571254, 2571254

**request context:**

- referer: `https://www.questionpro.com/a/frame.do?mode=viewIndividual&surveyID=2WIxiT4ne29LlJ_o167hQkXKneqjK1Z7J8UqsvyuOfQ-&responseSetID=q3X7Zx7oyJlkN.WY6rf28BgIEQMT_5YbH.2nhFM23Ww-`
- params: `surveyID=13745315&responseSetID=150832808`

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

## pdm report

```
30 errors logged (2026-08-28 → 2026-09-03)

us dc — 1 panel, 0 portal
eu dc — 0 panel, 1 portal
```

---

## engineering update

```
30 errors | panel-1, portal-0 (us) | panel-0, portal-1 (eu)

~ 10  : [2026-09-01] cannot invoke "string.length()" because "ipaddress" is nulljava.lang.nullpointerexception: cannot in — /a/showQPointIncentive.do
~ 6   : [2026-09-02] java.lang.nullpointerexception: cannot invoke "com.surveyconsole.infra.survey.getsection(long)" beca — /a/showPanelPollReport.do
```