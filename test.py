a = [1,2,3,4,5,6,7]
import json


st = """
    GROUP_CONCAT(CONCAT('{"id":', pvc.clause_type_id, ', "constraint":',pvc.constraint, ', "key":"', ct.key,'"}')  SEPARATOR ';')
"""

s = """{"id":1, "constraint":{"min": 1}, "key":"HOUR"};{"id":5, "constraint":{"usage": 1}, "key":"USAGE"}"""


d = s.split(';')
for i in d:
    l = json.loads(i)
    print(l["key"])

    """
    select (case when substring(max(sk.sku_repr), 9, 1)="0" then ((sum(case when (o.actual_duration is null or o.actual_duration=0) then (case when duration_unit='HOURS' then o.duration else o.duration/60 end) else o.actual_duration/3600 end))) end) as hours,
    (case when substring(max(sk.sku_repr), 9, 1)="0" then ((sum(case when (o.actual_duration is null or o.actual_duration=0) then (case when duration_unit='HOURS' then o.duration*3600 else o.duration*60 end) else o.actual_duration end))/(8400)) end) as asset_util,
    date(convert_tz(ifnull(o.work_started_at, ifnull(o.work_ended_at, ifnull(o.rescheduled_time, ifnull(o.scheduled_on, o.placed_on)))), 'UTC', 'Asia/Kolkata')) as date, 
    s.id as supplier_id,
    l2.state_location_id as state_location,
    st.id as instrument_id,
    "Tractor" as instrument_type 
    from orders o 
    left join order_desired_implements odi on odi.order_id=o.id 
    left join order_suppliers os on os.order_id = o.id 
    left join sku sk on sk.sku=odi.desired_implement_sku_id 
    left join suppliers s on s.id=os.supplier_id 
    inner join supplier_tractors st on st.supplier_id=os.supplier_id 
    inner join order_assigned_tractors oat on oat.order_id=o.id and oat.tractor_id=st.id 
    left join farm_lands fl on fl.id=o.farm_land_id 
    left join locations l on l.id=fl.location_id 
    left join (select l.name, l.state_code, sc.state_location_id 
    from state_codes sc 
    inner join locations l on sc.state_location_id=l.id 
    where sc.state_location_id is not null) l2 on l.state_code=l2.state_code 
    where l.state_code <> 9999 
    and o.status in ('Feedback', 'Work Completed', 'Order Completed', 'Partially Paid', 'Payment Completed') 
    and date(convert_tz(ifnull(o.work_started_at, ifnull(o.work_ended_at, ifnull(o.rescheduled_time, ifnull(o.scheduled_on, o.placed_on)))), 'UTC', 'Asia/Kolkata'))
     between "2018-01-05" and "2018-07-20"
    group by date, state_location, supplier_id, instrument_id, instrument_type;
    """