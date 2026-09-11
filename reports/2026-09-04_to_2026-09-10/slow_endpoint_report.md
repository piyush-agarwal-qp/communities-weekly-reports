# Slow Endpoint Report: 2026-09-04 to 2026-09-10

Top 20 Slowest Queries
         • /getSurveyAbandonedMembers – Latency : 261200 ms
         • /getCrosstabResults – Latency : 3424 ms
         • /getAtRiskMembers – Latency : 2097 ms
         • /getActiveMembersTrend – Latency : 1870 ms
         • /getMembersActivityHeatmap – Latency : 1723 ms
         • /getActivityTrends – Latency : 1717 ms
         • /getEngagementDrivers – Latency : 1710 ms
         • /getSurveyResponseStatusTrends – Latency : 1703 ms
         • /getTopEngagedMembers – Latency : 1689 ms
         • /getActivityBreakdown – Latency : 1686 ms
         • /showCampaignBatch.do – Latency : 1060 ms
         • /cacheInsightDataForInterval – Latency : 961 ms
         • /getEngagementTrends – Latency : 953 ms
         • /reminderCount.do – Latency : 924 ms
         • /sendSurveyToFilteredMember – Latency : 728 ms
         • /showPanelProjectReminder.do – Latency : 593 ms
         • /approveReward.do – Latency : 541 ms
         • /showRewardHistoryLog.do – Latency : 521 ms
         • /router.do – Latency : 412 ms
         • /api/nativehtml/panel.reward.PanelRewardRedeem – Latency : 334 ms

---

## full breakdown (all endpoints seen across the week's top daily slots)

