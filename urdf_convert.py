from tkinter import filedialog
import pandas as pd
import urdf_temp as urdf


list_file = []
files = filedialog.askopenfilenames(initialdir="/",\
					title = "Select File",\
					filetypes = (("*.xlsx","*.xlsx"),("*.xls","*xls"),("*.csv","*csv")))
#initialdir : 파일찾기 기본 경로
#filetypes : 찾는 파일의 확장자
#title : 창의 타이틀명

#찾은 파일의 경로 - 0번째 index에 파일의 경로가 담겨있습니다.
files = list(files)


#Sheet1 정보 딕셔너리
data_Sheet1 = dict()
#Inbody 정보 딕셔너리
data_Inbody = dict()
#3DScan 정보 딕셔너리
data_3DScan = dict()

#등록번호를 저장할 리스트 (ex : W0001)
id_list = list()

def getKeyList(data) :
    key_name = list()
    for col in data:
        key_name.append(col)
    return key_name

#엑셀파일을 읽어 딕셔너리로 반환하는 함수입니다.
def getSeetDataMap(col_name, _data_list, data, key_name) :
    for col in data.index:
        data_id = ""
        data_map = dict()
        _pass = False
        for item in key_name:
            if str(data[str(col_name)][col]) != 'nan' :
                if data_id == "":
                    data_id = data[str(col_name)][col]
                data_map[str(item)] = data[str(item)][col]
            else :
                _pass = True
        if _pass == False:
            _data_list[data_id] = data_map
            if data_id.find(data_id) != -1 :
                id_list.append(data_id)
    return _data_list



def clavicle_link(id):
    """
        id : 등록번호 (ex W0001)
        어깨 길이
    """
    #id = 모든 함수에서 id는 등록번호로 사용됩니다. ex W0001
    clavicle = float(data_Sheet1[str(id)]['어깨길이'])
    values = (clavicle/2) * 0.01
    #print("쇄골 링크 길이 : "+str(values))
    return values

def chest_link(id):
    """
        id : 등록번호 (ex W0001)
        가슴 링크 지름
    """
    clavicle = float(data_3DScan[str(id)]['어깨높이'])
    chest = float(data_3DScan[str(id)]['가슴높이'])
    chest_2 = float(data_3DScan[str(id)]['(젖)가슴높이'])
    waist = float(data_3DScan[str(id)]['허리높이'])
    values =  ((clavicle - chest) +  (chest-chest_2) + ((chest_2-waist)/2)) *0.01
    #print("가슴 링크 지름 : "+str(values))
    return values


def waist_link(id):
    """
        id : 등록번호 (ex W0001)
        허리 링크 지름
    """
    chest_2 = float(data_3DScan[str(id)]['(젖)가슴높이'])
    waist = float(data_3DScan[str(id)]['허리높이'])
    low = float(data_3DScan[str(id)]['배꼽아래높이'])

    values = (((chest_2 - waist)/2) + ((waist-low)/2))*0.01

    #print("허리 링크 지름 : "+str(values))
    return values

def ventral_link(id):
    """
        id : 등록번호 (ex W0001)
        배 링크 지름
    """
    waist = float(data_3DScan[str(id)]['허리높이'])
    low = float(data_3DScan[str(id)]['배꼽아래높이'])
    sat = float(data_3DScan[str(id)]['샅높이'])

    values =  (((waist-low)/2) +  (low-sat)) *0.01

    #print("배 링크 지름 : "+str(values))
    return values

def hip_link(id):
    """
        id : 등록번호 (ex W0001)
        하지상박
    """
    leg = float(data_Sheet1[str(id)]['다리길이'])
    calf = float(data_Sheet1[str(id)]['종아리길이'])
    low = float(data_3DScan[str(id)]['배꼽아래높이'])
    hip = float(data_3DScan[str(id)]['엉덩이높이'])

    value1 = (leg-calf) * 0.01
    value2 = (low-hip) * 0.01

    #print("엉덩이기준 하지 상박 길이 : " +  str((value1 - value2)))

    return value1 - value2

def forearm_link(id):
    """
        id : 등록번호 (ex W0001)
        하지하박
    """
    calf = float(data_Sheet1[str(id)]['종아리길이'])
    values = calf * 0.01
    #print("하지 하박 길이 : " + str(values))
    return values

def shoulder_link(id) :
    """
        id : 등록번호 (ex W0001)
        상완길이
    """
    values = float(data_Sheet1[id]['상완길이'])*0.01
    #print("상완 길이 : "+str(values))
    return values

