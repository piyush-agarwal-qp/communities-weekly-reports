# weekly error report — 2026-08-21 to 2026-08-27

**date range:** 2026-08-21 → 2026-08-27
**total errors:** 26
**clusters:** 7

---

## summary table

| # | sev | root cause | count | dc | side | dates |
|---|-----|-----------|-------|-----|------|-------|
| 1 | high | java.lang.IllegalArgumentException: /web/questionpro/qp_userimages/sub-3/3368204 | 14 | EU+US | portal | 2026-08-21 → 2026-08-25 |
| 2 | low | java.lang.NullPointerException: Cannot invoke "com.surveyconsole.micropanel.prof | 2 | US | other | 2026-08-25 |
| 3 | low | java.util.ConcurrentModificationException | 2 | US | other | 2026-08-25 |
| 4 | low | java.lang.NullPointerException: Cannot invoke "com.surveyconsole.user.User.getAc | 2 | EU | panel | 2026-08-25 |
| 5 | low | java.lang.IndexOutOfBoundsException: Index 0 out of bounds for length 0 | 2 | US | other | 2026-08-24 |
| 6 | low | java.lang.NullPointerException: Cannot invoke "com.surveyconsole.batch.Processin | 2 | EU | other | 2026-08-24 |
| 7 | low | java.lang.NullPointerException: Cannot invoke "com.surveyconsole.micropanel.Pane | 2 | EU | panel | 2026-08-24 |

---

## dc & side breakdown

| dc | portal | panel | other |
|----|--------|-------|-------|
| us | 1 | 0 | 3 |
| eu | 1 | 2 | 1 |

---

## cluster details

### 1. java.lang.IllegalArgumentException: /web/questionpro/qp_userimages/sub *(high, 14 hits)*

**dc / side:** eu + us · portal
**endpoint:** `survey-angular.panel.GlobalDataAJSHandler-GetPanelSpaceDetails`
**dates:** 2026-08-21 → 2026-08-25
**affected hosts:** mrlabs, pveuqprun2.questionpro.net, pveuqprun3.questionpro.net, uilabs1
**error ids (sample 5/14):** 2540186, 2537878, 2537876, 2537875, 2537874

**request context:**

- referer: `https://uilabs1.questionpro.com/a/showDiscussionModeration.do`
- ip: `123.201.33.202` (IN)

**root cause:**
```
java.lang.IllegalArgumentException: /web/questionpro/qp_userimages/sub-3/3368204/panel/164769 does not exist
```

**codebase frames:**
```
at com.surveyconsole.micropanel.Panel.getTotalUsedSpaceForPanelInMB(Panel.java:22772)
at com.surveyconsole.angular.panel.GlobalDataAJSHandler.apiGetPanelSpaceDetails(GlobalDataAJSHandler.java:26)
```

---

### 2. java.lang.NullPointerException: Cannot invoke "com.surveyconsole.micro *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `/a/showSampleBalancing.do`
**dates:** 2026-08-25
**affected hosts:** mrlabs
**error ids (sample 2/2):** 2537889, 2537889

**request context:**

- referer: `https://mrlabs.questionpro.com/a/showSampleBalancing.do?lcfpn=false`

**root cause:**
```
java.lang.NullPointerException: Cannot invoke "com.surveyconsole.micropanel.profile.PanelMemberCustomField.getFieldTitleDisplay()" because the return value of "com.surveyconsole.micropanel.Panel.getPanelMemberCustomField(long)" is null
```

**codebase frames:**
```
at com.surveyconsole.micropanel.quota.QuotaMapping.getCustomFieldElementEditHTML(QuotaMapping.java:277)
at com.surveyconsole.micropanel.quota.QuotaMapping.getHTMLGrid(QuotaMapping.java:154)
at com.surveyconsole.application.logs.filter.MDCFilter.filter(MDCFilter.java:26)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
at com.surveyconsole.intercom.IntercomAppFilter.filter(IntercomAppFilter.java:28)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
```

---

### 3. java.util.ConcurrentModificationException *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `/a/showSampleBalancing.do`
**dates:** 2026-08-25
**affected hosts:** mrlabs
**error ids (sample 2/2):** 2537885, 2537885

**request context:**

- referer: `https://mrlabs.questionpro.com/a/showSampleBalancing.do?lcfpn=false`

**root cause:**
```
java.util.ConcurrentModificationException
```