| endpoint | avg latency (ms) | total requests |
|---|---|---|
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetSurveyAbandonedMembers` | 261200 | 1 |
| `/a/ajs/survey-angular.panel.ProfileCrossTabAJSHandler-GetCrosstabResults` | 3424 | 18 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetAtRiskMembers` | 2097 | 1 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetActiveMembersTrend` | 1870 | 10 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetMembersActivityHeatmap` | 1723 | 7 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetActivityTrends` | 1717 | 7 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetEngagementDrivers` | 1710 | 7 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetSurveyResponseStatusTrends` | 1703 | 7 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetTopEngagedMembers` | 1689 | 7 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetActivityBreakdown` | 1686 | 7 |
| `/a/showCampaignBatch.do` | 1060 | 390 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-CacheInsightDataForInterval` | 961 | 7 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetEngagementTrends` | 953 | 16 |
| `/a/reminderCount.do` | 924 | 458 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-SendSurveyToFilteredMember` | 728 | 460 |
| `/a/showPanelProjectReminder.do` | 593 | 447 |
| `/a/approveReward.do` | 541 | 153 |
| `/a/showRewardHistoryLog.do` | 521 | 10 |
| `/a/router.do` | 412 | 36 |
| `/a/api/nativehtml/panel.reward.PanelRewardRedeem` | 334 | 6 |
| `/a/ajs/survey-angular.panel.portal.PortalRewardAJSHandler-RedeemReward` | 325 | 187 |
| `/a/showMembers.do` | 322 | 451 |
| `/a/showRewardResolvedLog.do` | 263 | 31 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-GetPanelFilter` | 262 | 1089 |
| `/a/searchMember.do` | 261 | 1239 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetPointsLeaderboard` | 245 | 2 |
| `/a/searchCampaignBatchProject.do` | 169 | 86 |
| `/a/showPanelSegment.do` | 167 | 1331 |
| `/a/ShareCrosstab` | 161 | 52 |
| `/a/showQPointIncentive.do` | 157 | 164 |
| `/a/showOrgUsersPanel.do` | 153 | 15 |
| `/a/ajs/survey-angular.panel.portal.PanelMemberAccountAJSHandler-GetLeaderBoard` | 130 | 1419 |
| `/a/searchSurveyCampaignBatch.do` | 116 | 1651 |
| `/a/ajs/survey-angular.panel.portal.PortalDashBoardAJSHandler-GetDiscussionDetails` | 104 | 3 |
| `/a/showLiveDiscussions.do` | 103 | 1 |
| `/a/showPanelReport.do` | 93 | 6 |
| `/a/ajs/survey-angular.panel.profile.ajs.iron.PanelProfileAJSHandler-ImportProfileFields` | 93 | 8 |
| `/a/newPanelWizardName.do` | 92 | 123 |
| `/a/ajs/survey-angular.panel.portal.PortalDashBoardAJSHandler-GetTopicDetails` | 92 | 5 |
| `/a/savePanelLandingPageImage.do` | 86 | 3 |
| `/a/ajs/survey-angular.panel.PanelDiscussionTopicAJSHandler-GetAllDeletedItems` | 85 | 2 |
| `/a/ajs/survey-angular.panel.modules.polls.iron.PanelPollAJSHandler-AddUpdatePanelPoll` | 82 | 1 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-GetPanelMemberFilterDeliveryOption` | 79 | 11 |
| `/a/showPanelMemberDashBoard.do` | 74 | 3887 |
| `/a/showProfileCrossTabReport.do` | 71 | 5 |
| `/a/showPanelHealthDashboard.do` | 60 | 21 |
| `/a/showPanelUserReport.do` | 57 | 74 |
| `/a/ajs/survey-angular.panel.portal.PortalRewardAJSHandler-GetAllAvailableRewards` | 55 | 1661 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-GetPanelMemberFilterCount` | 54 | 172 |
| `/a/ajs/survey-angular.panel.portal.DiscussionTopicAJSHandler-AddUpdateComment` | 48 | 2 |
| `/a/ajs/survey-angular.panel.analytics.pointdistribution.ajs.iron.PointDistributionAJSHandler-GetTotalPointsEarned` | 47 | 1 |
| `/a/addProfileCrosstabReport.do` | 45 | 3 |
| `/a/ajs/survey-angular.panel.portal.PortalDashBoardAJSHandler-GetSurveyDetails` | 36 | 1624 |
| `/a/ajs/survey-angular.panel.portal.PanelMemberAccountAJSHandler-UpdateProfileImage` | 36 | 1 |
| `/a/ajs/survey-angular.panel.portal.PanelMemberAccountAJSHandler-UpdateMemberDetailsFromAccount` | 34 | 7 |
| `/a/ajs/survey-angular.panel.portal.PanelMemberAccountAJSHandler-GetPointsHistory` | 30 | 318 |

---

## Copy-paste block

```
Top 20 Slowest Queries
         • /getSurveyAbandonedMembers – Latency : 261200 ms
         • /getCrosstabResults – Latency : 3424 ms
         • /getAtRiskMembers – Latency : 2097 ms
         • /getActiveMembersTrend – Latency : 1870 ms
         • /getMembersActivityHeatmap – Latency : 1723 ms
         • /getActivityTrends – Latency : 1717 ms
         • /getEngagementDrivers – Latency : 1710 ms
         • /getSurveyResponseStatusTrends – Latency : 1703 ms
         • /getTopEngagedMembers – Latency : 1689 ms
         • /getActivityBreakdown – Latency : 1686 ms
         • /showCampaignBatch.do – Latency : 1060 ms
         • /cacheInsightDataForInterval – Latency : 961 ms
         • /getEngagementTrends – Latency : 953 ms
         • /reminderCount.do – Latency : 924 ms
         • /sendSurveyToFilteredMember – Latency : 728 ms
         • /showPanelProjectReminder.do – Latency : 593 ms
         • /approveReward.do – Latency : 541 ms
         • /showRewardHistoryLog.do – Latency : 521 ms
         • /router.do – Latency : 412 ms
         • /api/nativehtml/panel.reward.PanelRewardRedeem – Latency : 334 ms
```