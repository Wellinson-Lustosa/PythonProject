medida = float(input('Uma  distância em metros: '))
km = medida * 0.0001
hm = medida * 0.001
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {} m coresponde a {:.6f} km {:.4f} hm {:.3f} dam {:.3f} dm {:.3f} cm {:.3f} mm'. format(medida, km, hm, dam,dm, cm, mm))