import { ThumbUpIcon } from "@heroicons/react/outline";
import Image from "next/image";
import SnowImg from "../public/snowman.png";

function Thumbnail({ results }) {
  return (
    <div>
      {results.map((info) => (
        // eslint-disable-next-line react/jsx-key
        <div className="p-2 group cursor-pointer transform duration-200 ease-in transition sm:hover:scale-105 hover:z-50">
          <Image layout="responsive" src={SnowImg} height={1080} width={1920} />
          <div className="p-2">
            <h2 className="mt-1 text-2xl transition-all duration-100 ease-in-out group-hover:font-bold">
              {info.area_name}
            </h2>

            <p className="truncate max-w-md">■積雪量: {info.snow_volume}cm</p>
            <p className="truncate max-w-md">■コース数: {info.course}</p>
            <p className="truncate max-w-md">■住所: {info.address}</p>
            <p className="truncate max-w-md">■リフト券: {info.lift_charges}</p>
            <p className="truncate max-w-md">■営業時間: {info.business_hours}</p>

            <p className="flex items-center opacity-0 group-hover:opacity-100">
            --
              <ThumbUpIcon className="h-5 mx-2" /> いいね!
            </p>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Thumbnail;
