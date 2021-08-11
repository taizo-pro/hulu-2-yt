import Thumbnail from "./Thumbnail"

function Results({ results }) {
  return (
    <div className="px-5 sm:grid md:grid-cols-2 xl:grid-cols-3 3xl:flex flex-wrap justify-center">
      <Thumbnail results={results}/>
      {/* <ul>
        {results.map(info => (
          <li key={info.id}>
          <p>■{info.area_name}</p>
          <p>【積雪量】{info.snow_volume}</p>
          <p>【コース数】{info.course}</p>
          <p>【住所】{info.address}</p>
          <p>【リフト代】{info.lift_charges}</p>
          <p>【営業時間】{info.business_hours}</p>
          <p>【取得元URL】{info.original_page_url}</p>
          <br></br>
          </li>
        ))}
      </ul> */}
    </div>
  );
}

export default Results;