def elbow_link(id) : 
    """
        id : 등록번호 (ex W0001)
        하완길이
    """
    values = float(data_Sheet1[id]['하완길이'])*0.01
    #print("하완 길이 : "+str(values))
    return values


def degToRad(val):
   """
    Args:
        val deggre
    Returns:
        deggre값을 radian으로 계산하여 반환
    """
   
   if val == "nan":
       return "nan"

   return val * (3.14/180) 

def kgToNm(val):
    """
    Args:
        val1 kg값
    Returns:
        kg를 뉴턴으로 변환한 값
    """
    if val == "nan":
       return "nan"
    return val * 9.8066
    

def getMass(val1, val2):
    """
    Args:
        val1 
        val2
        신전력 또는 굴곡력
    Returns:
        신전력과 굴곡력 중 작은값
    """
    
    if val1 == "nan" or val2 == "nan":
       return "nan"
    if val1 > val2 :
        return val2
    else:
        return val1

def V_Avg(item ,name, total):
    """둘레 평균
    
    Args:
        item : 등록번호 (ex:W0001)
        name : 헤더명 (ex:상완둘레_)
        total : 계산할 둘레의 수 (ex:상완둘레_1~5 : total = 5) 
    Returns:
        둘레의 평균값 반환
    """
    avg = 0.0

    for i in range(total):
        if data_Sheet1[item][name+str(i+1)] == "nan":
            return "nan"
        avg +=float(data_Sheet1[item][name+str(i+1)])

    return avg/total

def getPercentToValue(total, val, kg):
    """질량 계산

    Args:
        total : 신체 체적의 총합
        val : 계산될 부위의 체적
        kg : 총 몸무게
    Returns:
        총 kg의 n% 만큼의 질량을 반환
    """
    per = (val/total)*100.0

    mass = per * (kg/100.0)

    return mass



data_Sheet1 = dict()
data_Inbody = dict()
data_3DScan = dict()
id_list = list()


data = pd.read_excel(str(files[0]), sheet_name="Sheet1", engine='openpyxl')
key_name = getKeyList(data)
getSeetDataMap('등록번호', data_Sheet1, data, key_name)

data = pd.read_excel(str(files[0]), sheet_name="Inbody", engine='openpyxl')
key_name = getKeyList(data)
getSeetDataMap('차트번호', data_Inbody, data, key_name)

data = pd.read_excel(str(files[0]), sheet_name="3D스캔", engine='openpyxl')
key_name = getKeyList(data)
getSeetDataMap('차트번호', data_3DScan, data, key_name)


