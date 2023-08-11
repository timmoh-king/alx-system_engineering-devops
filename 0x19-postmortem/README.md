## 0x19. Postmortem

**Posted:** Friday, August 11, 2023

*By Timothy Kariuki - ALX SE student*
<br/>

## Table of Contents
- [Issue summary](#Issue-summary)
- [Timeline](#Timeline)
- [Root cause](#Root-cause)
- [Resolution and recovery](#Resolution-and-recovery)
- [Corrective and preventative](#Corrective-and-preventative)

<br/>

*Earlier this week I experienced an outage in my server. Today I am providing an incident report that details the nature of the outage and the response*

The following is the incident report for the server infrastrucure that occured on `August 5, 2023`. I understand this service issue has impacted valued collaboratiers and users, and I apologize to everyone that was affected.

## Issue summary

From `August 4, 2023` 4:25 PM to  `August 8, 2023` 7:30 PM, requests to the ALX server `100.34.56.123` and `54.34.10.127` resulted in 500 error response messages. Applications and ALX tasks that rely on this servers also returned errors or had reduced functionality. At its peak this issue affected 100% of traffic to this server infrastructure. The root cause of this outage was technical failure of the physical server computer `Hp proBook 6470b` that failed to start hence shting down the servers.
<br/>

## Timeline (East African Time - EAT)

- August 4, 2023 3:00 PM: Configuration of servers begin
- August 4, 2023 3:25 PM: Outage begins
- August 4, 2023 4:26 PM: Pagers alert teams
- August 4, 2023 6:45 PM: Server shutdown
- August 5, 2023 2:15 PM: First attempt to restore the physical computer
- August 5, 2023 8:30 PM: 100% of traffic back online
- August 6, 2023 5:00 AM: Server shutdown
- August 8, 2023 8:45 PM: Request of new servers
- August 8, 2023 9:00 PM: configuration of new servers
- August 8, 2023 9:30 PM: Servers are back online
<br/>

## Root cause

On August 4, 2023 4:26 PM , the monitoring team systems alerted the team who quickly escalated the issue. By August 4, 2023 6:45 PM the incident response team identified that the monitoring system was exacerbating the problem caused by the server shutdown. This exposed a downtime and a complete shutdown of our servers since our host device could not power on. The computer failure caused a loss of all our server information and acquiring new servers and a computer devive was the safest and the best option to go for.
<br/>

## Resolution and recovery
On August August 4, 2023 4:26 PM, the monitoring team systems alerted the team who quickly escalated the issue. By August 4, 2023 6:45 PM the incident response team identified that the monitoring system was exacerbating the problem caused by the server shutdown.

On August 5, 2023 2:15 PM, we attampted to repair our `Hp proBook 6470b` server device. This rollback failed due to complexity and the technicality in the computer. And a computer engineer was called in to solve counter the issue. The problm was addressed and we successfully rolled back on August 5, 2023 8:30 PM

On  August 6, 2023 5:00 AM we experienced a second time server shutdown that was caused by `Hp proBook 6470b` failing to restart and caused downtime for two days. On  August 7, 2023 8:45 PM we opted to repair the host device again but resulted to failure so purchasing a new host device was the safest and last option

August 8, 2023 8:45 PM we managed to request for new servers `100.54.52.78` and `56.78.192.67` and addressed the technical bug. We successfully rolled back on August 8, 2023 9:30 PM
<br/>

## Corrective and preventative

In the last five days, we've conducted an internal revieew and analysis of the outage. The following are actions we are taking to address the underlying causes of the issue and to help prevent recurrence and improve response times:

- Disable the current configuration release mechanism until safer measures are implemnted
- Programmatically enforce staged rollouts of all configuration changes
- Backup sever information on a regular basis
- Regular computer devices audit and solve technical issues early enough

We are committed to continually and quickly improving our technology and operational processes to prevent outages. We appreciate your patience and again apologize for the impact to you users, and collaborators. We thank you for your continued support.