**codebase frames:**
```
at com.surveyconsole.micropanel.quota.QuotaMapping.getHTMLGrid(QuotaMapping.java:204)
at com.surveyconsole.application.logs.filter.MDCFilter.filter(MDCFilter.java:26)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
at com.surveyconsole.intercom.IntercomAppFilter.filter(IntercomAppFilter.java:28)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
at com.surveyconsole.infra.XSSPreventionFilter.filter(XSSPreventionFilter.java:131)
```

---

### 4. java.lang.NullPointerException: Cannot invoke "com.surveyconsole.user. *(low, 2 hits)*

**dc / side:** eu · panel
**endpoint:** `/a/showPanelManagement.do`
**dates:** 2026-08-25
**affected hosts:** pveuqpweb3.questionpro.net
**error ids (sample 2/2):** 2536577, 2536577

**request context:**

- referer: `https://eu.questionpro.com/a/showPanelManagement.do`

**root cause:**
```
java.lang.NullPointerException: Cannot invoke "com.surveyconsole.user.User.getActivePanel()" because "<local37>" is null
```

**codebase frames:**
```
at com.surveyconsole.application.logs.filter.MDCFilter.filter(MDCFilter.java:26)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
at com.surveyconsole.intercom.IntercomAppFilter.filter(IntercomAppFilter.java:28)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
at com.surveyconsole.infra.XSSPreventionFilter.filter(XSSPreventionFilter.java:131)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
```

---

### 5. java.lang.IndexOutOfBoundsException: Index 0 out of bounds for length  *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `/a/loadResponse.do`
**dates:** 2026-08-24
**affected hosts:** qpweb2.questionpro.net
**error ids (sample 2/2):** 2532339, 2532339

**request context:**

- referer: `https://www.questionpro.com/a/frame.do?mode=viewIndividual&surveyID=6EIRNPJwzzszXBSuMDP3ezLNF.iRa7Hcxqq3xxaXVYw-&responseSetID=MISq3K5RSARJsCYIimxLNGZ8GFm.uOeRyTYzGiK2rjs-`
- params: `surveyID=13738675&responseSetID=150562087`

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

### 6. java.lang.NullPointerException: Cannot invoke "com.surveyconsole.batch *(low, 2 hits)*

**dc / side:** eu · other
**endpoint:** `/a/showPanelProject.do`
**dates:** 2026-08-24
**affected hosts:** pveuqpweb3.questionpro.net
**error ids (sample 2/2):** 2516505, 2516505

**request context:**

- referer: `https://eu.questionpro.com/a/showPanelProject.do?lcfpn=false`

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
at com.surveyconsole.infra.XSSPreventionFilter.filter(XSSPreventionFilter.java:131)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
```

---

### 7. java.lang.NullPointerException: Cannot invoke "com.surveyconsole.micro *(low, 2 hits)*

**dc / side:** eu · panel
**endpoint:** `/a/editPanelMember.do`
**dates:** 2026-08-24
**affected hosts:** pveuqpweb4.questionpro.net
**error ids (sample 2/2):** 2516438, 2516438

**request context:**

- referer: `https://eu.questionpro.com/a/showPanelUserReport.do?lcfpn=false`
- params: `ajax=true&engine=dojo&ID=26619565`

**root cause:**
```
java.lang.NullPointerException: Cannot invoke "com.surveyconsole.micropanel.PanelMember.getMemberNotes()" because "member" is null
```

**codebase frames:**
```
at com.surveyconsole.micropanel.PanelMemberNotesCache.<init>(PanelMemberNotesCache.java:17)
at com.surveyconsole.micropanel.EditPanelMemberAction.setNotesCacheObjectInSession(EditPanelMemberAction.java:61)
at com.surveyconsole.micropanel.EditPanelMemberAction.doPerform(EditPanelMemberAction.java:45)
at com.bhaskaran.ui.ActionAdapter.lambda$perform$0(ActionAdapter.java:299)
at com.bhaskaran.performance.iron.PerformanceLogUtil.executeWithLoggingIfPossible(PerformanceLogUtil.java:34)
at com.bhaskaran.ui.ActionAdapter.perform(ActionAdapter.java:298)
```

---

## pdm report

```
26 errors logged (2026-08-21 → 2026-08-27)

us dc — 0 panel, 1 portal
eu dc — 2 panel, 1 portal
```

---

## engineering update

```
26 errors | panel-0, portal-1 (us) | panel-2, portal-1 (eu)

~ 14  : [2026-08-21→2026-08-25] java.lang.illegalargumentexception: /web/questionpro/qp_userimages/sub-3/3368204/panel/164769 does n — survey-angular.panel.GlobalDataAJSHandler-GetPanelSpaceDetails
```