for item in id_list:

    print(str(data_Sheet1[item]))

    #엑셀에서 필수 값이 입력되어있는 경우에만 urdf 파일을 생성하도록 조건을 걸어두었습니다.
    if str(clavicle_link(item)) != 'nan'  and str(chest_link(item)) != 'nan' and str(waist_link(item)) != 'nan' and str(ventral_link(item)) != 'nan' and str(hip_link(item)) != 'nan' and str(forearm_link(item)) != 'nan' :
        checkList = dict()


        shoulder_flex_R = degToRad(data_Sheet1[item]['어깨_굴곡_R'])
        shoulder_exten_R = -degToRad(data_Sheet1[item]['어깨_신전_R'])
        shoulder_in_R = degToRad(data_Sheet1[item]['어깨_내회전_R'])
        shoulder_out_R = -degToRad(data_Sheet1[item]['어깨_외회전_R'])
        elbow_flex_R = degToRad(data_Sheet1[item]['팔꿈치_굴곡_R'])
        elbow_exten_R = -degToRad(data_Sheet1[item]['팔꿈치_신전_R'])
       
        shoulder_flex_L = degToRad(data_Sheet1[item]['어깨_굴곡_L'])
        shoulder_exten_L = -degToRad(data_Sheet1[item]['어깨_신전_L'])
        shoulder_in_L = -degToRad(data_Sheet1[item]['어깨_내회전_L'])
        shoulder_out_L = degToRad(data_Sheet1[item]['어깨_외회전_L'])
        elbow_flex_L = degToRad(data_Sheet1[item]['팔꿈치_굴곡_L'])
        elbow_exten_L = -degToRad(data_Sheet1[item]['팔꿈치_신전_L'])

        posterior_out_R = degToRad(data_Sheet1[item]['둔부_외회전_R'])
        posterior_in_R = -degToRad(data_Sheet1[item]['둔부_내회전_R'])
        knee_flex_R = -degToRad(data_Sheet1[item]['무릎_굴곡_R'])
        
        posterior_out_L = degToRad(data_Sheet1[item]['둔부_외회전_L'])
        posterior_in_L = -degToRad(data_Sheet1[item]['둔부_내회전_L'])
        knee_flex_L = -degToRad(data_Sheet1[item]['무릎_굴곡_L'])
        
        knee_str_exten_L = kgToNm(data_Sheet1[item]['하지근력_굴곡력_L'])
        knee_str_flex_L = kgToNm(data_Sheet1[item]['하지근력_신전력_L'])
    
        knee_str_exten_R = kgToNm(data_Sheet1[item]['하지근력_굴곡력_R'])
        knee_str_flex_R = kgToNm(data_Sheet1[item]['하지근력_신전력_R'])

        shoulder_str_exten_L = kgToNm(data_Sheet1[item]['어깨근력_굴곡력_L'])
        shoulder_str_flex_L = kgToNm(data_Sheet1[item]['어깨근력_신전력_L'])

        shoulder_str_exten_R = kgToNm(data_Sheet1[item]['어깨근력_굴곡력_R'])
        shoulder_str_flex_R = kgToNm(data_Sheet1[item]['어깨근력_신전력_R'])

        elbow_str_exten_L = kgToNm(data_Sheet1[item]['팔꿈치_굴곡력_L'])
        elbow_str_flex_L = kgToNm(data_Sheet1[item]['팔꿈치_신전력_L'])
    
        elbow_str_exten_R = kgToNm(data_Sheet1[item]['팔꿈치_굴곡력_R'])
        elbow_str_flex_R = kgToNm(data_Sheet1[item]['팔꿈치_신전력_R'])

        hip_joint_str_exten_L = kgToNm(data_Sheet1[item]['고관절_굴곡력_L'])
        hip_joint_str_flex_L = kgToNm(data_Sheet1[item]['고관절_신전력_L'])
        
        hip_joint_str_exten_R = kgToNm(data_Sheet1[item]['고관절_굴곡력_R'])
        hip_joint_str_flex_R = kgToNm(data_Sheet1[item]['고관절_신전력_R'])


        #미입력된 값이 있는지 확인하는 용도입니다.
        checkList['shoulder_flex_R'] = shoulder_flex_R
        checkList['shoulder_exten_R'] = shoulder_exten_R
        checkList['shoulder_in_R'] = shoulder_in_R
        checkList['shoulder_out_R'] = shoulder_out_R
        checkList['elbow_flex_R'] = elbow_flex_R
        checkList['elbow_exten_R'] = elbow_exten_R
        checkList['shoulder_flex_L'] = shoulder_flex_L
        checkList['shoulder_exten_L'] = shoulder_exten_L
        checkList['shoulder_in_L'] = shoulder_in_L
        checkList['shoulder_out_L'] = shoulder_out_L
        checkList['elbow_flex_L'] = elbow_flex_L
        checkList['elbow_exten_L']  = elbow_exten_L
        checkList['posterior_out_R'] = posterior_out_R
        checkList['posterior_in_R'] = posterior_in_R
        checkList['knee_flex_R'] = knee_flex_R
        checkList['posterior_out_L'] = posterior_out_L
        checkList['posterior_in_L'] = posterior_in_L
        checkList['knee_str_exten_L'] = knee_str_exten_L
        checkList['knee_flex_L']= knee_flex_L
        checkList['knee_str_flex_L'] = knee_str_flex_L
        checkList['knee_str_exten_R'] = knee_str_exten_R
        checkList['knee_str_flex_R'] = knee_str_flex_R
        checkList['shoulder_str_exten_L'] = shoulder_str_exten_L
        checkList['shoulder_str_flex_L'] = shoulder_str_flex_L
        checkList['shoulder_str_exten_R'] = shoulder_str_exten_R
        checkList['shoulder_str_flex_R'] = shoulder_str_flex_R
        checkList['elbow_str_exten_L'] = elbow_str_exten_L
        checkList['elbow_str_flex_L'] = elbow_str_flex_L
        checkList['elbow_str_exten_R']  = elbow_str_exten_R
        checkList['elbow_str_flex_R'] = elbow_str_flex_R
        checkList['hip_joint_str_exten_L'] = hip_joint_str_exten_L
        checkList['hip_joint_str_flex_L'] = hip_joint_str_flex_L
        checkList['hip_joint_str_exten_R'] = hip_joint_str_exten_R
        checkList['hip_joint_str_flex_R'] = hip_joint_str_flex_R

        isNAN = False
        for check in checkList.values():
            print(check)
            if check == "nan":
                True
                break
        
        if isNAN ==  True:
            continue

        knee_str_L = getMass(knee_str_exten_L, knee_str_flex_L)
        knee_str_R = getMass(knee_str_exten_R, knee_str_flex_R)

        shoulder_str_L = getMass(shoulder_str_exten_L, shoulder_str_flex_L)
        shoulder_str_R = getMass(shoulder_str_exten_R, shoulder_str_flex_R)

        elbow_str_L = getMass(elbow_str_exten_L, elbow_str_flex_L)
        elbow_str_R = getMass(elbow_str_exten_R, elbow_str_flex_R)

        hip_joint_str_L = getMass(hip_joint_str_exten_L, hip_joint_str_flex_L)
        hip_joint_str_R = getMass(hip_joint_str_exten_R, hip_joint_str_flex_R)
        
        #머리 무게 n%
        head_kg = 10

        totla_kg =  data_Sheet1[item]['몸무게'] - (data_Sheet1[item]['몸무게'] / 100 * head_kg)
        #print("몸무게 : " + str(data_Sheet1[item]['몸무게']))
        upper_eight_Avg = V_Avg(item, '상완둘레_', 5)
        row_eight_Avg = V_Avg(item, '하완둘레_', 5)
        #print('상완둘레 : ' + str(upper_eight_Avg))
        #print('하완둘레 : ' + str(row_eight_Avg))

        upper_leg_Avg = V_Avg(item, '허벅지둘레_', 5)
        row_leg_Avg = V_Avg(item, '종아리둘레_', 5)

        #print('허벅지둘레 : ' + str(upper_leg_Avg))
        #print('종아리둘레 : ' + str(row_leg_Avg))
        
        chest_Avg = data_Sheet1[item]['가슴둘레']
        waist_Avg = data_Sheet1[item]['허리둘레']
        root_Avg = data_Sheet1[item]['골반둘레']

        #print('가슴둘레 : ' + str(chest_Avg))
        #print('허리둘레 : ' + str(waist_Avg))
        #print('골반둘레 : ' + str(root_Avg))

        total = upper_eight_Avg+row_eight_Avg+upper_leg_Avg+row_leg_Avg+chest_Avg+waist_Avg+root_Avg

        #print("둘레 총 합 : "+str(total))
        #print("=========================================================")
        #상완 질량
        upper_eight_Kg = getPercentToValue(total, upper_eight_Avg, totla_kg)
        #하완 질량
        row_eight_Kg = getPercentToValue(total, row_eight_Avg, totla_kg)
        #허벅지 질량
        upper_leg_Avg = getPercentToValue(total, row_eight_Avg, totla_kg)
        #종아리 질량
        row_leg_Avg = getPercentToValue(total, row_eight_Avg, totla_kg)
        #가슴 질량
        chest_Avg = getPercentToValue(total, chest_Avg, totla_kg)
        #허리 질량
        waist_Avg = getPercentToValue(total, waist_Avg, totla_kg)
        #골반 질량
        root_Avg  = getPercentToValue(total, root_Avg, totla_kg)


    f = open(item+".urdf", "w+")
    f.write(urdf.create_URDF(item, hip_link(item),
                            forearm_link(item),
                            shoulder_link(item),
                            elbow_link(item),
                            clavicle_link(item),
                            shoulder_flex_R,
                            shoulder_exten_R,
                            shoulder_in_R,
                            shoulder_out_R, 
                            elbow_flex_R,
                            elbow_exten_R,
                            shoulder_flex_L,
                            shoulder_exten_L,
                            shoulder_in_L,
                            shoulder_out_L,
                            elbow_flex_L,
                            elbow_exten_L,
                            posterior_out_R,
                            posterior_in_R,
                            knee_flex_R,
                            posterior_out_L,
                            posterior_in_L,
                            knee_flex_L,
                            knee_str_L,
                            knee_str_R,
                            shoulder_str_L,
                            shoulder_str_R,
                            elbow_str_L,
                            elbow_str_R,
                            hip_joint_str_L,
                            hip_joint_str_R,
                            upper_eight_Kg,
                            row_eight_Kg,
                            upper_leg_Avg,
                            row_leg_Avg,
                            chest_Avg,
                            waist_Avg,
                            root_Avg
                            ))